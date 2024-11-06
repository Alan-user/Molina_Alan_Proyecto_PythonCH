from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from mensajeria.models import Mensaje
from mensajeria.forms import MensajeNuevo
from django.utils import timezone

@login_required
def iniciar_msj(request):
   formulario = MensajeNuevo()
   if request.method == 'POST':
     print("Formulario recibido:", request.POST)
     formulario = MensajeNuevo(request.POST)

     if formulario.is_valid():
         print("Formulario válido, guardando mensaje")
         data = formulario.cleaned_data
         msj = Mensaje(
             remitente=request.user,
             destinatario=data.get('destinatario'),
             fecha=timezone.now().date(),
             asunto=data.get('asunto'),
             cuerpo=data.get('cuerpo')
         )
         msj.save()
         formulario = MensajeNuevo()
         return redirect('mensajeria:ver')
     else:
         print("Errores en el formulario:", formulario.errors)

   return render(request, 'mensajeria/iniciar_msj.html', {'form': formulario})    

@login_required
def ver_msj(request):
    usuario_actual = request.user
    msj = Mensaje.objects.filter(remitente=usuario_actual).union(Mensaje.objects.filter
                (destinatario=usuario_actual)).order_by('-fecha')
    return render(request, 'mensajeria/ver_msj.html', {'msj': msj})

@login_required
def ver_msj_detalle(request, id):
    msj = Mensaje.objects.get(id=id)
    return render(request, 'mensajeria/ver_msj_detalle.html', {'msj': msj})