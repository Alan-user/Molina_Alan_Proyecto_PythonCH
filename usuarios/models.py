from django.db import models
from django.contrib.auth.models import User

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    años = models.IntegerField(blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    acerca_de_mi = models.CharField(max_length=200, blank=True, null=True)