from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
# Create your views here.

# CReate games

class CreateGameView(generic.CreateView):
    form_class = forms.GameForm
    template_name = 'crud/create_game.html'
    success_url = '/games_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateGameView, self).form_valid(form=form)

class GamesListView(generic.ListView):
    template_name = 'crud/games_list.html'
    model = models.Games
    paginate_by = 2
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['games'] = self.model.objects.all()
        return context

# def create_game_view(request):
#     if request.method == "POST":
#         form = forms.GameForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/games_list/')
#     else:
#         form = forms.GameForm()

#     context = {
#         'form': form
#     }
#     return render(request, template_name='crud/create_game.html', context=context)


# def games_list_view(request):
#     if request.method == "GET":
#         games = models.Games.objects.all().order_by('-id')
#         context = {
#             'games': games
#         }
#     return render(request=request, template_name='crud/games_list.html', context=context)

class UpdateGameView(generic.UpdateView):
    template_name = 'crud/update_game.html'
    model = models.Games
    form_class = forms.GameForm
    success_url = '/games_list/'

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=game_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateGameView, self).form_valid(form=form)

class DeleteGameView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    model = models.Games
    success_url = '/games_list/'
    context_object_name = 'game_id'

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=game_id)
    


# def update_games_view(request, id):
#     game_id = get_object_or_404(models.Games, id=id)
#     if request.method == "POST":
#         form = forms.GameForm(request.POST, instance=game_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/games_list/')
#     else:
#         form = forms.GameForm(instance=game_id)

#     context = {
#         "form": form,
#         "game_id": game_id,
#     }
#     return render(request=request, template_name="crud/update_game.html", context=context)

# def delete_games_view(request, id):
#     game_id = get_object_or_404(models.Games, id=id)
#     game_id.delete()
#     return redirect('/games_list/')