from django.urls import path
from inicio.views import inicio, about_me, Tablero_general, egresos, ingresos, graficas
from inicio.views import tabla_general

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about-me/', about_me, name='about_me'),
    path('Tablero-general', Tablero_general, name='tablero_general'),
    path('egresos', egresos, name='egresos'),
    path('ingresos', ingresos, name='ingresos'),
    path('graficas', graficas, name='graficas'),
    path('tabla_general', tabla_general, name='tabla_general'),
]
