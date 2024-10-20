from django.shortcuts import render
from .forms import CrearFlujoForm, BuscarFlujoForm
from .models import Flujo_dinero


def inicio(request):
    # Inicializa el formulario vacío
    formulario = CrearFlujoForm()

    if request.method == 'POST':
        formulario = CrearFlujoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            flujo = Flujo_dinero(
                tipoflujo=data.get('tipo_de_flujo'),
                fecha=data.get('fecha'),
                importe=data.get('importe'),
                concepto=data.get('concepto')
            )
            flujo.save()
        # Reinicia el formulario después de guardar
        formulario = CrearFlujoForm()

    return render(request, 'inicio/index.html', {'form': formulario})

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
    formulario = BuscarFlujoForm(request.GET)
    flujos = Flujo_dinero.objects.all()
    
    if formulario.is_valid():
        concepto = formulario.cleaned_data.get('concepto')
        tipo = formulario.cleaned_data.get('tipo')
        tipo_de_flujo = formulario.cleaned_data.get('tipo_de_flujo')
        
        if concepto:
            flujos = flujos.filter(concepto__icontains=concepto)
        if tipo:
            flujos = flujos.filter(tipo__icontains=tipo)  # Filtrando por el campo 'tipo'
        if tipo_de_flujo:
            flujos = flujos.filter(tipo_de_flujo=tipo_de_flujo)  # Filtrando por 'tipo_de_flujo'
        
        formulario = BuscarFlujoForm()  # Reinicia el formulario después de la búsqueda

    return render(request, 'inicio/tabla_general.html', {'flujos': flujos, 'form': formulario})