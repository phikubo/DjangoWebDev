from django.shortcuts import render
#from .forms import registrar_usuario_form, registrar_compro_form   #para registrar users 1 y compros
from django.views.generic import FormView   #para registrar users 2
# Create your views here.
def landing_view(request):
    return render(request,'miapp/index.html')

class Contactenos(FormView):
    
    pass
