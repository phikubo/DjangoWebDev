from django.contrib import admin
from miapp.models import Centro_comercial, Area_local, Combos_promos
from miapp.models import admincc, Perfil
# Register your models here.
admin.site.register(Centro_comercial)
admin.site.register(Area_local)
admin.site.register(Combos_promos)
admin.site.register(admincc)
admin.site.register(Perfil)
