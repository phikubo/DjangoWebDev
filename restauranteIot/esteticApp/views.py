from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing(request):
    #retu="Bienvenido a landing"
    #return HttpResponse(retu)
    return render(request, 'esteticApp/landing.html')

def registro(request):
    
    pass

def sesion(request):
    pass

def gestionar(request):
    pass

'''Tareas:
1. Crear los formularios de registro
2. Crear modelo en la base de datos.
3. linkear la base de datos.'''