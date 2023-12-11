from django.contrib import admin
from .models import *


class BreedsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'height', 'lifespan', 'description', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Breeds, BreedsAdmin)


