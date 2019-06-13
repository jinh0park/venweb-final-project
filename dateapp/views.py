from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse
from .models import Spot


def welcome(request):
    spots = Spot.objects.all()[:2]
    return render(request, 'dateapp/welcome.html', {'spots':spots})


@login_required
def index(request):
    spots = Spot.objects.all()
    return render(request, 'dateapp/index.html', {'spots': spots})


def register(request):
    return render(request, 'dateapp/register.html')


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
            return render(request, 'dateapp/login.html')
    else:
        if request.user.is_authenticated:
            django_logout(request)
            return render(request, 'dateapp/login.html')
        else:
            return render(request, 'dateapp/login.html')


def forgot_password(request):
    return render(request, 'dateapp/forgot-password.html')


class SpotDetailView(DetailView):
    model = Spot
    context_object_name = 'spot'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spots'] = Spot.objects.all()
        return context

