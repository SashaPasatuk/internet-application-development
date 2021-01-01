
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_land, name='countries'),
    path('russia', views.show_city_rus, name='russia'),
    path('germany', views.show_city_ger, name='germany'),
    path('japan', views.show_city_jp, name='japan'),
]