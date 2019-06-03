from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout ,authenticate
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'main/welcome.html')

@login_required
def index(request):
    return render(request, 'main/index.html')


@login_required
def register(request):
    return render(request, 'main/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            django_login(request, user)
            return redirect('index')
        else:
            return render(request, 'main/login.html')
    else:
        if request.user.is_authenticated:
            django_logout(request)
            return render(request, 'main/login.html')
        else:
            return render(request, 'main/login.html')


def forgot_password(request):
    return render(request, 'main/forgot-password.html')
