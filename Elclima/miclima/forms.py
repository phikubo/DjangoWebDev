from django.forms import ModelForm, TextInput
from .models import Ciudades

class CiudadForm(ModelForm):
    """Form definition for Ciudad."""

    class Meta:
        """Meta definition for Ciudadform."""

        model = Ciudades
        #fields = ('',)
        fields= ['nombre']
        widgets = {'nombre': TextInput(attrs={'class':'input','placeholder':'Nombre de la Ciudad'})}
