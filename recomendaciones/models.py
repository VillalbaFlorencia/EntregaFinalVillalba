from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone


class Series(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    netflix = models.BooleanField()
    descripcion = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)  
    
    def __str__(self):
        return f'{self.nombre}, {self.categoria}'
 
 
class Peliculas(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    netflix = models.BooleanField()
    descripcion = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.nombre}, {self.categoria}'

        
