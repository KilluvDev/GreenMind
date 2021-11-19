#Django
from django.http import HttpResponse
from django.shortcuts import render

# Utilities
from datetime import datetime


#Json
import json

#import pdb; pdb.set_trace()   # Debuger

def home(request):
	return render(request,'index.html',{})

def form(request):
	return render(request,'forms.html',{})

def history(request):
	return render(request,'history.html',{})

def useracc(request):
	return render(request,'user.html',{})