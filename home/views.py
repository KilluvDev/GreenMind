#Django
from django.shortcuts import render, redirect
from .models import *
from .models import Post
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import ProductForm
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
	posts = Post.objects.filter(user=request.user)
	context = { 'posts': posts}
	return render(request,'recordhistory.html', context)

def calculator(request):

	form = ProductForm()

	if request.method == 'POST':
		Cantidadfinal = int(request.POST['Cantidad'])
		ModelAutofinal = int(request.POST['ModelAuto'])#
		Usosfinal = int(request.POST['Usos'])#
		Diasfinal = int(request.POST['Días'])#
		Luzfinal = int(request.POST['Luz'])#
		Gasfinal = int(request.POST['Gas'])#
		Dietafinal = int(request.POST['Dieta'])#
		Plasticofinal = int(request.POST['Plastico'])

		Emisiones = (Luzfinal * 0.38 ) / Cantidadfinal
		Emisiones += (Gasfinal * 0.19) / Cantidadfinal
		if ModelAutofinal==1:
			Emisiones += 0.109 * (Usosfinal*365)
		elif ModelAutofinal==2:
			Emisiones += 0.153 * (Usosfinal*365)
		elif ModelAutofinal==3:
			Emisiones += 0.195 * (Usosfinal*365)
		Emisiones += Diasfinal*0.07*15
		if Dietafinal==0:
			Emisiones += 1300
		elif Dietafinal==1:
			Emisiones += 1000
		elif Dietafinal==2:
			Emisiones += 790
		elif Dietafinal==3:
			Emisiones += 560
		elif Dietafinal==4:
			Emisiones += 660
		Emisiones += Plasticofinal * 3.5
		Emisiones = round(Emisiones / 1000,2)
		Emisiones = str(Emisiones)
		Emisiones += ' Tons CO2'
		form = ProductForm(request.POST)
		if form.is_valid():
			print("valido")
			p = Post(user = request.user)
			p.content = Emisiones
			p.save()
	return render(request,'calculator.html', {'form':form})

class RegisterPage(FormView):
	template_name='register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(RegisterPage, self).form_valid(form)

