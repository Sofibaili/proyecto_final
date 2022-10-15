from django.shortcuts import render
from AppPower.models import Familiar

# Create your views here.

def index(request):
    return render(request, "AppPower/saludar.html",
     {
     'nombre':'Sofia',
     'apellido': 'Baili'

     })


def index_dos(request, nombre, apellido):
    return render(request, "AppPower/saludar.html",
     {
     'nombre': nombre,
     'apellido': apellido,
      })

def index_tres(request):
    return render(request, "AppPower/saludar.html",
     {
     'notas': [1, 2, 3, 4, 5, 6, 7, 8]
     })


def imc(request):
    imc = (60/1.6) #calcular el imc
    return render(request, 'AppPower/imc.html', {'imc': imc})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "AppPower/familiares.html", {"lista_familiares": lista_familiares})
  