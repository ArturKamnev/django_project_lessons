from django.shortcuts import render
from . import models
# Create your views here.

def car_list_view(request):
    if request.method == "GET":
        cars = models.Car.objects.all()
        context = {
            'cars': cars,
        }
    return render(request, template_name='cars.html', context=context)