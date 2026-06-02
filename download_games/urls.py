from django.urls import path
from . import views

urlpatterns = [
    path('create_game/', views.create_game_view, name='create_game'),
    path('games_list/', views.games_list_view, name='games_list'),
    path('games_list/<int:id>/update/', views.update_games_view, name='update_game'),
    path('games_list/<int:id>/delete/', views.delete_games_view, name='delete_game'),
]