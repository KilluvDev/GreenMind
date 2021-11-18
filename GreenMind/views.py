#Django
from django.http import HttpResponse
from django.shortcuts import render

# Utilities
from datetime import datetime


#Json
import json

#import pdb; pdb.set_trace()   # Debuger

def home(request):
	
	return render(request,'/index.html')

