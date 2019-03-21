from django.urls import path, include
from . import views
from .models import Contactenos
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

app_name='users_path'
urlpatterns = [
    path('',views.landing_view,     name='landing_view'),
    #path('contactenos/', Contactenos.as_view(), name='contactenos'),
]
