from django.shortcuts import render
from django.http import HttpResponse
from .operations import *
from .models import Skill

def index(request):
    return render(request, 'main/index.html')

def collect(request):
    context = {
        'big_companies': get_big_companies(),
        'skills': Skill.objects.all(),
    }
    return render(request, 'main/collect.html', context)
