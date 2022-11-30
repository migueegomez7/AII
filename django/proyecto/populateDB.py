#encoding:utf-8
from myapp.models import BoardGame,Film
import os
import django
from scrap import extract_boardgames,extract_films



def populate_boardgames():
    
    BoardGame.objects.all().delete()
    lista = []
    lista = extract_boardgames()
    i = 1
    return len(lista)
'''    for line in lista:
        title = line[0]
        price = line[1]
        complexity = line[3]
        lista.append(BoardGame(idBoardGame = i,titulo = title, precio = float(price), complejidad = complexity))
        i += 1
        BoardGame.objects.bulk_create(lista)
'''    

def populate_films():
    Film.objects.all().delete()
    lista = []
    lista = extract_films()
    j = 1
    
    return len(lista)

'''
def populatePais():
    Pais.objects.all().delete()
    
    lista=[]
    fileobj=open(path+"\\paises", "r")
    for line in fileobj.readlines():
        rip = str(line.strip()).split('|')
        lista.append(Pais(idPais=int(rip[0].strip()), nombre=str(rip[1].strip())))
    fileobj.close()
    Pais.objects.bulk_create(lista)  # bulk_create hace la carga masiva para acelerar el proceso
    
    return len(lista)
'''


def populate():
    b = populate_boardgames()
    
