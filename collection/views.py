from django.http.response import Http404
from django.shortcuts import render
from main.models import Skill
from .helpers.collect import get_big_companies, working_with_models
from .helpers.queries import add_data

def collect(request):
    if Skill.objects.count() < 1:
        raise Http404("404.html is shown")  # 404.html page is returned
    
    context = {
        'big_companies': get_big_companies(),
        'skills': Skill.objects.all(),
        'working_with_models': working_with_models(),
        'favicon': "favicon.png", 
    }
    return render(request, 'collection/collect.html', context)

def queries(request, opt:int):
    context = {}
    if opt == 1:
        context = { "data": add_data() }
    return render(request, 'collection/queries.html', context)
 