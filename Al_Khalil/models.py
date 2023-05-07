from django.db import models
from django.urls import reverse


class Jai_Namaz(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to='jai_namaz')
    price = models.IntegerField(blank=False)


class Tasbih(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to='tasbih')
    price = models.IntegerField(blank=False)


class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to='book')
    price = models.IntegerField(blank=False)


class Youtube(models.Model):
    name = models.URLField(max_length=500)


def __str__(self):
    return self.title