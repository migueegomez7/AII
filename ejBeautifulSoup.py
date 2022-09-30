from tkinter import messagebox
from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
from sqlite3 import *
import re
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

#Al debuguear beautifulSoup, entrar en contents que es donde está el contenido de los hijos
def extraer_jornadas():
    url = "https://resultados.as.com/resultados/futbol/primera/2020_2021/calendario/"
    f = urllib.request.urlopen(url)
    s = BeautifulSoup(f,"lxml") #lxml is a parser
    l = s.find_all("div", class_= ["cont-modulo","resultados"])
    return l

def almacenar():
    con = connect("ejtkinter.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS partidos")
    cur.execute("CREATE TABLE partidos(ID INTEGER PRIMARY KEY AUTOINCREMENT, JORNADA TEXT NOT NULL, EQUIPO_LOCAL TEXT NOT NULL, EQUIPO_VISITANTE TEXT NOT NULL, GOLES_L INTEGER NOT NULL,GOLES_V INTEGER NOT NULL,LINK TEXT NOT NULL)")
    
    
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='partidos'")
    if res.fetchone() is not None:
        messagebox.showinfo("Successful Creation","BD creada correctamente")


def listar():
    return "a"

def printea(l):
    for i in range(len(l)):
        print("------------- 1 ------- ")
        print("")
        print(l[i])

def populate(l):
    return "a"

def ventana_principal():
    top = Tk()
    top.geometry("300x300")
    b1 =  Button ( top, text = "Almacenar", relief = RAISED, command = almacenar)
    b2 =  Button ( top, text = "Listar", relief = RAISED, command = listar)
    b1.pack(side = TOP)
    b2.pack(side = TOP)
    l = extraer_jornadas()
    printea(l)
    top.mainloop()

if __name__ == "__main__":
    ventana_principal()