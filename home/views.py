#Django
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import UserCreation
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Utilities
from datetime import datetime

#import pdb; pdb.set_trace()   Debuger


def home(request):
	return render(request,'index.html', {})

def profile(request):
	posts = Profile.objects.all()
	context = { 'posts': posts}
	return render(request, 'profile.html', context)


class get_name(LoginView):
	template_name = 'login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return '../'



def historyofuse(request):
	posts = Post.objects.all()
	context = { 'posts': posts}
	return render(request,'recordhistory.html', context)

def calculator(request):
	return render(request,'calculator.html')

def register(request):
	return render(request, 'register.html')
