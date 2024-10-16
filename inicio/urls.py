from django.urls import path
from inicio.views import inicio, about_me

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about-me/', about_me, name='about_me'),
]
