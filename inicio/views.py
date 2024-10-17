from django.shortcuts import render


def inicio(request):
    return render(request, 'inicio/index.html')

def about_me(request):
    return render(request, 'inicio/about_me.html')

def Tablero_general(request):
    return render(request, 'inicio/Tablero_general.html')

def egresos(request):
    return render(request, 'inicio/egresos.html')

def ingresos(request):
    return render(request, 'inicio/ingresos.html')

def graficas(request):
    return render(request, 'inicio/graficas.html')

def tabla_general(request):
    return render(request, 'inicio/tabla_general.html')