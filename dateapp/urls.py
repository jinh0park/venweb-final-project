from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('content', views.index, name='index'),
    path('login', views.login, name='login'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('register', views.register, name='register'),
    path('content/spot/<int:pk>', views.SpotDetailView.as_view(), name='spot-detail'),
]