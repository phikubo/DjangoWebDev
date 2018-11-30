from django.contrib import admin

# Register your models here.
from .models import pregunta
from .models import eleccion

admin.site.register(pregunta)
admin.site.register(eleccion)