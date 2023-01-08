import os
import random
import shutil
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD
from whoosh.index import open_dir
from whoosh import qparser
import scrap

def films_index():
    
    film_schema = Schema(title = TEXT(stored=True), genres = KEYWORD(stored=True,commas=True), sinopsis = TEXT(stored=True,phrase=False))

    ix_film = index.create_in("indexdir",schema = film_schema,indexname="films") #Calling index.create_in on a directory with an existing index will clear the current contents of the index.
    writer = ix_film.writer()
    
    i = 0
    films = scrap.extract_films()
    for film in films:
        writer.add_document(title = film[0], genres = film[4], sinopsis = film[5])
        i+=1
    writer.commit()
    print("Fin de indexado. Se han indexado " + str(i) + " películas.")
    
    
def get_films(user_search):
    ix = open_dir("indexdir",indexname="films")
    scope  = []
    with ix.searcher() as searcher:
        qp = qparser.MultifieldParser(["title","genres","sinopsis"],ix.schema).parse(user_search)
        results = searcher.search(qp)
        for r in results:
            print(r['title'])
            scope.append(r)
    return scope

def boardgames_index():
    boardgame_schema = Schema(title = TEXT(stored=True), description = TEXT(stored=True,phrase=False))

    ix_boardgame = index.create_in("indexdir",schema = boardgame_schema,indexname="boardgames")
    writer = ix_boardgame.writer()
    
    i = 0
    boardgames = scrap.extract_boardgames()
    for boardgame in boardgames:
        writer.add_document(title = boardgame[0], description = boardgame[5])
        i+=1
    writer.commit()
    print("Fin de indexado. Se han indexado " + str(i) + " juegos de mesa.")
    
def get_boardgames(user_search):
    ix = open_dir("indexdir",indexname="boardgames")
    scope  = []
    with ix.searcher() as searcher:
        qp = qparser.MultifieldParser(["title","description"],ix.schema).parse(user_search)
        results = searcher.search(qp)
        for r in results:
            print(r['title'])#Si se elimina este print, da el fallo whoosh.reading.readerclosed
            scope.append(r)
    return scope