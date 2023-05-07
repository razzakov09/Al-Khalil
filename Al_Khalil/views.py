from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *


def index(request):
    jainamaz = Jai_Namaz.objects.all()
    tasbih = Tasbih.objects.all()
    book = Book.objects.all()
    youtube = Youtube.objects.all()
    data = {'jainamaz': jainamaz,
            'tasbih': tasbih,
            'book': book,
            'youtube': youtube}
    return render(request, 'index.html', context=data)