from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from ej1 import *

top = Tk()

def populate_table(table,tuplas):
    query = "INSERT INTO " + table + " VALUES"
    for tupla in tuplas:
        query += "('" + tupla[0] + "','" + tupla[1] + "','" + tupla[2] + "')"
        if tupla != tuplas[len(tuplas)-1]:
            query += ","
    return query

def almacenaBt():
    almacena("https://sevilla.abc.es/rss/feeds/Sevilla_Sevilla.xml")

def almacena(url):
    con = connect("ejtkinter.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS news")
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("CREATE TABLE news(title, link, date)")
    cur.execute("CREATE TABLE test(title TEXT NOT NULL, link TEXT NOT NULL, date DATE NOT NULL)")
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='news'")
    if res.fetchone() is not None:
        messagebox.showinfo("Successful Creation","BD creada correctamente")
    abrir_url(url, "./noticias_almacenadas")
    lista_tuplas = tratar_archivo("./noticias_almacenadas")
    query = populate_table("test",lista_tuplas)
    print(query)
    cur.execute(query)
    con.commit()
    

def listaBt():
    lista("SELECT * FROM test")

def lista(selectquery):
    con = connect("ejtkinter.db")
    cur = con.cursor()
    newtab = Toplevel()
    sc = Scrollbar(newtab)
    sc.pack(side = RIGHT, fill = Y)
    lb = Listbox(newtab, width = 200, yscrollcommand=sc.set)
    for row in cur.execute(selectquery):
        lb.insert(END, row[0])
        lb.insert(END, row[1])
        lb.insert(END, row[2])
        lb.insert(END, '')
    lb.pack(side = LEFT, fill = BOTH) #Fill lo que hace es que lb se adapte al tamaño de la ventana(fillea la ventana) :)
    sc.config(command = lb.yview)
    

    #Si pongo aquí un print(noticias.fetchall()) no lo guarda en var luego. Por qué? El fetch solo funca una vez??
'''    var = StringVar()
    var = noticias.fetchall()
    con.commit()

    text.insert(INSERT,var)
    text.pack()
'''

def lista_por_mes():
    month = StringVar()
    label = Label(top, text = "Introduzca el mes (mm): ")
    label.grid(row = 2, column = 1)
    input = Entry(top, textvariable = month)
    input.grid(row = 2, column = 2)
    lista("SELECT * FROM news n WHERE ")
    



b1 =  Button ( top, text = "Almacenar", relief = RAISED, command = almacenaBt)
b2 =  Button ( top, text = "Listar", relief = RAISED, command = listaBt)
b3 =  Button ( top, text = "Busca Mes", relief = RAISED, command = lista_por_mes)
b4 =  Button ( top, text = "Busca Dia", relief = RAISED )
b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)
b4.grid(row = 0, column = 3)

top.mainloop()

