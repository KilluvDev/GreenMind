#Django
from django.shortcuts import render
from .models import *

# Utilities
from datetime import datetime

#import pdb; pdb.set_trace()   Debuger

def home(request):
	return render(request,'index.html', {})

def profile(request):
	
	return render(request, 'profile.html', {})


def historyofuse(request):
	posts = Post.objects.all()

	context = { 'posts': posts}
	return render(request,'profile.html', context)



'''
def form(request):
	return render(request,'.html', {})

def history(request):
	return render(request,'.html', {})


def useracc(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			message.success(request,f'Usuario {username} creado')
	else:
		form = UserCreationForm()

	context = { 'form ': form}
	return render(request, 'user.html', {})

	'''