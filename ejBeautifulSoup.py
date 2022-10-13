from tkinter import messagebox
from traceback import print_tb
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
'''
    locales = []
    visitantes = []
    for i in range(len(l)):
        s.find
'''
def imprimir(cursor):
    newtab = Toplevel()
    sc = Scrollbar(newtab)
    sc.pack(side = RIGHT, fill = Y)
    lb = Listbox(newtab, width = 200, yscrollcommand=sc.set)
    for row in cursor:
        lb.insert(END, "Jornada: " + str(row[0]))
        lb.insert(END, "Local: " + row[1])
        lb.insert(END, "Visitante: " + row[2])
        lb.insert(END, "Goles local: " + str(row[3]))
        lb.insert(END, "Goles visitante: " + str(row[4]))
        lb.insert(END, "Link de visionado: " + row[5])
        lb.insert(END, '')
    lb.pack(side = LEFT, fill = BOTH) #Fill lo que hace es que lb se adapte al tamaño de la ventana(fillea la ventana) :)
    sc.config(command = lb.yview)

def almacenar():
    con = connect("ejtkinter.db")
    con.text_factory = str
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS partidos")
    cur.execute("CREATE TABLE partidos(JORNADA INTEGER NOT NULL, EQUIPO_LOCAL TEXT NOT NULL, EQUIPO_VISITANTE TEXT NOT NULL, GOLES_L INTEGER NOT NULL,GOLES_V INTEGER NOT NULL,LINK TEXT NOT NULL)")
    l = extraer_jornadas()
    for i in l: #Itera sobre jornadas
        jornada = i.a['title']
        match = re.search("([0-9])+",jornada)
        a = match.group(0)
        tbody = i.find("tbody").contents
        trs = [x for x in tbody if x != "\n"]
        for p in trs:
            local = p.find("td",class_ = "col-equipo-local").span.string
            visitante = p.find("td",class_ = "col-equipo-visitante").span.next_sibling.next_sibling.string
            resultado = p.find("a", class_ = "resultado").string
            stringa = "sadasdas 1234 - 567 - 9084 \n" #peta si le meto más números , pq?
            goles_l = re.findall("([0-9])+",resultado)[0]
            goles_v = re.findall("([0-9])+",resultado)[1]
            link = p.find("td", class_ = "col-resultado").a["href"]
            cur.execute("INSERT INTO partidos VALUES (?,?,?,?,?,?)",(a,local,visitante,goles_l,goles_v,link))
    con.commit()
    cursor = con.execute("SELECT COUNT(*) FROM partidos")
    messagebox.showinfo( "Base Datos", "Base de datos creada correctamente \nHay " + str(cursor.fetchone()[0]) + " registros")
    con.close()

def listar():
    con = connect("ejtkinter.db")
    cur = con.cursor()
    cur = con.execute("SELECT * FROM partidos")
    imprimir(cur)


def buscar_jornada():
    def listar_busqueda(event):
        conn = connect('ejtkinter.db')
        conn.text_factory = str
        s =  int(en.get())
        cursor = conn.execute("""SELECT * FROM partidos WHERE JORNADA = ?""",(s,)) 
        imprimir(cursor)       
        conn.close()
    
    conn = connect('ejtkinter.db')
    conn.text_factory = str
    cursor= conn.execute("""SELECT DISTINCT JORNADA FROM partidos""")
    valores=[i[0] for i in cursor]
    conn.close()
    
    v = Toplevel()
    lb = Label(v, text="Seleccione la jornada: ")
    lb.pack(side = LEFT)
    en = Spinbox(v,values=valores,state="readonly")
    en.bind("<Return>", listar_busqueda)
    en.pack(side = LEFT)


def populate(l):
    return "a"

def estadisticas_jornada():
    def listar_estadisticas(event):
        conn = connect('ejtkinter.db')
        conn.text_factory = str
        s =  int(en.get())
        cursor = conn.execute("""SELECT SUM(GOLES_L)+SUM(GOLES_V) FROM partidos WHERE JORNADA = ?""",(s,)) 
        total_goles = cursor.fetchone()[0]
        golitos = conn.execute("""SELECT GOLES_L,GOLES_V FROM partidos WHERE JORNADA = ?""",(s,))
        empates = 0
        locales = 0
        visitantes = 0
        for g in golitos:
            if g[0] == g[1]:
                empates += 1
            elif g[0] < g[1]:
                visitantes += 1
            else:
                locales += 1
        conn.close()
        newtab = Toplevel()
        sc = Scrollbar(newtab)
        sc.pack(side = RIGHT, fill = Y)
        lb = Listbox(newtab, width = 200, yscrollcommand=sc.set)
        lb.insert(END, "Jornada: " + str(s))
        lb.insert(END, "Goles totales: " + str(total_goles))
        lb.insert(END, "Empates: " + str(empates))
        lb.insert(END, "Gana local: " + str(locales))
        lb.insert(END, "Gana visitante: " + str(visitantes))
        lb.pack(side = LEFT, fill = BOTH) #Fill lo que hace es que lb se adapte al tamaño de la ventana(fillea la ventana) :)
        sc.config(command = lb.yview)
        
    conn = connect('ejtkinter.db')
    conn.text_factory = str
    cursor= conn.execute("""SELECT DISTINCT JORNADA FROM partidos""")
    valores=[i[0] for i in cursor]
    conn.close()
    
    v = Toplevel()
    lb = Label(v, text="Seleccione la jornada: ")
    lb.pack(side = LEFT)
    en = Spinbox(v,values=valores,state="readonly")
    en.bind("<Return>", listar_estadisticas)
    en.pack(side = LEFT)

def ventana_principal():
    top = Tk()
    top.geometry("300x300")
    b1 =  Button ( top, text = "Almacenar", relief = RAISED, command = almacenar)
    b2 =  Button ( top, text = "Listar", relief = RAISED, command = listar)
    b3 =  Button ( top, text = "Buscar Jornada", relief = RAISED, command = buscar_jornada)
    b4 =  Button ( top, text = "Estadísticas Jornada", relief = RAISED, command = estadisticas_jornada)
    b1.pack(side = TOP)
    b2.pack(side = TOP)
    b3.pack(side = TOP)
    b4.pack(side = TOP)
    s = extraer_jornadas()
    top.mainloop()

if __name__ == "__main__":
    ventana_principal()