from django.contrib import admin
from django.urls import path, include
from setup import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('produtos.urls')),
    path('',include('produtos.urls')),
    path('',include('movimentacao.urls')),
    path('', include('usuarios.urls')),
    path('', include('homepage.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)