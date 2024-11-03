from django.urls import path
from inicio.views import (
    inicio, 
    about_me, 
    Tablero_general,
    graficas, 
    tabla_general, 
    ver_flujo, 
    eliminar_flujo, 
    editar_flujo
)
app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about-me/', about_me, name='about_me'),
    path('Tablero-general', Tablero_general, name='tablero_general'),
    path('graficas', graficas, name='graficas'),
    path('tabla-general', tabla_general, name='tabla_general'),
    path('ver-flujo/<int:id>/', ver_flujo, name='ver_flujo'),
    path('eliminar-flujo/<int:id>/', eliminar_flujo, name='eliminar_flujo'),
    path('editar-flujo/<int:id>/', editar_flujo, name='editar_flujo'),
]
