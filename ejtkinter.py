from tkinter import *
from sqlite3 import *

top = Tk()

def populate_table(table,tuplas):
    query = "INSERT INTO " + table + " VALUES"
    for tupla in tuplas:
        query += tupla
        if tupla != tuplas[len(tuplas)-1]:
            query += ","
    return query

def almacena():
    con = connect("ejtkinter.db")
    cur = con.cursor()
    cur.execute("DROP TABLE news")
    cur.execute("CREATE TABLE news(title, link, date)")
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='news'")
    if res.fetchone() is not None:
        print("BD creada correctamente")
    query = populate_table("news",lista_tuplas)
    cur.execute(query)
    con.commit()
    
def lista(selectquery):
    newtab = Toplevel()
    text = Text(newtab)

    con = connect("ejtkinter.db")
    cur = con.cursor()
    noticias = cur.execute(selectquery)
    
    text.insert(INSERT,noticias)
    
    con.commit()


def lista_por_mes():
    month = StringVar()
    label = Label(top, text = "Introduzca el mes (mm): ")
    label.grid(row = 2, column = 1)
    input = Entry(top, textvariable = month)
    input.grid(row = 2, column = 2)
    lista("SELECT * FROM news n WHERE ")
    



b1 =  Button ( top, text = "Almacenar", relief = RAISED, command = almacena)
b2 =  Button ( top, text = "Listar", relief = RAISED, command = lista)
b3 =  Button ( top, text = "Busca Mes", relief = RAISED, command = lista_por_mes)
b4 =  Button ( top, text = "Busca Dia", relief = RAISED )
b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)
b4.grid(row = 0, column = 3)

top.mainloop()

