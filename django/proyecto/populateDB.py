#encoding:utf-8
from myapp.models import BoardGame,Film
import os
import django
from scrap import extract_boardgames,extract_films



def populate_boardgames():
    
    BoardGame.objects.all().delete()
    res = []
    lista = extract_boardgames()
    i = 1
    for line in lista:
        print(line)
        title = line[0]
        price = float(line[1])
        complexity = line[3]
        print(complexity)
        boardgame = BoardGame(idBoardGame = i, titulo = title, precio = price, complejidad = complexity)
        #boardgame.save()
        print("----------------")
        print(boardgame)
        res.append(boardgame)
        i += 1
    BoardGame.objects.bulk_create(res)
    return len(res)
    

def populate_films():
    Film.objects.all().delete()
    res = []
    lista = extract_films()
    j = 1
    for line in lista:
        film = Film(idFilm = j, titulo = line[0],director = line[1],fecha_estreno = line[2],pais = line[3])
        #film.save()
        print("-----------")
        print(film)
        res.append(film)
        j += 1
    Film.objects.bulk_create(res)
    return len(res)




def populate():
    b = populate_boardgames()
    f = populate_films()
    return (b,f)