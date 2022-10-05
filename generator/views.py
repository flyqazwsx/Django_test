from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print('Hello Django')

    return render(request, 'index.html', {'password': 123456})
