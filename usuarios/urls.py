from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path("perfi/", views.perfil, name="perfil"),
    path('perfil/editar/contraseña', views.CambiarPass.as_view(), name='mod_pass'),
]
