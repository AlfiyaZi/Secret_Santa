from django.shortcuts import render, redirect
from django.contrib import messages
from apps.home.models import User, Item
from amazon.api import AmazonAPI
import bcrypt


amazon = AmazonAPI('AKIAIHLZRKVT4Z7YA4DA', 'hh9fH8KhGG3P9EhMP4gWmeqsLnQSkejQMNiHK5oF', 'dojo0d-20')

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
	if not password:
		messages.add_message(request, messages.INFO, 'Password cannot be blank', extra_tags="registration")
		errors += 1
	if not confirm:
		messages.add_message(request, messages.INFO, 'Confirmation cannot be blank', extra_tags="registration")
		errors += 1
	if password != confirm:
		messages.add_message(request, messages.INFO, 'Password must match confirm', extra_tags="registration")
		errors += 1

	if errors == 0:
		# password = password.encode("utf-8")
		# pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
		User.objects.create(name=name, username=username, password=password, admin=admin)
		messages.add_message(request, messages.INFO, 'Successfully Registered!', extra_tags="registration")

	return redirect('/')

def login(request):

	username = request.POST['username']
	password = request.POST['password']

	if not User.objects.all().filter(username=username):
		messages.add_message(request, messages.INFO, 'Username is invalid', extra_tags="login")
		return redirect('/')
	else:
		# pw_hash = User.objects.all().filter(username=username)[:1][0].password
		# if bcrypt.hashpw(password, pw_hash) == pw_hash:
		if User.objects.all().filter(username=username)[0].password != password:
			messages.add_message(request, messages.INFO, 'Password is invalid', extra_tags="login")
			return redirect('/')
		else:
			return redirect('dashboard')

def dashboard(request):

	return render(request, 'home/dashboard.html')

def back(request):

	return redirect('/')

def add(request):
	try:
		search = request.session['keyword']
	except:
		request.session['keyword'] = ''
	
	try:
		query = amazon.search_n(5, Keywords=search, SearchIndex='All')

	except:
		query = ""
	# lookup = amazon.lookup(ItemId ='B00251VAGK')
	# print lookup['images']
	item = {
		'items': query,
	}
	
	return render(request, 'home/add.html', item )



def search(request):
	request.session['keyword'] = request.POST['search']
	return redirect ('add')