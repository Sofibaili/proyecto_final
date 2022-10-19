from django import forms

class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100) #no me deja poner mas de 100 caracteres en la pagina en la parte de nombre

      