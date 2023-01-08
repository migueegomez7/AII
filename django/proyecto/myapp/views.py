from django.shortcuts import render
from django.http import HttpResponse
import whooshcode
from .models import *
import populateDB
#This class is a Request Handler, it is like a controller. It does not contain views nor html code nor templates.
def index(request):
    peliculas_almacenadas = Film.objects.all()
    modelmap = {'peliculas': peliculas_almacenadas}
    return render(request, 'index.html', modelmap)


def populateDatabase(request):
    #(f,b) = populateDB.populate()
    #informacion="Datos cargados correctamente\n" + "Juegos de mesa: " + str(b)  + "\n Peliculas: " + str(f)
    informacion = "a"
    return render(request, 'carga.html', {'inf':informacion})

def seleccion(request):
    user_search = request.POST.get("tema")
    print(user_search)
    films = whooshcode.get_films(user_search)
    boardgames = whooshcode.get_boardgames(user_search)
    return render(request,'seleccion.html',{'films':films, 'boardgames':boardgames})
    
def indice(request):
    #whooshcode.films_index()
    #whooshcode.boardgames_index()
    return render(request,'indice.html')