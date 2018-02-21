from django.urls import path
from django.conf.urls import url

from app.eventos.views import index_eventos,validar,evento_grafico,mostrarinfo

app_name = 'eventos'


urlpatterns = [
    path('index/', index_eventos),
    #url(r'^juegosbien/', juegosmundialbien, name='juegos_listar'),
    url(r'grafico/', evento_grafico),
    url(r'^validar/',validar, name='validar'),
    url(r'^mostrarinfo/',mostrarinfo, name='mostrarinfo'),


]
