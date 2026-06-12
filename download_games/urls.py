from django.urls import path
from . import views

urlpatterns = [
    path('create_game/', views.CreateGameView.as_view(), name='create_game'),
    path('games_list/', views.GamesListView.as_view(), name='games_list'),
    path('games_list/<int:id>/update/', views.UpdateGameView.as_view(), name='update_game'),
    path('games_list/<int:id>/delete/', views.DeleteGameView.as_view(), name='delete_game'),
]