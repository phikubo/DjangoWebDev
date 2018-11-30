from django.urls import path

from . import views

app_name='cuent'
urlpatterns = [
    path('login/', views.entrar_views,name='entrar_views'),
]  