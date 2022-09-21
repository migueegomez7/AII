'''
Ejercicio 1. Campaña electoral
a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
el mensaje Estimado <nombre>, vote por mí.
b) Escribir una función que reciba una tupla con nombres, una posición de origen p y
una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a
partir de la posición p.
c) Modificar las funciones anteriores para que tengan en cuenta el género del
destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el
género.
'''

tuplaNombres = ('Pablo', 'Miguel', 'Hola', 'Amigo', 'Ey', 'Antonio', 'Que')
tuplaNombresGenero = (('Pablo', 'M'), ('Migue', 'M'), ('Antonia', 'F'), ('Paula', 'F'), ('Alejandro', 'M'), ('Paca', 'F'), ('Juan', 'M'))

def ej1a(tupla):
    for nombre in tupla:
        print("Estimado " + nombre + ", vote por mí.")

#ej1a(tuplaNombres)

def ej1b(tupla, py, n):
    for i in range(py, py + n):
        print("Estimado " + tupla[i] + ", vote por mí.")

#ej1b(tuplaNombres, 1, 3)

def ej1c(tupla, py, n):
    for i in range(py, py + n):
        if tupla[i][1] == 'M':
            print("Estimado " + tupla[i][0] + ", vote por mí.")
        else:
            print("Estimada " + tupla[i][0] + ", vote por mí.")

ej1c(tuplaNombresGenero, 1, 4)

'''''''''
Ejercicio 2. Escribir una función que reciba una lista de tuplas (Apellido, Nombre,
Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga
primero el nombre, luego la inicial con un punto, y luego el apellido. 

'''

tupla2 = [("Gomez","Miguel","A"),("Kennedy","John","F"),("Espada", "Pablo","J")]

def ej2(tupla2):
    ls = []
    for tp in tupla2:
        ls.append(tp[1] + " " + tp[2] + ". " + tp[0])
    return ls

print(ej2(tupla2))

'''
Ejercicio 1. Agenda simplificada
Escribir una función que reciba una cadena a buscar y una lista de tuplas
(nombre_completo, telefono), y busque dentro de la lista, todas las entradas que
contengan en el nombre completo la cadena recibida (puede ser el nombre, el apellido
o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas
encontradas. 
'''
listatuplas = [("Miguelon gomez gomez", "912123456"),("Pablo Espada Hoyo", "123456789"),("Chema Contreras","123321456")]

def ejBusqueda(lista, cadena    ):
    listaRes = []
    for tupla in lista:
        if cadena in tupla[0]:
            listaRes.append(tupla)
    return listaRes

print(ejBusqueda(listatuplas, "Migue"))

'''


Diccionarios
Ejercicio 1. Continuación de la agenda.
Escribir un programa que vaya solicitando al usuario que ingrese nombres.
a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe
mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. 
b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena "*", para salir del programa. 
'''
diccionario = dict()
def ejDiccionarios():
    while True:
        nombre = input("Ingrese un nombre:")
        if str(nombre) != "*":
            if nombre not in diccionario.keys():
                telefono = input("Ingrese un numero:")
                diccionario[nombre] = telefono # dicccionario.put(nombre, telefono)
                print(diccionario)
            else:
                print(diccionario[nombre])
                correcto = input("Si es correcto el telefono escriba 'si'")
                if correcto != "si":
                    telefono = input("Ingrese un numero:")
                    diccionario[nombre] = telefono
        else:
            break        
                
    

ejDiccionarios() 


