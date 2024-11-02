from django.urls import path
from gastos_en_cuotas import views

app_name = 'gastos-en-cuotas'

urlpatterns = [
    path('cuotas/crear/', views.C_G_Cuotas.as_view() , name='crear_g_cuotas'),
    path('cuotas/resumen/', views.VerGCuotas.as_view() , name='resumen_cuotas'),
    path('cuotas/ver/<int:pk>/', views.VerDetalle.as_view() , name='ver_cuotas'),
    path('cuotas/editar/<int:pk>/', views.EditarGC.as_view() , name='editar_cuotas'),
    path('cuotas/eliminar/<int:pk>/', views.EliminarGC.as_view() , name='eliminar_cuotas'),
    
]
