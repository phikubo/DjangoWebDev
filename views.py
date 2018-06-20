from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect #agregado por mi
from .models import pregunta, eleccion
from django.template import loader #para usar index.html
from django.http import Http404
from django.urls import reverse

# Create your views here.

#funcion agregada por mi
def index(request):
    listar_ultimas_preguntas = pregunta.objects.order_by('-pub_calendario')[:5]
    salida = ', '.join([q.pregunta_texto for q in listar_ultimas_preguntas])
    return HttpResponse(salida)
    #q es una variable local que se crea a partir de las listar ultimas preguntas.
    
#creada. En urls.py se especifica el nombre de esta funcion como views.index.
def index2(request):
    listar_ultimas_preguntas = pregunta.objects.order_by('-pub_calendario')[:5]
    template = loader.get_template('pollss/index.html')
    contexto = {
        'listar_ultimas_preguntas': listar_ultimas_preguntas,
    }
    return HttpResponse(template.render(contexto, request))

def index3(request):
    listar_ultimas_preguntas = pregunta.objects.order_by('-pub_calendario')[:5]
    contexto = {'listar_ultimas_preguntas': listar_ultimas_preguntas}
    return render(request, 'pollss/index.html', contexto)



def detalles(request,id_pregunta):
    try:
        preguntass = pregunta.objects.get(pk=id_pregunta)
    except pregunta.DoesNotExist:
        raise Http404("La pregunta no existe bitch!")
    #si en lugar de detalles.html hubiera puesto index.html, al no existir
    #la variable listar_ultimas_preguntas, el resultado es 'no polls available'
    return render(request, 'pollss/detalles.html', {'pregunta': preguntass})
def detalles2(request, id_pregunta):
    preguntass=get_object_or_404(pregunta, pk=id_pregunta)
    return render(request, 'pollss/detalles.html',{'pregunta': preguntass})
    #si en lugar de pregunta en el diccionario de render, pongo preguntas, falla.
    #debe llamarse igual que la variable en cuestion.
def detalles3(request, id_pregunta):
    preguntass=get_object_or_404(pregunta, pk=id_pregunta)
    return render(request, 'pollss/detalles.html',{'pregunta': preguntass})

def resultados(request,id_pregunta):
    respuestas=get_object_or_404(pregunta, pk=id_pregunta)
    return render(request, 'pollss/resultados.html', {'pregunta':respuestas})
    #response="Estas mirando resultados: %s"
    #return HttpResponse(response %id_pregunta)

def votar(request, id_pregunta):
    preguntas = get_object_or_404(pregunta, pk=id_pregunta)
    print("id: ", id_pregunta)
    try:
         
        print("holi")
        
        opcion_seleccionada = preguntas.eleccion_set.get(pk=request.POST['elecciones'])
        
    except (KeyError, eleccion.DoesNotExist):
        print(KeyError, eleccion.DoesNotExist)
        print("holi2")
        return render(request, 'pollss/detalles.html',{'pregunta':preguntas,
        'error_message':"No seleccionaste nada bitch!", 
        })
    else:
        print("holi3")
        opcion_seleccionada.votos +=1
        opcion_seleccionada.save()
        return HttpResponseRedirect(reverse('poll:resultados', args=(preguntas.id,)))
        #return HttpResponse("Estas votando: %s" %id_pregunta) 