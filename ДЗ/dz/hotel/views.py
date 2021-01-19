from django.shortcuts import render, redirect
from .models import Room


def hotel(request):
    return render(request, 'hotel/hotel.html')


def economy(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/economy.html', {'economy': rooms})


def standart(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/standart.html', {'standart': rooms})


def lux(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/lux.html', {'lux': rooms})


def list_room(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/rooms.html', {'list': rooms})
