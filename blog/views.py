from django.shortcuts import render, get_object_or_404
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
        facts = models.FactsMk.objects.all().order_by('-id')
        context = {
            "fighter": fighter,
            'facts': facts,
        }
    return render(request, template_name='fighters/fighter_list.html', context=context)

def fighter_detail_view(request, id):
    if request.method == 'GET':
        fighter_id = get_object_or_404(models.Fighter, id=id)
        context = {
            'fgt_id': fighter_id
        }
    return render(request, template_name='fighters/fighter_detail.html', context=context )
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