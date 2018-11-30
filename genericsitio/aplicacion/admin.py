from django.contrib import admin

# Register your models here.
from .models import pregunta,eleccion
admin.site.register(pregunta)
admin.site.register(eleccion)