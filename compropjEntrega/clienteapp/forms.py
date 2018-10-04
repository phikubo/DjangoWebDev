from django import forms
from django.contrib.auth.models import User #para registrar usuarios.
from django.forms import ModelForm, TextInput, NumberInput, ChoiceField, Textarea, Select, FileInput
from .models import Combos_promos, Area_local
class registrar_usuario_form(forms.Form):
    usuario =   forms.CharField(widget=forms.TextInput(attrs={'class':'input100'}))
    correo  =   forms.EmailField(widget=forms.TextInput(attrs={'class':'input100'}))
    password_1  =  forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False,attrs={'class':'input100'}))
    password_2  =  forms.CharField(label='Confirmar Password',widget=forms.PasswordInput(render_value=False,attrs={'class':'input100'}))
    
class registrar_compro_form(forms.Form):
    #adscrito =forms.ForeingKey()
    adscrito = forms.ModelChoiceField(queryset=Area_local.objects.all()) #aqui se hace un filtro.
    nombre =   forms.CharField(widget=forms.TextInput(attrs={'class':'input100' ,'placeholder':'Un título genial!'}))
    descripcion =forms.CharField(widget=forms.TextInput(attrs={'class':'textarea','placeholder':'Descripción'}))
    #foto=forms.ImageField()
        