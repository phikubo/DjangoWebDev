"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include #include creada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('pollss.urls')), #el segundo pollss es el nombre de la carpeta de la aplicacion
    path('index/',include('cuentaUsuario.urls')),
    path('djangoCuenta/',include('django.contrib.auth.urls')),
]

#urls.py: llama en path a pollss.urls. En la app pollss url.py de views de usa la funcion index
#por lo que en total, en la direccion localhost/polls aparece lo que se puso en esa funcion index.

#http://igorsobreira.com/2010/12/11/extending-user-model-in-django.html