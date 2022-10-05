from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.


def password(request):
    return render(request, './password.html', {'password': 123456})


def index(request):
    print('Hello Django')

    return render(request, 'index.html',)
