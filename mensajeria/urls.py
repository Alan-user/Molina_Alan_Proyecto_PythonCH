from django.urls import path
from mensajeria import views

app_name = 'mensajeria'

urlpatterns = [
    path('iniciar/', views.iniciar_msj , name='iniciar'),
    path('ver/', views.ver_msj , name='ver'),
    path('ver/detalle/<int:id>/', views.ver_msj_detalle , name='ver_detalle'),
]