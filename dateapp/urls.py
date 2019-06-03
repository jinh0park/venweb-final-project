from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('content', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
]