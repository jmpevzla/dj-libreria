from tabnanny import verbose
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 100, verbose_name = 'Titulo')
    imagen = models.ImageField(upload_to = 'media/', null = True, verbose_name = 'Imagen')
    descripcion = models.TextField(null = True, verbose_name = 'Descripcion')