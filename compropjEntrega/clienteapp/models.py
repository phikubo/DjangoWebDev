from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Centro_comercial(models.Model):
    nombre_centro = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    def __str__(self):
        return "{0}, {1}".format(self.nombre_centro,self.ciudad)

class Area_local(models.Model):
    inscripcion_cc = models.ForeignKey(Centro_comercial,null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ubicacion=models.PositiveSmallIntegerField()
    coordenadas = models.CharField(max_length=100)
    def __str__(self):
        return "{0}, {1}".format(self.nombre, self.inscripcion_cc)

class Combos_promos(models.Model):
    compros = models.ForeignKey(Area_local,null=True, blank=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100,  default='Mi primer combo')
    descripcion=models.CharField(max_length=100)
    release_date = models.DateField()
    def __str__(self):
        return "{0}, {1}".format(self.nombre, self.compros)
    
'''Una cosa es el nombre, y otra el usuario
Para el caso del usuario es la clave con la que un cc/local se logea.
Para el caso del nombre, es la clave que permite diferenciarlos'''
class Perfil(models.Model):
    user    =   models.OneToOneField(User,on_delete=models.CASCADE)
    eslocal =   models.OneToOneField(Area_local,on_delete=models.CASCADE ,null=True, blank=True)
    escc    =   models.OneToOneField(Centro_comercial,on_delete=models.CASCADE, null=True, blank=True)
    nombre  =   models.CharField(max_length=100 )