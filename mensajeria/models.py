from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    fecha = models.DateField()    
    cuerpo = models.CharField(max_length=500)
    asunto = models.CharField(max_length=100)
    
    def __str__(self):
        return ( 
                f'{self.id} {self.destinatario} {self.remitente}' 
                f'{self.fecha} {self.cuerpo} {self.asunto} '
        )

