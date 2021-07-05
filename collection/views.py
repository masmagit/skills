from django.shortcuts import render
from .collect import *

def collect(request):
    context = {
        'big_companies': get_big_companies(),
        'skills': Skill.objects.all(),
        'working_with_models': working_with_models()
    }
    return render(request, 'collection/collect.html', context)
