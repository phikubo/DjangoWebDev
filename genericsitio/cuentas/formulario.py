from django import forms
from django.db import models
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model,login,logout
from django.contrib.auth.models import User

User=get_user_model()

class UsuarioLoginForm(forms.Form):
    print("usuarioLoginform")
    NombreUsuario= forms.CharField(max_length=100)
    Contrasena= forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        print("clean")
        try:
            usuario=self.cleaned_data.get("NombreUsuario")
            contrasena=self.cleaned_data.get("Contrasena")
        except:
            print("Exc")
        if usuario and contrasena:
            isUser=authenticate(username=usuario,password=contrasena)
            print("entro")
            if not isUser:
                print(1)
                raise forms.ValidationError("No existe el usuario")
            if not isUser.check_password(contrasena):
                print(2)
                raise forms.ValidationError("Clave incorrecta")
            if not isUser.is_active:
                print(3)
                raise forms.ValidationError("No esta activo")
        return super(UsuarioLoginForm,self).clean(*args,**kwargs)


#En caso de crear formularios.py debo hacer lo siguiente:
'''
En views.py debo cambiar el import actual por:
    from . formularios import UsuarioLoginForm
    Y eso es basicamente v:
'''

#Para hacer funcionar los css con las direcciones:
'''
Hay que encontrar el archivo que carga por ejemplo los fonts. Cuando lo encuentre debo revisar
que los archivos que llama esten en la carpeta donde esta el css y en el css cambio la direccion
de los fonts que se llaman, se repite el proceso para todos las cosas que muestren error en la consola.
'''