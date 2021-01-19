from django.contrib import admin
from .models import Room, Guest


class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'count', 'type', 'price')


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'amount', 'data1', 'data2')


admin.site.register(Room, RoomAdmin)
admin.site.register(Guest, GuestAdmin)
