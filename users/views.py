from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm
from django.contrib import messages

def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request,'Registered Successfully')
			return redirect('users:login')
		

			
	else:
		form = RegisterForm()
	template_name = 'users/register.html'
	context = {'form':form}
	return render(request,template_name,context)


def login_view(request):
	if request.method=='POST':
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			user.save()
			if user is not None:
				login(request,user)
				messages.success(request,f'You are now logged in as {username}')
				return redirect('wordmeaning:main')
			else:
				messages.error(request,'Invalid')

	else:
		form =AuthenticationForm()
	template_name = 'users/login.html'
	context = {'form':form}
	return render(request,template_name,context)


def logout_view(request):
	logout(request)
	messages.success(request,'Logged out Successfully')
	return redirect('users:login')