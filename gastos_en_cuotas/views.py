from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from gastos_en_cuotas.models import PagoEnCuotas
from django.urls import reverse_lazy

class C_G_Cuotas(CreateView):
    model = PagoEnCuotas
    template_name = "pago_en_cuotas/crear_pago.html"
    success_url = reverse_lazy('gastos-en-cuotas:crear_g_cuotas')
    fields = ['cantidad_cuotas', 'banco', 'importe', 'fecha', 'concepto']
    
class VerGCuotas(ListView):
    model = PagoEnCuotas
    template_name = 'pago_en_cuotas/resumen_GC.html'
    context_object_name = 'gastos'
    
    
class VerDetalle(DetailView):
    model = PagoEnCuotas
    template_name = 'pago_en_cuotas/ver_pago_gc.html'
    context_object_name = 'detalle'

class EditarGC(UpdateView):
    model = PagoEnCuotas
    template_name = "pago_en_cuotas/editar_pago.html"
    success_url = reverse_lazy('gastos-en-cuotas:resumen_cuotas')
    fields = ['cantidad_cuotas', 'banco', 'importe', 'fecha', 'concepto']
    
class EliminarGC(DeleteView):
    model = PagoEnCuotas
    template_name = "pago_en_cuotas/eliminar_pago.html"
    success_url = reverse_lazy('gastos-en-cuotas:resumen_cuotas')
