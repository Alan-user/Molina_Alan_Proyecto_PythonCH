from django.db import models
class PagoEnCuotas(models.Model):
    
    BANCOS= [
        ('Santander', 'Santander' ),
        ('Galicia', 'Galicia' ),
        ('BBVA', 'BBVA' ),
        ('Macro', 'Macro' ),
        ('Superville', 'Superville' ),
        ]
    
    CANT_CUOTAS= [
        (1, 1),
        (3, 3),
        (6, 6),
        (12, 12),
        (18, 18),
        (24, 24),
        ]
    cantidad_cuotas = models.IntegerField(choices=CANT_CUOTAS)
    banco = models.CharField(max_length=10, choices=BANCOS)
    importe = models.FloatField()
    fecha = models.DateField()
    concepto = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.id} {self.importe} {self.banco} {self.fecha}'
