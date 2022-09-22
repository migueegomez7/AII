from csv import excel
import urllib.request
import os.path
import re


def abrir_url(url, archivo):
    try:
        urllib.request.urlretrieve(url,archivo)
    except:
        print  ("Error al conectarse a la página")
        return None

def tratar_archivo(archivo):
    f = open (archivo, "r",encoding='utf-8')
    s = f.read()
    l1 = re.findall(r'<title>(.*)</title>\s*<link>(.*)</link>', s)
    l2 = re.findall(r'<pubDate>(.*)</pubDate>', s)
    
    for i in range(0, len(l1)):
        tupla = l1[i]
        l1[i] = tupla[0], tupla[1], formatea_fecha(l2[i])
    return l1

def formatea_fecha(fecha):
    meses = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12",}
    mes = meses[fecha[8:11]]
    dia = fecha[5:7]
    año = fecha[12:16]
    return dia + "/" + mes + "/" +  año
    
    
    
def imprimir_lista(lista):
    for tupla in lista:
      imprimir_tupla(tupla)

def imprimir_tupla(tupla):
        print("Titulo: " + tupla[0])
        print("Link: " + tupla[1])
        print("Fecha: " + tupla[2])
        print("\n")


def busca_noticias_por_dia(lista):
    mes = input("Seleccione un mes 'mm': ")
    dia = input("Seleccion un día 'dd': ")  
    for tupla in lista:
        if mes == tupla[2][3:5] and dia == tupla[2][0:2]:
            imprimir_tupla(tupla)
            

if __name__ == "__main__":
    archivo = "./noticias"
    abrir_url("https://sevilla.abc.es/rss/feeds/Sevilla_Sevilla.xml", archivo)
    lista_tuplas = tratar_archivo(archivo)
    imprimir_lista(lista_tuplas)
    busca_noticias_por_dia(lista_tuplas)

