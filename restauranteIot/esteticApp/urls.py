from django.urls import path, include

from . import views

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    #path('registro/', views.registro, name='registro'),
    #path('sesion/', views.sesion, name='sesion'),
    #path('gestionar/', views.gestionar, name='gestionar'),


]
