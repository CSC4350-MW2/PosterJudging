from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import administrator

# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        post = administrator()
        post.username = response.POST['username']
        post.email = response.POST['email']
        post.password = response.POST['password1']
        post.save()

        return redirect("login")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def login(response):
    if response.method == "POST":
        return redirect("administrator/")
    else:
        form = LoginForm()
        return render(response, "registration/login.html", {"form": form})