from django import forms
from django.contrib.auth.models import User

class MensajeNuevo(forms.Form):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Destinatario",
        widget=forms.Select(attrs={'class': 'form-control', 'data-live-search': 'true'})
    )
    asunto = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cuerpo = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))