from django.shortcuts import render, redirect
from django.contrib import messages
from apps.home.models import User, Item
from amazon.api import AmazonAPI




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
		messages.add_message(request, messages.INFO, 'Name cannot be blank')
		errors += 1
	if not username:
		messages.add_message(request, messages.INFO, 'Username cannot be blank')
		errors += 1
	if not password:
		messages.add_message(request, messages.INFO, 'Password cannot be blank')
		errors += 1
	if not confirm:
		messages.add_message(request, messages.INFO, 'Confirmation cannot be blank')
		errors += 1
	if password != confirm:
		messages.add_message(request, messages.INFO, 'Password must match confirm')
		errors += 1

	if errors == 0:
		User.objects.create(name=name, username=username, password=password, admin=admin)
		messages.add_message(request, messages.INFO, 'Successfully Registered!')

	return redirect('/')

def login(request):

	username = request.POST['username']
	password = request.POST['password']
	errors = 0

	if not User.objects.get(username=username):
		messages.add_message(request, messages.INFO, 'Username is invalid')
		errors += 1
		return redirect('/')
	else:
		if password != User.objects.get(username=username).password:
			messages.add_message(request, messages.INFO, 'Password is invalid')
			errors += 1
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

	try: # searches amazon for keyword and returns top 5 items 
		query = amazon.search_n(5, Keywords=search, SearchIndex='All')

	except:
		query = ""

	item = {
		'items': query,
	}
	
	return render(request, 'home/add.html',item)

