from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import registrar_usuario_form, registrar_compro_form   #para registrar users 1 y compros
from django.views.generic import FormView   #para registrar users 2
from django.contrib.auth.models import User #para registrar users 3
from django.views.generic.base import TemplateView #para ver templates con contexto

#para usar el decorador
from django.contrib.auth.decorators import login_required

#para la fecha
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect

from .models import *

# Create your views here.
def landing_view(request):
    return render(request,'clienteapp/landing.html')

def login_view(request):
    return render(request,'clienteapp/login.html')

def logout(request):
    pass

def registro_view(request):
    return render(request, 'clienteapp/registro.html')

#/centrocomercial/
#estado:90%
class cc_view(TemplateView):
    template_name = "clienteapp/cc_view.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['ccs']=Centro_comercial.objects.all()
        context['locales']=Area_local.objects.all()
        print(context)
        return context
    
    '''cc debe ver todos los locales registrados y debe poder agregar locales'''
    #formview

#/user/pk=pk
#estado:60%
'''Revela la informacion de un centro comercial en especifico'''
class user_view(TemplateView):
    template_name = "clienteapp/user_view.html"
    def get_context_data(self, pk, **kwargs):
        context=super().get_context_data(**kwargs)
        context['identificacion']=Centro_comercial.objects.get(id=pk) 
        print(context)
        return context
    #templateview
    '''user view debe solo poder ver los centros comerciales y puede filtrar por nombre y ciudad*proximamente'''

''' El centro comercial puede registrar con RegistrarView a los centros comerciales
Los centros comerciales son registrados por el administrador de la aplicacion, de tal modo,
tanto el centro comercial puede loguearse para registrar, como los locales para registrar sus combos.'''
#no impleentada
class cc_admin_view(FormView):
    template_name = "clienteapp/local_admin_view.html"
    form_class = registrar_compro_form
    success_url = '/localadmin/'
    
    def form_valid(self, form):
        elcompro=Combos_promos(adscrito=self.request.POST['usuario'], nombre=self.request.POST['correo'], password=self.request.POST['password_1'])
        elcompro.save()
        return super().form_valid(form)
    
    '''Admin view puede agregar promociones, segun su tarifa*proximamente puede publicar todos o una.'''
    #formview
    def get_context_data(self, pk, **kwargs):
        context=super().get_context_data(**kwargs)
        context['compros']=Combos_promos.objects.all() 
        print(context)
        return context


#localadmin/
'''
Revela todas las promociones'''

class Compro_View(FormView):
    template_name = 'clienteapp/local_admin_view.html'
    form_class = registrar_compro_form
    success_url="/"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['compros']=Combos_promos.objects.all()
        print("Has llegado a compro view a context_data")
        print(context)
        print("-------------------------------------") 
        
        return context

    def form_valid(self, form):
        print("Has llegado a form valid")

        a=Area_local.objects.get(id=self.request.POST['adscrito'])
        print(a,type(self.request.POST['adscrito']))
        compro=Combos_promos(compros=a, nombre=self.request.POST['nombre'], descripcion=self.request.POST['descripcion'], release_date=datetime.now())
        print("Has llegado a compro view a form_valid")
        print(compro.compros, compro.nombre, compro.descripcion, compro.release_date)
        compro.save()
        return super().form_valid(form)

#completado 90%
#/registrar/

class RegistroView(FormView):
    
    template_name = 'clienteapp/registro.html'
    form_class = registrar_usuario_form
    success_url = '/'
    def form_valid(self, form):
        usr=User.objects.create_user(username=self.request.POST['usuario'], email=self.request.POST['correo'], password=self.request.POST['password_1'])
        usr.save()
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super().form_valid(form)