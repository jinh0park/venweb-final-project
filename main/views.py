from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def sample_generic(request):
    return render(request, 'main/generic.html')
