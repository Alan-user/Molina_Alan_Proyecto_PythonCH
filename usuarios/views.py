from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioDeCreacionDeUsuario

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')
            
            try_logg = authenticate(username=usuario, password=contraseña)
            
            django_login(request,try_logg)
            
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