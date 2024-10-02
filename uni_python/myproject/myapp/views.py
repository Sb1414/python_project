from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
import requests
from datetime import datetime
from .github_api import get_github_data

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def info(request):
    username = 'Sb1414'
    github_data = get_github_data(username)
    return render(request, 'myapp/info.html', {'github_data': github_data})
