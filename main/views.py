from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill

def index(request):
    return render(request, 'main/index.html')
