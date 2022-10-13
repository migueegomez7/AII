
from tkinter import messagebox
from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
from sqlite3 import *

root = Tk()



def extraer_pelis():
    BASE_URL = "https://www.elseptimoarte.net"
    url = BASE_URL + "/estrenos/"
    f = urllib.request.urlopen(url)
    s = BeautifulSoup(f,"lxml") #lxml is a parser
    l = []
    link_peliculas = s.find("ul", class_="elements").find_all("li") #Si pones class es palabra protegida de python
    for pelicula in link_peliculas:
        pagina_peli = urllib.request.urlopen(BASE_URL+pelicula.a["href"])
        s = BeautifulSoup(pagina_peli,"lxml")
        datos = s.find("section", class_="highlight").div.dl
        titulo_original = datos.find("dt", string="Título original").find_next_sibling("dd").string
        if (datos.find("dt", string="Título")):
            titulo = datos.find("dt", string="Título").find_next_sibling("dd").string
        else:
            titulo = titulo_original
        paisEs = " ".join(datos.find("dt",string="País").find_next_sibling("dd").stripped_strings)
        fechaEstreno=datos.find("dt", string="Estreno en España").find_next_sibling("dd").string
        director=datos.find("dt", string="Director").find_next_sibling("dd").a.string
        generoS = pelicula.find("p", class_ = "generos").string
        
        l.append((titulo, titulo_original, paisEs, fechaEstreno, director, generoS))

    return l

def cargar():
    con = connect("pelis.db")
    con.text_factory = str
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS pelis")
    cur.execute("CREATE TABLE pelis(ID INTEGER PRIMARY KEY AUTOINCREMENT, TITULO TEXT, TITULO_ORIGINAL TEXT NOT NULL, PAISES TEXT NOT NULL, FECHA_ESTRENO DATE NOT NULL, DIRECTOR TEXT NOT NULL, GENEROS TEXT NOT NULL)")
    l = extraer_pelis()

    for pelicula in l:
        insert = 'INSERT INTO pelis (TITULO, TITULO_ORIGINAL, PAISES, FECHA_ESTRENO, DIRECTOR, GENEROS) VALUES ("{0}", "{1}", "{2}", {3}, "{4}", "{5}")'.format(pelicula[0], pelicula[1], pelicula[2], pelicula[3], pelicula[4], pelicula[5])
        print(insert)
        cur.execute(insert)

    res = cur.execute("SELECT name FROM sqlite_master WHERE name='pelis'")
    if res.fetchone() is not None:
        messagebox.showinfo("Successful Creation","Almacenadas " + str(con.execute("SELECT COUNT(*) FROM pelis").fetchone()[0]) + " peliculas")


def commandCargar():
    cargar()

def commandListar():
    pass

def commandSalir():
    root.destroy()

def commandBuscarPorTitulo():
    pass

def commandBuscarPorFecha():
    pass

def commandBuscarPorGenero():
    pass


def ventana_principal():
    menubar = Menu(root)
    root.config(menu = menubar) 
    datosMenu = Menu(menubar, tearoff=0)
    buscarMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Datos", menu=datosMenu)
    menubar.add_cascade(label="Buscar", menu=buscarMenu)

    #DATOS
    datosMenu.add_command(label = "Cargar", command = commandCargar)
    datosMenu.add_command(label = "Listar", command = commandListar)
    datosMenu.add_command(label = "Salir", command = root.quit)

    #BUSCAR
    buscarMenu.add_command(label = "Titulo",command = commandBuscarPorTitulo)
    buscarMenu.add_command(label = "Fecha",command = commandBuscarPorFecha)
    buscarMenu.add_command(label = "Genero",command = commandBuscarPorGenero)

    root.mainloop()
    '''
    menubar = Menu(root)

    #DATOS
    menudatos = Menu(menubar, tearoff=0)
    menudatos.add_command(label = "Cargar", command = commandCargar)
    menudatos.add_command(label = "Listar", command = commandListar)
    menudatos.add_command(label = "Salir", command = root.quit)
    menudatos.add_cascade(label = "Datos", menu = menudatos)

    #BUSCAR
    menubuscar = Menu(menubar, tearoff = 0)
    menubuscar.add_command(label = "Titulo",command = commandBuscarPorTitulo)
    menubuscar.add_command(label = "Fecha",command = commandBuscarPorFecha)
    menubuscar.add_command(label = "Genero",command = commandBuscarPorGenero)
    menudatos.add_cascade(label = "Buscar", menu = menubuscar)

    root.config(menu = menubar)
    root.mainloop()
    '''

ventana_principal()