from django.db import models
from django.urls import reverse


class Guest(models.Model):
    name = models.CharField('ФИО', max_length=100)
    phone = models.CharField('Номер телефона', max_length=11)
    amount = models.IntegerField('Количество постояльцев')
    data1 = models.DateField('Дата заезда')
    data2 = models.DateField('Дата выезда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Постояльцы'
        verbose_name_plural = 'Постояльцы'
        ordering = ["data1"]


class Room(models.Model):
    number = models.CharField('Номер', max_length=15)
    count = models.IntegerField('Вместимость, чел.')
    type = models.CharField('Тип номера', max_length=10)
    price = models.PositiveSmallIntegerField('Цена за сутки, руб.')
    name = models.ManyToManyField(Guest, verbose_name='ФИО', related_name='Name')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Номера'
        verbose_name_plural = 'Номера'

    def get_absolute_url(self):
        return reverse("rooms_detail", kwargs={"slug": self.url})
