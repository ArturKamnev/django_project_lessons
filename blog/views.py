from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.core.paginator import Paginator
from django.db.models import F

# Create your views here.

def home_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World')
    
def fighter_list_view(request):
    if request.method == 'GET':
        fighter = models.Fighter.objects.all().order_by('-id')
        facts = models.FactsMk.objects.all().order_by('-id')
        paginator = Paginator(fighter, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        context = {
            "fighter": page_obj,
            'facts': facts,
        }
    return render(request, template_name='fighters/fighter_list.html', context=context)

def fighter_detail_view(request, id):
    if request.method == 'GET':
        fighter_id = get_object_or_404(models.Fighter, id=id)
        views_blog = request.session.get('viewed_blog', [])

        if id not in views_blog:
            fighter_id.views = F('views')+1
            fighter_id.save()
            fighter_id.refresh_from_db
        views_blog.append(id)
        request.session['viewed_blog'] = views_blog

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

def search_view(request):
    query = request.GET.get('s', '')
    if query:
        fighter = models.Fighter.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Блог не найден')
    return render(request, template_name='fighters/fighter_list.html', context={'fighter': fighter})

