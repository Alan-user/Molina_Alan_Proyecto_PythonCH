from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioDeCreacionDeUsuario, FormularioEdicionPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from usuarios.models import DatosExtra
from django.urls import reverse_lazy

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            django_login(request,usuario)
            
            DatosExtra.objects.get_or_create(user=usuario)
            
            return redirect('inicio:inicio')
        
    return render(request, 'usuarios/login.html', {'form': formulario})

def register(request):
    formulario = FormularioDeCreacionDeUsuario()
    
    if request.method == 'POST':
        formulario = FormularioDeCreacionDeUsuario(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('usuarios:login')
    return render(request, 'usuarios/register.html', {'form': formulario})

@login_required
def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    formulario = FormularioEdicionPerfil(instance=request.user, 
                                         initial= {'avatar': datos_extra.avatar,
                                                   'años':datos_extra.años,
                                                   'fecha_de_nacimiento': datos_extra.fecha_de_nacimiento,
                                                   'acerca_de_mi': datos_extra.acerca_de_mi
                                         })
    
    if request.method =='POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            new_avatar = formulario.cleaned_data.get('avatar')
            
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar
            datos_extra.años = formulario.cleaned_data.get('años')
            datos_extra.fecha_de_nacimiento = formulario.cleaned_data.get('fecha_de_nacimiento')
            datos_extra.acerca_de_mi = formulario.cleaned_data.get('acerca_de_mi')

            datos_extra.save()
            
            formulario.save()
            
            return redirect('usuarios:perfil')
    
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})

class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name= 'usuarios/mod_password.html'
    success_url=reverse_lazy('usuarios:editar_perfil')

@login_required
def perfil(request):
    datos_extra = request.user.datosextra
    return render(request, 'usuarios/perfil.html', {'user': request.user, 'datos_extra': datos_extra})
