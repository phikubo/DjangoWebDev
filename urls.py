from django.urls import path 
from . import views

app_name='poll'
urlpatterns = [
    path('', views.index, name='index'),
    #/polls/index2/
    path('index2/', views.index2, name='index2'),
    #/polls/index2/
    path('index3/', views.index3, name='index3'),

    #ex:    /polls/detalles2/4
    path('detalles2/<int:id_pregunta>/',views.detalles2, name="detalles2"),
    #ex:    /polls/detalles2/4
    path('detalles3/<int:id_pregunta>/',views.detalles3, name="detalles3"),
    #ex:    /polls/5/
    path('<int:id_pregunta>/', views.detalles, name='detalles'),
    #ex:    /polls/5/resultados
    path('<int:id_pregunta>/resultados/', views.resultados, name='resultados'),
    #ex:    /polls/5/votar
    path('<int:id_pregunta>/votar/', views.votar, name='votar'),
]

#archivo creado por mi