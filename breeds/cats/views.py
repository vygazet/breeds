import os
from django.shortcuts import render
from .models import *
from PIL import Image
from django.conf import settings
from django.views import generic
from django.core.paginator import Paginator


menu = [{'title': "Pradžia", 'url_name': "index"},
        {'title': "Informacija", 'url_name': "info"},
        {'title': "Galerija", 'url_name': "gallery"},
        {'title': "Admin", 'url_name': "admin:login"},
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Pradinis puslapis',
        'title2': 'Visos pasaulio katės'
    }
    return render(request, 'cats/index.html', context=context)


def info(request):
    data = Breeds.objects.all()
    photos = Breeds.objects.all()
    paginator = Paginator(Breeds.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_breeds = paginator.get_page(page_number)
    context = {
        'data': data,
        'menu': menu,
        'title': 'Informacija',
        'title2': 'Katinų veislės'
    }
    return render(request, 'cats/info.html', context=context)


def gallery(request):
    photos = Breeds.objects.all()
    paginator = Paginator(Breeds.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_breeds = paginator.get_page(page_number)
    context = {
        'photos': photos,
        'menu': menu,
        'title': 'Galerija',
        'title2': 'Nuotraukų galerija'
    }

    return render(request, 'cats/gallery.html', context=context)


class BreedsListView(generic.ListView):
    model = Breeds
    paginate_by = 2
    template_name = 'info.html'
