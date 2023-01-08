#encoding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re
import os, os.path
import django
from datetime import datetime
from whoosh.index import create_in,open_dir
from whoosh.fields import Schema, TEXT, KEYWORD, DATETIME, ID, STORED
from whoosh.qparser import QueryParser
from whoosh import query, index


BOARDGAME_PAGES = 20
FILM_PAGES = 20

def extract_boardgames():
    BASE_URL = 'https://zacatrus.es/'
    link_juegos = set()
    l = []
    for p in range(1,BOARDGAME_PAGES+1):
        f = urllib.request.urlopen(BASE_URL + 'juegos-de-mesa.html/?p=' + str(p))
        s = BeautifulSoup(f,"lxml") #lxml is a parser1
        link_juegos = s.find("ol", class_="products list items product-items").find_all("li")
    
        for juego in link_juegos:
            titulo = "Sin título"
            titulo_temp = juego.find("a", class_="product-item-link")
            if(titulo_temp):
                titulo = str(titulo_temp.string).strip()
            print("Leyendo juego: ", titulo)

            precio = 0.0
            precio_temp = juego.find("span", class_="price")
            if(precio_temp):
                precio = float(precio_temp.string[0:-2].replace(',','.'))
            pagina_juego = urllib.request.urlopen(juego.a["href"])
            bsJuego = BeautifulSoup(pagina_juego, "lxml")
            complejidad = "Desconocida"
            if(bsJuego.find("div", class_="col label", string="Complejidad")):
                complejidad = bsJuego.find("div", class_="col label", string="Complejidad").find_next_sibling("div").string

            tematica = "Desconocida"
            if(bsJuego.find("div", class_="col label", string="Temática")):
                tematica = bsJuego.find("div", class_="col label", string="Temática").find_next_sibling("div").string

            num_jugadores = "Desconocido"
            if(bsJuego.find("div", string="Núm. jugadores")):
                num_jugadores = bsJuego.find("div", string="Núm. jugadores").find_next_sibling("div").string
            
            detalles = ""
            if(bsJuego.find("div", class_= "data item content")):
                for parrafo in bsJuego.find("div", class_= "data item content").find_all("p"):
                    detalles+=str(parrafo.text)
            else:
                detalles = "Sin detalles"
            descripcion = ""
            if(bsJuego.find("div", class_= "product attribute description")):
                descripcion = bsJuego.find("div", class_= "product attribute description").get_text()
            print((titulo, precio, tematica, complejidad, num_jugadores, detalles, descripcion))
            l.append((titulo, precio, tematica, complejidad, num_jugadores,detalles, descripcion))
    print("Extraídos {numero} juegos".format(numero=len(l)))
    return l 

def extract_films():    
    l = []
    re_fecha = re.compile('^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$')
    for p in range(1,FILM_PAGES+1): 
        f = urllib.request.urlopen("https://www.elseptimoarte.net/estrenos/" + str(p))
        s = BeautifulSoup(f, "lxml")
        lista_link_peliculas = s.find("ul", class_="elements").find_all("li")
        for link_pelicula in lista_link_peliculas:
            f = urllib.request.urlopen("https://www.elseptimoarte.net"+ urllib.parse.quote(link_pelicula.a['href']))
            s = BeautifulSoup(f, "lxml")
            datos = s.find("main", class_="informativo").find("section",class_="highlight").div.dl
            titulo = datos.find("dd").string.strip()
            print("Leyendo pelicula: ", titulo)
            generos_director = s.find("div",id="datos_pelicula")
            director = "".join(generos_director.find("p",class_="director").stripped_strings)        
            sinopsis = s.find("div",class_="info").get_text()
            if re_fecha.match(datos.find_all("dd")[3].string.strip()) is not None:
                fecha = datetime.strptime(datos.find_all("dd")[3].string.strip(), '%d/%m/%Y')
            if(datos.find_all("dt")[2].string.strip() == "País"):
                pais = datos.find_all("dt")[2].find_next_sibling("dd").a.string.strip()
            generos = "".join(generos_director.find("p",class_="categorias").stripped_strings)
            print((titulo, director, fecha, pais, generos, sinopsis))
            l.append((titulo,director,fecha,pais,generos,sinopsis))
    print("Extraídas {numero} películas.".format(numero=len(l)))
    return l