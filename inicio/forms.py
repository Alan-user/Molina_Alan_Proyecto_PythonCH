from django import forms
from django.core.exceptions import ValidationError
from datetime import date


class CrearFlujoForm(forms.Form):
    TIPO_MOVIMIENTO_CHOICES = [
        ('ingresos', 'Ingresos'),
        ('egresos', 'Egresos'),
    ]
    
    TIPO_GASTO_CHOICES = [
        ('', 'Seleccione una opción'),
        ('Pago de Haberes', 'Pago de Haberes'),
        ('Servicio', 'Servicio'),
        ('Gasto Puntual', 'Gasto Puntual'),
        ('Membresía', 'Membresía'),
        ('Seguros', 'Seguros'),
        ('Otros', 'Otros')
    ]
    
    tipo_de_flujo = forms.ChoiceField(choices=TIPO_MOVIMIENTO_CHOICES, 
        widget=forms.RadioSelect,
        label='Tipo de Flujo', required=True)
    fecha = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'DD-MM-YYYY'}),
                            label='Fecha', required=True)
    importe = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': '$$$$$'}),
        label='Importe', required=True)
    tipo = forms.ChoiceField(choices=TIPO_GASTO_CHOICES, label='Tipo de Gasto', required=True)
    concepto = forms.CharField(max_length=20, label='Concepto', required=True)

class BuscarFlujoForm(forms.Form):
    TIPO_MOVIMIENTO_CHOICES = [
        ('', 'Todo'),
        ('ingresos', 'Ingresos'),
        ('egresos', 'Egresos'),
    ]
    
    TIPO_GASTO_CHOICES = [
        ('', 'Todo'),
        ('Servicio', 'Servicio'),
        ('Gasto Puntual', 'Gasto Puntual'),
        ('Membresía', 'Membresía'),
        ('Seguros', 'Seguros'),
    ]
    
    concepto = forms.CharField(max_length=20, label='Concepto', required=False)
    tipo = forms.ChoiceField(choices=TIPO_GASTO_CHOICES, required=False, label='Tipo de Gasto')
    tipo_de_flujo = forms.ChoiceField(choices=TIPO_MOVIMIENTO_CHOICES, required=False, label='Tipo de Movimiento') 