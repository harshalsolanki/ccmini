from django.shortcuts import render
from .models import User
import random

# Create your views here.

def register_tours():
	tours = ['Elephant Nature Park (Thailand)', 'Lone Pine Koala Sanctuary - Australia', 'Bandhavgarh National Park, Madhya Pradesh']
	random.shuffle(tours)
	return tours[0] + "&&" + tours[1]

def welcome(request):
	user_name = request.POST.get('username')
	pass_word = request.POST.get('password')
	try:
		current_user = User.objects.get(username = user_name)
	except:
		return render(request, 'registration/login.html',{})
		
	if pass_word == current_user.password:
		tour = current_user.tours
		tour_list = tour.split('&&')
		return render(request, 'wild/wt.html',{"name":current_user.first, "tours":tour_list})

	return render(request, 'registration/login.html',{})


def signup(request):

	return render(request, 'registration/signup.html', {})

def register(request):
	user_name = request.POST.get('username')
	first_name = request.POST.get('FirstName')
	last_name = request.POST.get('LastName')
	email_add = request.POST.get('email')
	psw = request.POST.get('psw')
	tour = register_tours()
	current_user = User(username = user_name, first = first_name, password=psw, last = last_name,email = email_add,tours =tour)
	current_user.save()
	
	return render(request, 'registration/login.html',{})

