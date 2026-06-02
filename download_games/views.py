from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
# Create your views here.

# CReate games
def create_game_view(request):
    if request.method == "POST":
        form = forms.GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/games_list/')
    else:
        form = forms.GameForm()

    context = {
        'form': form
    }
    return render(request, template_name='crud/create_game.html', context=context)


def games_list_view(request):
    if request.method == "GET":
        games = models.Games.objects.all().order_by('-id')
        context = {
            'games': games
        }
    return render(request=request, template_name='crud/games_list.html', context=context)

def update_games_view(request, id):
    game_id = get_object_or_404(models.Games, id=id)
    if request.method == "POST":
        form = forms.GameForm(request.POST, instance=game_id)
        if form.is_valid():
            form.save()
            return redirect('/games_list/')
    else:
        form = forms.GameForm(instance=game_id)

    context = {
        "form": form,
        "game_id": game_id,
    }
    return render(request=request, template_name="crud/update_game.html", context=context)

def delete_games_view(request, id):
    game_id = get_object_or_404(models.Games, id=id)
    game_id.delete()
    return redirect('/games_list/')