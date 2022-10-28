from django.shortcuts import render
from AppPower.models import Familiar
from AppPower.forms import Buscar, FamiliarForm
from django.views import View 


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
 
class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'AppPower/buscar.html'
    initial = {"nombre":""}

    def get(self, request): #este e sun metodo. Recibo un get en el servidor inicializo un formulario con los valores que defino
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form}) 

    def post(self, request): #este es otro metodo. Recibe la info y s einicializa con los valores que fueron enviados 
        form = self.form_class(request.POST)
        if form.is_valid(): #chequea que no haya mas de 100 caracteres que lo definimos en forms. Si es valido extrago el valor del campo
            nombre = form.cleaned_data.get("nombre")  
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'AppPower/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request): #igual al de buscar, nada mas que va a recibir el formulario de familiar
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial) #hay que incicializarlo de nuevo 
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


