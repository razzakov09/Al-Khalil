from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Al_Khalil.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Al_Khalil.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)