from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('info/', info, name="info"),
    path('gallery/', views.gallery, name="gallery"),
    path('search/', views.search, name="search"),
]

