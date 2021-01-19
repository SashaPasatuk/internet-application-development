# Generated by Django 3.1.5 on 2021-01-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='number',
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.ManyToManyField(related_name='Name', to='hotel.Guest', verbose_name='ФИО'),
        ),
    ]
