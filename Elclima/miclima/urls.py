from . import views
from django.urls import path 
app_name='appclima'
urlpatterns = [
    #http://127.0.0.1:8000/djangoCuenta/login/
    path('', views.index, name='index'),
]