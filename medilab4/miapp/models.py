from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Centro_comercial(models.Model):
    nombre_centro = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre_centro

class Area_local(models.Model):
    locales = models.ForeignKey(Centro_comercial,null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ubicacion=models.PositiveSmallIntegerField()
    def __str__(self):
        return "{0}, {1}".format(self.nombre, self.locales)

class Combos_promos(models.Model):
    compros = models.ForeignKey(Area_local,null=True, blank=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100,  default='Mi primer combo')
    descripcion=models.CharField(max_length=100)
    release_date = models.DateField()
    def __str__(self):
        return "{0}, {1}".format(self.nombre, self.compros)
    
class admincc(models.Model):
    nombre=models.CharField(max_length=100,  default='BigBoss')
    locales = models.ForeignKey(Area_local, null=True, blank=True,on_delete=models.CASCADE)
    ccs = models.OneToOneField(Centro_comercial, null=True, blank=True,on_delete=models.CASCADE)
    compros = models.ForeignKey(Combos_promos,null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}".format(self.nombre)

class Perfil(models.Model):
    user    =   models.OneToOneField(User,on_delete=models.CASCADE)
    eslocal =   models.OneToOneField(Area_local,on_delete=models.CASCADE ,null=True, blank=True)
    escc    =   models.OneToOneField(Centro_comercial,on_delete=models.CASCADE, null=True, blank=True)
    nombre  =   models.CharField(max_length=100 )

class Contactenos(models.Model):
    compros = models.ForeignKey(Area_local,null=True, blank=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100,  default='Mi primer combo')
    descripcion=models.CharField(max_length=100)
    release_date = models.DateField()
    def __str__(self):
        return "{0}, {1}".format(self.nombre, self.compros)