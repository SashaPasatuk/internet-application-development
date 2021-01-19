from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel, name='main'),
    path('economy_room', views.economy, name='economy'),
    path('standart_room', views.standart, name='normal'),
    path('lux_room', views.lux, name='lux'),
    path('list_room', views.list_room, name='list'),
]
