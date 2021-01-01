from django.shortcuts import render


def show_land(request):
    return render(request, 'land/countries.html')


def show_city_rus(request):
    return render(request, 'land/city_rus.html')


def show_city_ger(request):
    return render(request, 'land/city_ger.html')


def show_city_jp(request):
    return render(request, 'land/city_jp.html')
