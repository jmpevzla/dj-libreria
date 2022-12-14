from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 100, verbose_name = 'Titulo')
    imagen = models.ImageField(upload_to = 'media/', null = True, verbose_name = 'Imagen')
    descripcion = models.TextField(null = True, verbose_name = 'Descripción')

    def __str__(self) -> str:
        return self.titulo

    def save(self):
        if self.id:
            previous = Libro.objects.get(id = self.id).imagen
            if self.imagen != previous: 
                self.imagen.storage.delete(previous.name)
        return super().save()

    def delete(self, using = None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        return super().delete()