from django.urls import path
from . import views

urlpatterns = [
    path('fighter_list/', views.fighter_list_view, name='fighter_list'),
    path('fighter_list/<int:id>/', views.fighter_detail_view, name="fgt_id"),
    path('search/', views.search_view, name='search'),
]