from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearFlujoForm, BuscarFlujoForm
from .forms import EditarFlujoForm
from .models import Flujo_dinero
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    # Inicializa el formulario vacío
    formulario = CrearFlujoForm()

    if request.method == 'POST':
        formulario = CrearFlujoForm(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data
            flujo = Flujo_dinero(
                tipo_de_flujo=data.get('tipo_de_flujo'),
                fecha=data.get('fecha'),
                importe=data.get('importe'),
                tipo=data.get('tipo'),
                concepto=data.get('concepto'),
                comprobante=data.get('comprobante')
            )
            flujo.save()

        # Reinicia el formulario después de guardar
        formulario = CrearFlujoForm()

    return render(request, 'inicio/index.html', {'form': formulario})

def about_me(request):
    return render(request, 'inicio/about_me.html')

@login_required
def Tablero_general(request):
    return render(request, 'inicio/Tablero_general.html')

@login_required
def graficas(request):
    return render(request, 'inicio/graficas.html')

@login_required
def tabla_general(request): 
    formulario = BuscarFlujoForm(request.GET)
    flujos = Flujo_dinero.objects.all()
    
    if formulario.is_valid():
        tipo = formulario.cleaned_data.get('tipo')
        tipo_de_flujo = formulario.cleaned_data.get('tipo_de_flujo')
        
        if tipo:
            flujos = flujos.filter(tipo__icontains=tipo)  # Filtrando por el campo 'tipo'
        if tipo_de_flujo:
            flujos = flujos.filter(tipo_de_flujo=tipo_de_flujo)  # Filtrando por 'tipo_de_flujo'
        
        formulario = BuscarFlujoForm()  # Reinicia el formulario después de la búsqueda

    return render(request, 'inicio/tabla_general.html', {'flujos': flujos, 'form': formulario})

@login_required
def ver_flujo(request,id):
    flujo = Flujo_dinero.objects.get(id=id)
    return render(request, 'inicio/ver_flujo.html', {'flujo': flujo})

@login_required
def eliminar_flujo(request, id):
    flujo = get_object_or_404(Flujo_dinero, id=id)
    
    if request.method == 'POST':
        flujo.delete()
        return redirect('inicio:tabla_general')  # Redirigir después de eliminar

    return render(request, 'inicio/eliminar_flujo.html', {'flujo': flujo})

@login_required
def editar_flujo(request, id):
    flujo = get_object_or_404(Flujo_dinero, id=id)
    
    if request.method == "POST":
        formulario = EditarFlujoForm(request.POST, initial={
            'tipo_de_flujo': flujo.tipo_de_flujo,
            'fecha': flujo.fecha,
            'importe': flujo.importe,
            'tipo': flujo.tipo,
            'concepto': flujo.concepto,
        })
        
        if formulario.is_valid():
            flujo.tipo_de_flujo = formulario.cleaned_data.get('tipo_de_flujo', flujo.tipo_de_flujo)
            flujo.fecha = formulario.cleaned_data.get('fecha', flujo.fecha)
            flujo.importe = formulario.cleaned_data.get('importe', flujo.importe)
            flujo.tipo = formulario.cleaned_data.get('tipo', flujo.tipo)
            flujo.concepto = formulario.cleaned_data.get('concepto', flujo.concepto)
            
            flujo.save()
            return redirect('inicio:tabla_general')
    else:
        formulario = EditarFlujoForm(initial={
            'tipo_de_flujo': flujo.tipo_de_flujo,
            'fecha': flujo.fecha,
            'importe': flujo.importe,
            'tipo': flujo.tipo,
            'concepto': flujo.concepto,
        })
    
    return render(request, 'inicio/editar_flujo.html', {'flujo': flujo, 'form': formulario})
