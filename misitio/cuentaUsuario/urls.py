from django.urls import path 
from . import views

app_name='cuentaU'
urlpatterns = [
    #http://127.0.0.1:8000/djangoCuenta/login/
    path('', views.index, name='index'),

    #http://127.0.0.1:8000/index/registrar/
    path('registrar', views.register, name='registrar'),
]