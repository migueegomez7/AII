#encoding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re
import os
import django


BOARDGAME_PAGES = 1

def extract_boardgames():
    BASE_URL = 'https://zacatrus.es/'
    link_juegos = set()
    l = []
    for p in range(1,BOARDGAME_PAGES+1):
        f = urllib.request.urlopen(BASE_URL + 'juegos-de-mesa.html/?=' + str(p))
        s = BeautifulSoup(f,"lxml") #lxml is a parser1
        link_juegos.update(s.find("ol", class_="products list items product-items").find_all("li"))
    
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
        print((titulo, precio, tematica, complejidad, num_jugadores, detalles))
        l.append((titulo, precio, tematica, complejidad, num_jugadores,detalles))   
    print("Extraídos {numero} juegos".format(numero=len(l)))
    return l 

def extract_films():
    pass

