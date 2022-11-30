from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import populateDB
#This class is a Request Handler, it is like a controller. It does not contain vies nor html code nor templates.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Migue'})


def index(request):
    return render(request, 'index.html')

def populateDatabase(request):
    (b) = populateDB.populate()
    informacion="Datos cargados correctamente\n" + "Juegos de mesa: " + str(b)
    return render(request, 'carga.html', {'inf':informacion})