from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name="home"),
    path('persons/', views.persons_mk_view, name='persons_mk'),
    path('fighter_list/', views.fighter_list_view, name='fighter_list')
]