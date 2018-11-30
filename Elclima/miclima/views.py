from django.shortcuts import render
import requests
from .models import Ciudades
from .forms import CiudadForm

# Create your views here.
def index(request):
    urltotal='http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=07695c8107665f493a4d71a7ea7d310b'
    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=07695c8107665f493a4d71a7ea7d310b'
    
    
    '''Primera aproximacion:
    ciudad='bogota' 
    #r=requests.get(url.format(ciudad)) ->todo el formato json
    r=requests.get(url.format(ciudad)).json()
    #print(r.text) ->Imprime datos si esta correcto, y los nombres del siguiente diccionario
    clima_ciudad = {
        'ciudad':ciudad,
        'temperatura':r['main']['temp'],
        'descripcion':r['weather'][0]['description'],
        'icono':r['weather'][0]['icon'],
    }
    #print(clima_ciudad) ->los datos que queremos sacar
    context={'clima_ciudad2':clima_ciudad}
    #clima_ciudad2 es el nombre de la variable que se usa en el html.
    #mientras que clima_ciudad es el nombre de la variable que se reconoce aqui en views, en python
    return render(request, 'miclima/weather.html', context)
    
    '''
    if request.method == 'POST':
        print(request.POST)
        form = CiudadForm(request.POST)
        form.save()

    
    forma=CiudadForm()


    ciudades = Ciudades.objects.all()
    datos_ciudades = []
    for ciudad in ciudades:
        r=requests.get(url.format(ciudad.nombre)).json()
        clima_ciudad = {
        'ciudad':ciudad.nombre,
        'temperatura':r['main']['temp'],
        'descripcion':r['weather'][0]['description'],
        'icono':r['weather'][0]['icon'], 
        }
        datos_ciudades.append(clima_ciudad) #Por cada objeto de ciudades, hace el request, 
        #con el nombre de la ciudad
    #print(datos_ciudades)
    context={'clima_datos':datos_ciudades, 'form':forma }
    return render(request, 'miclima/weather.html', context)
    #return render(request, 'direccionTemplate')