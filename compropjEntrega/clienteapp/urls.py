from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
#from clienteapp.views import about_view #para las clases
from clienteapp.views import RegistroView, user_view, cc_view, Compro_View

app_name='users_path'
urlpatterns = [
    path('',            views.landing_view,     name='landing_view'),
    #path('login/',      views.login_view,       name='login_view'),
    path('login/', auth_views.LoginView.as_view(template_name='clienteapp/login.html'), name='login'),
    #path('registro/',   views.registro_view,    name='registro_view'),
    path('registrar/',RegistroView.as_view(), name='registro_view'),
    #path('about/',    about_view.as_view(), name='about'),
    path('centrocomercial/', cc_view.as_view(), name='cc_view'),
    path('user/<int:pk>', user_view.as_view(), name='user_view'),
    #path('localadmin/',admin_view.as_view(), name='ladmin_view'),
    path('localadmin/',Compro_View.as_view(), name='compro_view'),
]
