str1 = "separable"
ch = ','

def ej1a(string, character):
    cadena = ""
    for i in string:
        cadena +=  i + character
    return cadena[0:len(cadena)-1:1]

print(ej1a(str1,ch))

##########################################################

def ej1b(string, caracter):
    cadena = ""
    for c in string:
        if c == ' ':
            cadena += caracter
        else:
            cadena += c
    return cadena

print(ej1b("mi archivo de texto.txt", '_'))

##########################################################

def ej1c(string, caracter):
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    cadena = ""
    for c in string:
        if c in numeros:
            cadena += caracter
        else:
            cadena += c
    return cadena

print(ej1c("su clave es: 1540", 'X'))


##########################################################

def ej1d(string, caracter):
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    cadena = ""
    digit_counter = 0
    for c in string:
        cadena += c
        if c in numeros:
            digit_counter+=1
        if digit_counter % 3 == 0:
            cadena += caracter
    return cadena

print(ej1d("2552552550", '.'))


##########################################################
'''
#Ejercicio 2. Escribir funciones que dadas dos cadenas de caracteres:
#a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo,
’cadena’ es una subcadena de ’subcadena’.
b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe ’kde’ y
’gnome’ debe devolver ’gnome’. 
'''

def ej2a(str1, str2):
    return str2 in str1

print(ej2a("subcadena","cadena"))

###########################################################

def ej2b(str1,str2):
    if str1 < str2:
        return str1
    else:
        return str2

print(ej2b("Alo","Aliteracion"))


