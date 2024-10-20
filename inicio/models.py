from django.db import models

class Flujo_dinero(models.Model):
    
    tipo_de_flujo = models.CharField(max_length=15)
    fecha = models.DateField()    
    importe = models.FloatField()
    tipo = models.CharField(max_length=15)
    concepto = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.id} {self.tipo_de_flujo} {self.fecha} {self.importe} {self.tipo} {self.concepto}'
