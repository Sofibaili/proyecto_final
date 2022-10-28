from django import forms
from AppPower.models import Familiar

class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100) #no me deja poner mas de 100 caracteres en la pagina en la parte de nombre


class FamiliarForm(forms.ModelForm):
  class Meta: #meta sirve para daar caracteristicas especiales a un  modelo o formularios. meta ya existe en model
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte'] #que campos del modelo queremos usar en el formulario 