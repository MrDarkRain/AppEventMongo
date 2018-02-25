from django.urls import path
from django.conf.urls import url

from app.eventos.views import index_eventos,validar,mostrarinfo

app_name = 'eventos'


urlpatterns = [
    path('index/', index_eventos),
    url(r'^validar/',validar, name='validar'),
    url(r'^mostrarinfo/',mostrarinfo, name='mostrarinfo'),


]
