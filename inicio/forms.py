from django import forms

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
    fecha = forms.DateField(label='Fecha', widget=forms.DateInput(attrs={'type': 'date'}),
                            required=True)
    importe = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': '$$$$$'}),
        label='Importe', required=True)
    tipo = forms.ChoiceField(choices=TIPO_GASTO_CHOICES, label='Tipo de Gasto', required=True)
    concepto = forms.CharField(max_length=20, label='Concepto', required=True)
    comprobante = forms.ImageField(required=False)

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
    
    tipo = forms.ChoiceField(choices=TIPO_GASTO_CHOICES, required=False, label='Tipo de Gasto')
    tipo_de_flujo = forms.ChoiceField(choices=TIPO_MOVIMIENTO_CHOICES, required=False, label='Tipo de Movimiento') 
    
class EditarFlujoForm(CrearFlujoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    