#Django
from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Utilities
from datetime import datetime

#import pdb; pdb.set_trace()   Debuger


def home(request):
	return render(request,'index.html', {})

def profile(request):
	posts = Post.objects.all()
	context = { 'posts': posts}
	return render(request, 'profile.html', context)


def historyofuse(request):
	posts = Post.objects.all()
	context = { 'posts': posts}
	return render(request,'recordhistory.html', context)

def calculator(request):
	return render(request,'calculator.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			message.success(request, f'Usuario {username} creado')
	else:
		form = UserCreationForm()

	context = { 'form ': form}
	return render(request, 'register.html', context)