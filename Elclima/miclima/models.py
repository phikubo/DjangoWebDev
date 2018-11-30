from django.db import models

# Create your models here.

'''Ahora vamos a crear la base de datos para guardar el nombre de las ciudades y luego
consultarlas'''

class Ciudades(models.Model):
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return self.nombre
    class meta:
        verbose_name_plural= 'cities'

'''Luego de crear la tabla anterior hacemos migraciones para guardar los cambios en la base.
Primero makemigrations y luego migrate'''