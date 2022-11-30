from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import administrator
from django.contrib.auth.models import User, Group 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def register(response):
    # In future, check if passwords match
    if response.method == "POST":
        form = RegisterForm(response.POST)
        username = response.POST['username']
        email = response.POST['email']
        password = response.POST['password1']
        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect("login")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def login(response):
    if response.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    else:
        form = LoginForm()
        return render(response, "registration/login.html", {"form": form})