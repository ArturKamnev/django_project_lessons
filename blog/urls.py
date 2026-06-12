from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('pesons_mk/', views.PersonsMkView.as_view(), name='persons_mk'),
    path('fighter_list/', views.FighterListView.as_view(), name='fighter_list'),
    path('fighter_list/<int:id>/', views.FighterDetailView.as_view(), name="fgt_id"),
    path('search/', views.SearchView.as_view(), name='search'),
]