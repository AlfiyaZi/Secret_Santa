from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import forms
from apps.home.models import User, Item, Wishlist
from amazon.api import AmazonAPI
from random import randint, shuffle

amazon = AmazonAPI('AKIAIHLZRKVT4Z7YA4DA', 'hh9fH8KhGG3P9EhMP4gWmeqsLnQSkejQMNiHK5oF','dojo0d-20')

def index(request):

	return render(request, 'home/index.html')

def register(request):

	name = request.POST['name']
	username = request.POST['username']
	password = request.POST['password']
	confirm = request.POST['confirm']
	admin = request.POST['admin']
	errors = 0

	if not name:
		messages.add_message(request, messages.INFO, 'Name cannot be blank', extra_tags="registration")
		errors += 1
	if not username:
		messages.add_message(request, messages.INFO, 'Username cannot be blank', extra_tags="registration")
		errors += 1
	users = User.objects.all()
	for user in users:
		if username == user.username:
			messages.add_message(request, messages.INFO, 'Username already taken', extra_tags="registration")
			errors += 1
	if not password:
		messages.add_message(request, messages.INFO, 'Password cannot be blank', extra_tags="registration")
		errors += 1
	if not confirm:
		messages.add_message(request, messages.INFO, 'Confirmation cannot be blank', extra_tags="registration")
		errors += 1
	if password != confirm:
		messages.add_message(request, messages.INFO, 'Password does not match', extra_tags="registration")
		errors += 1

	if errors == 0:
		User.objects.create(name=name, username=username, password=password, admin=admin)
		messages.add_message(request, messages.INFO, 'Successfully Registered!', extra_tags="registration")
		return redirect('dashboard')
	else:
		context = {
			'errors': messages
		}
		return render(request, 'home/register.html', context)

def login(request):

	username = request.POST['username']
	password = request.POST['password']
	errors = 0

	if not username:
		messages.add_message(request, messages.INFO, 'Please enter a username', extra_tags="login")
		errors += 1
	elif not User.objects.all().filter(username=username):
		messages.add_message(request, messages.INFO, 'Username is not valid', extra_tags="login")
		errors += 1
		return redirect('login_page')
	else:
		if User.objects.all().filter(username=username)[0].password != password:
			messages.add_message(request, messages.INFO, 'Password is invalid', extra_tags="login")
			errors += 1

	if errors == 0:
		request.session['user_id'] = User.objects.all().filter(username=username)[0].id
		return redirect('dashboard')
	else:
		context = {
			'errors': messages
		}
		return render(request, 'home/login.html', context)

def dashboard(request):

	context = {
		'name': User.objects.get(id=request.session['user_id']).name,
		'users': User.objects.all(),
		'user_id': User.objects.get(id=request.session['user_id']).id,
		'santa': User.objects.get(id=request.session['user_id']).santa,
		'my_items': Wishlist.objects.all().filter(user=request.session['user_id']),
		'other_items': Wishlist.objects.all().exclude(user=request.session['user_id'])
	}

	return render(request, 'home/dashboard.html', context)

def back(request):

	return redirect('dashboard')

def logout(request):

	return redirect('/')

def add(request):

	try:
		search = request.session['keyword']
		query = amazon.search_n(5, Keywords=search, SearchIndex='All')

	except:
		request.session['keyword'] = ''
		query = ""

	context = {
		'username': User.objects.get(id=request.session['user_id']).username,
		'items': query,
	}

	return render(request, 'home/add.html', context)

def search(request):

	request.session['keyword'] = request.POST['search']
	return redirect ('add')

def create(request):

	user = User.objects.all().filter(id=request.session['user_id'])[:1]
	itemTitle = request.POST['item.title']
	itemASIN = request.POST['item.asin']
	itemImage = request.POST['item.imgURL']
	itemPrice = request.POST['item.price']
	Item.objects.create(title=itemTitle, user=user[0], asin=itemASIN, imgURL=itemImage, price=itemPrice)

	item_id = Item.objects.all().filter(title=itemTitle)[0].id
	item = Item.objects.all().filter(id=item_id)

	Wishlist.objects.create(item=item[0], user=user[0])

	return redirect('dashboard')

def random(request):

	#  allUsers is a queryset
	allUsers = User.objects.all()
	#  users is a mutable list
	users = []
	for user in allUsers:
		users.append(user)

	#  shuffles user list
	shuffle(users)
	count = 0

	#  updates santa attribute in DB
	for user in users:
		user = User.objects.get(id=user.id)
		count += 1
		if count == len(allUsers):
			count = 0
		user.santa = users[count].name
		user.save()

	return redirect('dashboard')
	
def reset(request):
	allUsers = User.objects.all()
	for user in allUsers:
		user.santa = "No One...yet"
		user.save()

	return redirect('dashboard')

def deleteItem(request, item_id):

	Item.objects.get(id=item_id).delete()
	return redirect('dashboard')

def user(request, user_id):
	user = User.objects.get(id=user_id)

	context = {
		'user': User.objects.get(id=user_id),
		'items': Wishlist.objects.all().filter(user=user_id),
	}

	return render(request, 'home/user.html', context)

def deleteAcct(request, user_id):

	user = User.objects.get(id=user_id)
	user.delete()

	return redirect('/')

def login_reg(request):
	return render(request, 'home/register.html')

def login_page(request):
	return render(request, 'home/login.html')

