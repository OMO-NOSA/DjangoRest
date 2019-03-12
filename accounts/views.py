from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from . models import CustomUser
from . forms import (
                    RegisterForm,
                    LoginForm,
                            )


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
            
    return render(request, 'accounts/register.html', {'form':form})
    

def login(request):
    if request.method == "POST":
      #Get the posted form
        form = LoginForm(request.POST)
      
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = LoginForm()
            
    return render(request, 'accounts/login.html', {'form':form})
		

def logout(request):
    logout(request)
    return redirect("login")