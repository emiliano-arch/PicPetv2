from django import forms
from models import Persona
""" from .models import Post """

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellidoPaterno', 'apellidoMAterno', 'nombreUsuario', 'email', 'edad', 'contrasenia']