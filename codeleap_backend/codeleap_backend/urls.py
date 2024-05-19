# codeleap_backend/codeleap_backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('careers.urls')),  # inclua as URLs do aplicativo careers
]
