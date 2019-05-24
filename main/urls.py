from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('sample', views.sample_generic, name='sample')
]