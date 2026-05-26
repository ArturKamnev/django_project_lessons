from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . import models
# Create your views here.

def home_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World')
    
def fighter_list_view(request):
    if request.method == 'GET':
        fighter = models.Fighter.objects.all().order_by('-id')
        context = {
            "fighter": fighter
        }
    return render(request, template_name='fighters/fighter_list.html', context=context)

def persons_mk_view(request):
    if request.method == "GET":
        context = {
            'title': 'Scorpion',
            'name': 'Hanzo Hasashi',
            'time': datetime.now(),
            'capabilities':[
                'kunai',
                'katana',
                'fite',
                'fatality fire'
            ]
        }
    return render(request, 'persons_mk.html', context)