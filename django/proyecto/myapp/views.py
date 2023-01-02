from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import populateDB
#This class is a Request Handler, it is like a controller. It does not contain vies nor html code nor templates.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Migue'})


def index(request):
    peliculas_almacenadas = Film.objects.all()
    modelmap = {'peliculas': peliculas_almacenadas}
    return render(request, 'index.html', modelmap)

def populateDatabase(request):
    (b,f) = populateDB.populate()
    informacion="Datos cargados correctamente\n" + "Juegos de mesa: " + str(b) + "\n Peliculas: " + str(f)
    return render(request, 'carga.html', {'inf':informacion})

def seleccion(request):
    checkbox_values = request.POST.getlist("checks")
    print(checkbox_values)