from django.conf.urls.static import static
from breeds import settings
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from cats.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cats.urls')),
    # path('', include('gallery.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
