from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioDeCreacionDeUsuario(UserCreationForm):
    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(label= 'Nombre')
    last_name = forms.CharField(label= 'Apellido')
    email = forms.EmailField(label= 'Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        
class FormularioEdicionPerfil(UserChangeForm):
    email = forms.EmailField(label= 'Email')
    first_name = forms.CharField(label= 'Nombre')
    last_name = forms.CharField(label= 'Apellido')
    password = None
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']