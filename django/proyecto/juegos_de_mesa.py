from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
from tkinter import messagebox
from sqlite3 import *
from lxml import *
from datetime import datetime
# lineas para evitar error SSL
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


root = Tk()

def commandCargar():
    BASE_URL = 'https://zacatrus.es/'
    f = urllib.request.urlopen(BASE_URL + 'juegos-de-mesa.html')
    s = BeautifulSoup(f,"lxml") #lxml is a parser
    l = []
    link_juegos = s.find("ol", class_="products list items product-items").find_all("li")
    
    for juego in link_juegos:
        titulo = str(juego.find("a", class_="product-item-link").string).strip()
        print("Leyendo juego: ", titulo)
        precio = str(juego.find("span", class_="price").string)
        votos_positivos = ""
        if(juego.find("div", class_="rating-result")):
            votos_positivos = str(juego.find("div", class_="rating-result").span.span.string)
        else:
            votos_positivos = 0

        pagina_juego = urllib.request.urlopen(juego.a["href"])
        bsJuego = BeautifulSoup(pagina_juego, "lxml")
        complejidad = ""
        if(bsJuego.find("div", class_="col label", string="Complejidad")):
            complejidad = bsJuego.find("div", class_="col label", string="Complejidad").find_next_sibling("div").string
        else:
            complejidad = "Desconocido"

        tematica = ""
        if(bsJuego.find("div", class_="col label", string="Temática")):
            tematica = bsJuego.find("div", class_="col label", string="Temática").find_next_sibling("div").string
        else:
            tematica = "Desconocido"
        
        l.append((titulo, votos_positivos, precio, tematica, complejidad))
    
    con = connect('juegos.db')
    con.text_factory = str
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS Juegos')
    cur.execute('CREATE TABLE Juegos(ID INTEGER PRIMARY KEY AUTOINCREMENT, TITULO TEXT, VOTOS_POSITIVOS INT, PRECIO FLOAT, TEMATICA TEXT, COMPLEJIDAD TEXT)')
    
    for juego in l:
        print("INSERT INTO Juegos(TITULO, VOTOS_POSITIVOS, PRECIO, TEMATICA, COMPLEJIDAD) VALUES ('{0}',{1},{2},'{3}','{4}')".format(juego[0],str(juego[1]).replace("%","").strip(),juego[2].replace(',','.').replace('€','').strip(), juego[3], juego[4]))
        cur.execute("INSERT INTO Juegos(TITULO, VOTOS_POSITIVOS, PRECIO, TEMATICA, COMPLEJIDAD) VALUES ('{0}',{1},{2},'{3}','{4}')".format(juego[0],str(juego[1]).replace("%","").strip(),juego[2].replace(',','.').replace('€','').strip(), juego[3], juego[4]))
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='Juegos'")
    if res.fetchone() is not None:
        messagebox.showinfo("Successful Creation","Almacenados " + str(cur.execute("SELECT COUNT(*) FROM Juegos").fetchone()[0]) + " juegos")
    con.commit()
    con.close()
    
def imprimir_juegos(cursor):
    v = Toplevel()
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, width=150, yscrollcommand=sc.set)
    for row in cursor:
        s = 'TÍTULO: ' + row[1]
        lb.insert(END, s)
        lb.insert(END, "\n\n")
        s = "VOTOS POSITIVOS: " + str(row[2])
        lb.insert(END, s)
        lb.insert(END, "\n\n")
        s = "PRECIO: " + str(row[3])
        lb.insert(END, s)
        lb.insert(END, "\n\n")
        s = "TEMÁTICA: " + row[4]
        lb.insert(END, s)
        lb.insert(END, "\n\n")
        s = "COMPLEJIDAD: " + row[5]
        lb.insert(END, s)
        lb.insert(END, "\n\n")
        lb.insert(END, "-----------------------------------------------------")
    lb.pack(side=LEFT, fill=BOTH)
    sc.config(command=lb.yview)
    
def commandJuegos():
    conn = connect('juegos.db')
    conn.text_factory = str
    cur = conn.cursor()
    cur = conn.execute("SELECT * FROM Juegos") 
    imprimir_juegos(cur)
    conn.close
   
    
        

def commandMejoresJuegos():
    pass


def ventana_principal():
    menubar = Menu(root)
    root.config(menu = menubar) 
    datosMenu = Menu(menubar, tearoff=0)
    listarMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Datos", menu=datosMenu)
    menubar.add_cascade(label="Listar", menu=listarMenu)

    datosMenu.add_command(label = "Cargar", command = commandCargar)
    datosMenu.add_command(label = "Salir", command = root.quit)

    listarMenu.add_command(label = "Juegos", command = commandJuegos)
    listarMenu.add_command(label = "Mejores juegos", command = commandMejoresJuegos)

    root.mainloop()


ventana_principal()

