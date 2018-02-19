from django.urls import path
from django.conf.urls import url

from app.eventos.views import index_eventos

app_name = 'eventos'


urlpatterns = [
    path('index/', index_eventos),
    #url(r'^juegosbien/', juegosmundialbien, name='juegos_listar'),   
]