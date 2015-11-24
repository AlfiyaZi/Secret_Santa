from django.shortcuts import render, redirect
from django.contrib import messages
from apps.home.models import User

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


	if not User.objects.all().filter(username=username):
		messages.add_message(request, messages.INFO, 'Username is invalid')
		errors += 1
		return redirect('/')
	else:
		if password != User.objects.all().filter(username=username).password:
			messages.add_message(request, messages.INFO, 'Password is invalid')
			errors += 1
			return redirect('/')
		else:
			return redirect('/dashboard')

def dashboard(request):

	return render(request, 'home/dashboard.html')