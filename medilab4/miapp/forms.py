from django import forms
from django.forms import ModelForm, TextInput, NumberInput, ChoiceField, Textarea, Select, FileInput
#from .models import Combos_promos, Area_local

class registrar_compro_form(forms.Form):
    #adscrito =forms.ForeingKey()
    pass
    #adscrito = forms.ModelChoiceField(queryset=Area_local.objects.all()) #aqui se hace un filtro.
    #nombre =   forms.CharField(widget=forms.TextInput(attrs={'class':'input100' ,'placeholder':'Un título genial!'}))
    #descripcion =forms.CharField(widget=forms.TextInput(attrs={'class':'textarea','placeholder':'Descripción'}))
    #foto=forms.ImageField()