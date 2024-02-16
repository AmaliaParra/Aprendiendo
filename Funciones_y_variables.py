# funciones
# parametro: nombre de la variaboe dentro de la función. Para que una variable tenga mas de un parametro, estos van dentros del parentesis y se separan por comas
# argumento: valores que se le entregan a la funion
# para llamar a una funcion: se indica la funcion y entre parentesis se indica el argumento "nombreFuncion + ()"
# Iterar:
# ___________________________________________________________________________________________________________________________________________________________________________________
# 1.1. FUNCION str: string

# Variable
# siempre deben empezar con una letra y
# no deben tener espacio,
# puede ser, todo con mayusculas, o con mayusculas intermedias
# base "0" para los indices
# indices: es el numero que se le asigna a cada letra de cada palabra ejemplo: Ultimate = U=1, l=2, t=3 etc
# metodo: funcion dentro de un objeto
# import: se utiliza para traer un archivo externo que contiene codigo en python
import math

nombre_curso = "Ultimate Python"
print(nombre_curso)

# ___________________________________________________________________________________________________________________________________________________________________________________
# 2. Números

# int: integer
numero = 2
# decimal: float
decimal = 1.2
# imaginario
imaginario = 2 + 2j

print(1 + 3)
print(1 - 3)
print(1 * 3)
print(1 / 3)
print(1 // 3)  # muestra solo la parte entera del resultado
print(1 % 3)  # muestra solo el modulo del resultado #aproxima
print(2 ** 3)  # exponente

# += : toma la variable anterior y le suma el siguiente y funciona para todad las oeraciones
# ejemplo

numero += 3
print("numero", numero)
numero -= 3
print("numero", numero)
numero *= 3
print("numero", numero)
numero /= 3
print("numero", numero)
numero %= 3
print("numero", numero)
numero **= 3
print("numero", numero)


# funciones en numeros
# round: aproxima
print(round(1.3))

# abs: valor absoluto
print(abs(-77))

# modulo: archivo externo que contiene codigo en python
# ejemplo import math: https://docs.python.org/3/library/math.html

# ceil: aproxima al numero mas cercano hacia arriba
print(math.ceil(1.1))

# floor aproxima al numero mas cercano hacia abajo
print(math.floor(1.9988))

# insnan: entregara un valor booleano en el que xpondra si el valor entre parentesis en o no un numero, solamente acepta caracteres numericos
print(math.isnan(23))

# pow: exponente
print(math.pow(12, 3))

# sqrt: raiz cuadrada
print(math.sqrt(4))

# operadores logicos/ de comparacion
# expresion: cadena de instrucciones que evaluar en una unica cosa
# ejemplo expresion(1+2) evaluacion (3)
print(1 > 2)  # puede entregar un valor bool
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print(1 == 2)
print(2 == "2")  # si se intenta comparar el numero (int 2) con (str 2), al ser datos diferentes (int y srt) entonces es falso
# en este caso, devuelve true porque esta negando que sean iguales y eso es cierto
print(2 != "2")
# en este caso se estan comparando dos int que valen lo mismo, por lo tanto seria falso
print(2 != 2)

# ___________________________________________________________________________________________________________________________________________________________________________________
# 3. FUNCION Bool: booleano
# True: valor booleano, que puede ser solo dos opciones de respuesta (1o0, verdadero o falso, s o no etc) se debe escribir con "T" mayuscula
publicado = True

# ___________________________________________________________________________________________________________________________________________________________________________________
# 4. Funciones y métodos
# estructura metodo: ... dato/argumento.metodo ()
# comillas dobles*3
descripcion_curso = """ultimate python contiene todos los detalles que necesitas saber"""
print(nombre_curso, descripcion_curso)

# ===================================================================================================================================================================================
# funcion type
# entrega el tipo de cadena o dato
# estructura: type(argumento)
print(type(nombre_curso))
# ===================================================================================================================================================================================
# funcion len
# permite obtener la longitud del string
# estructura: len(argumento)
# a continuacion se desea imprimir en monitor la funcion len, por lo tanto se agrega previo a la funcion, la funcion "print"
print(len(nombre_curso))
# ===================================================================================================================================================================================
# Funncion set
# permite crear conjuntos
# Solo permite datos que no se modificarán, como: tupla,
conjunto = set(["Dato1", "Dato2"])
print(conjunto)
# ===================================================================================================================================================================================
# issubset: Entregará una respuesta booleana, y determinará si el argumento es un subconjunto de (argumento2)
conjuntoA = {1, 2, 4, 6}
conjuntoB = {1, 6}
conjuntoC = conjuntoB.issubset(conjuntoA)
print(conjuntoC)

# otra forma
conjuntoC = conjuntoB <= conjuntoA
print(conjuntoC)
# ===================================================================================================================================================================================
# superset: Entregará una respuesta booleana, y determinará si el argumento es un superconjunto de (argumento2)
conjuntoA = {1, 2, 4, 6}
conjuntoB = {1, 6}
conjuntoC = conjuntoB.issuperset(conjuntoA)
print(conjuntoC)

# otra forma
conjuntoC = conjuntoB > conjuntoA
print(conjuntoC)

# ===================================================================================================================================================================================
# isdisjoint: entregará un resultado booleano y verifica si no hay datos en comun
conjuntoC = conjuntoB.isdisjoint(conjuntoA)
print(conjuntoC)
# ===================================================================================================================================================================================
# Funcion frozenset
# permite poner un conjunto dentro de otro conjunto
conjunto1 = frozenset({"Dato 1", "Dato 2"})
conjunto2 = {conjunto1, "Dato 3"}
print(conjunto2)

# ===================================================================================================================================================================================
# FUNCION tupla
# es como una lista, pero no se puede modificar más adelante
# se puede hacer con ([])
# ejemplo
fono = tuple(["966", "00", "68", "15"])
print(type(fono))
# otra forma
fona = "966", "00"
print(type(fona))
# ===================================================================================================================================================================================
# FUNCION list
# permite crear una lista
lista = list(["Amalia", "25 AÑOS", "ESCORPIO"])
print(lista)
print(len(lista))  # devuelve la cantidad de elementos de la lista

# METODOS PARA LAS LISTAS
# append: agrega un elemento a la lista
lista.append("Organizada")

# insert: agrega un elemento a la lista en un indice especifico
lista.insert(2, "Estudiosa")

# extend: agrega varios elementos a la lista
lista.extend(["Electricista", "Programadora", "Mamisonga"])
print(lista)

# pop: elimina un elemento de la lista por subindice
# -1 para eliminar el ultimo, -2 para eliminar el anteultimo y asi sucesivamente
lista.pop(1)
print(lista)

# remove: remumeve un elemento por su valor
lista.remove("Mamisonga")
print(lista)

# sort: ordena los elementos de una lista de cadena de caracteres numericos y booleanos en orden ascendente
lista2 = ([19, 11, 1998, 29, 12, 2008])
lista2.sort()
print(lista2)
lista2.sort(reverse=True)
print(lista2)

# reverse: invierte los elementos de una lista
lista2.reverse()
print(lista2)

# clear: elimina los elementos de la lista
lista.clear()
print(lista)
# ===================================================================================================================================================================================
# INPUT: permite recibir datos del usuario
# cuando se necesita una respuesta de string
""" nombre_input = input("Escribe tu nombre: ")
# cuando se necesita una respuesta numerica
edad_entero = int(input("Escribe tu edad: "))
edad_decimal = float(input("Escribe tu edad con meses: "))
 """
# ===================================================================================================================================================================================
# DICCIONARIO
# Estructura: keys: value, value, value etc
# o keys : value ,
#          value ,
# debe usar solo datos "hashable"

diccionario = {
    "lugar": "Casa",
    "color": "blanca",
    "fnac": "1998"
}
# dict: crear diccionario
diccionario2 = dict(Nombre2="Amallita", apellido2="Parra")
print(diccionario2)

# fromkeys: crea diccionario con cualquier valor none
diccionario2 = dict.fromkeys("nombre1", "apellido2")
print(diccionario2)
# si, "diccionario3 = dict.fromkeys()" se ingresa solo con parentesis, del primer argumento usará la primera letra para elaborar keys
# si, "diccionario3 = dict.fromkeys([])" se crea una lista dentro, entonces, tomara cada argumento como una key
diccionario2 = dict.fromkeys(["nombre1", "apellido2"])
print(diccionario2)
# si, "print(diccionario3 = dict.fromkeys("argumento"))" imprimirá solo el argumento y su none respectuivo
print(diccionario2["apellido2"])

# keys: devuelve las claves y iterar
print(diccionario.keys())

# get: devuelve el valor de la clave
print(diccionario.get("color"))

# pop: elimina un elemento del diccionario
print(diccionario.pop("fnac"))

# clear: elimina todos los elementos del diccionario
print(diccionario.clear())

# ===================================================================================================================================================================================
# FUNCION print
# permite mostrar en monitor
# estructura: print + ()
# si se desea acceder a un caracter en particular, se utilizan los parentesis cuadrados, ejemplo: print + (argumento1[argumento2])
print(nombre_curso[0])
# si se desea cortar el strin de "nombre_curso", es decir obtener la palabra de ultimate python
# estructura: print(nombre_curso[donde se desea iniar a recortar:cuantos caracteres se desean])
print(nombre_curso[0:8])
# si no se agrega el segundo argumento, el lenguaje entendera que va desde el primer agumento hasta el final
print(nombre_curso[9:])
# si no se agrega el primer argumento, el lenguaje entendera que va desde el inicio hasta el argumento 2
print(nombre_curso[:10])
# si no se agraga ningun valor entre ":" simplemente se imprime el string completo
# ===================================================================================================================================================================================
# operador de concatenacion: permite agregar mas argumentos a una funcion
# "+"
nombre = "Amalia"
apellido = "Parra"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# otra manera: operador de formateo de strings
# estructura print(f"texto {argumento1}, {argumento2}")

nombreCompleto = f"{nombre} {apellido}"
print(nombreCompleto)

# otra manera
# con un  "." entre los metodos ejemplo en #strip+capitalize mas abajo

# ___________________________________________________________________________________________________________________________________________________________________________________

# en los siguientes casos el metodo entregara respuestas gramaticales

# upper: metodo que transforma el argumento anterior a letras mayusculas
#  ejemplo
print(nombreCompleto.upper())
# ===================================================================================================================================================================================

# lower: metodo que transforma el argumento anterior a letras minusculas
#  ejemplo
print(nombreCompleto.lower())
# ===================================================================================================================================================================================

# capitalize: metodo que transforma a estilo oracion, es decir, primer caracter en mayuscula mientras que el resto de la oracion es minuscula
# ejemplo
print(nombreCompleto.capitalize())
# ===================================================================================================================================================================================

# title: metodo que transforma a estilo nombre propio, es decir, primer caracter de cada palabra de la oracion en mayuscula
# ejemplo
print(nombreCompleto.title())
# ===================================================================================================================================================================================

# strip: remueeve los espacios al principio y al finald e la oracion
# ejemplo
print(nombreCompleto.strip())
# ===================================================================================================================================================================================

# strip+capitalize
# ejemplo
print(nombreCompleto.strip().capitalize())
# ===================================================================================================================================================================================

# lstrip: quita los espacios en blanco a la izquiera del string
# ejemplo
print(nombreCompleto.lstrip())
# ===================================================================================================================================================================================

# rstrip: quita los espacios en blanco a la izquiera del string
# ejemplo
print(nombreCompleto.rstrip())
# ===================================================================================================================================================================================

# find: buscara una cadena de caracteres que le indiquemos entre parentesis y nos entregara el indice
# ejemplo
print(nombreCompleto.find("ali"))
# si la cadena de caracteres esta mal redactada, entregara un "-1" que significa que no existe en ese string
# ===================================================================================================================================================================================

# index: buscará una cadena en otra cadena
# ejemplo
print(nombreCompleto.index("i"))
# ===================================================================================================================================================================================

# count: buscará una cadena en otra cadena y devolvera cuantas veces la encontro
# ejemplo
print(nombreCompleto.count("a"))
# ===================================================================================================================================================================================

# replace: reemplazará caracteres
# ejemplo
print(nombreCompleto.replace("ali", "ALI"))
# ===================================================================================================================================================================================

# isnumeric: buscará si esa cadena de caracteres está compuesta solo de numeros, devolverá valor booleano
# ejemplo
print(nombreCompleto.isnumeric())
# ===================================================================================================================================================================================

# isalpha: buscará si esa cadena de caracteres está compuesta solo de numeros, devolverá valor booleano
# ejemplo
print(nombreCompleto.isalpha())
# ===================================================================================================================================================================================

# startswith: verifica si la cadena inica con el valor dado, devolvera un valor booleano
# ejemplo
print(nombreCompleto.startswith("a"))
# ===================================================================================================================================================================================

# endswith: verifica si la cadena termina con el valor dado, devolvera un valor booleano
# ejemplo
print(nombreCompleto.endswith("a"))
# ===================================================================================================================================================================================

# split: separa la cadena con la que le pasemos
# ejemplo
print(nombreCompleto.split(","))
# ===================================================================================================================================================================================


# ___________________________________________________________________________________________________________________________________________________________________________________
# en los casos siguiente el metodo entregara respuestas booleanas

# in: buscara la cadena de carcateres que se le indica pertenece al segundo argumento.
# en este caso el metodo va dentro del parentesis
# ejemplo print ("argumento1" in argumento2)
print("ali" in nombreCompleto)
# ===================================================================================================================================================================================

# not in: buscara la cadena de carcateres que se le indica NO pertenece al segundo argumento.
# en este caso el metodo va dentro del parentesis
# ejemplo print ("argumento1" not in argumento2)
print("ali" not in nombreCompleto)

# ===================================================================================================================================================================================

# 1.2 secuencias de escape: se utiliza para hacer entender al pc que el texto que viene a continuacion no es un caracter propio del lenguaje sino, parte del string

# crear nueva variable
curso = "U. python"
# Cuando se desean usar comillas dobles dentro de un sctring (dentro de otras comillas) se utiliza "\" antes y despues de las comillas dentro del srting
# \": ejemplo: curso = "Ultimate \"Python\""
# \': ejemplo: curso = "Ultimate \'Python\'"
# \\: ejemplo: curso = "Ultimate \\Python\\"
# \n: toma el string que continua y lo pasa a la siguiente liena
# ejemplo: curso = "Ultimate \nPython"
curso = "Ultimate \nPython"
print(curso)


# if, else: si cierta "condicion" se cumple entonces se le entregan ciertas instrucciones
# elif: agrega condiciones

edad = 66

if edad > 65:
    print("Desea aplicar su super descuento")
elif edad > 54:
    print("Desea aplicar su descuento")
elif edad > 17:
    print("Puede ver la peli")
else:
    print("No puede ver la peli")

print("Hasta pronto")

# operador ternario: va de la mano con la funcion if y else y su objetivo es devuelver un valor y lo asigna a la variable a la izquierda
# argumento 1 sera verdadero siempre que se cumpla la condicion a su derecha, esta condicion debe estar ubicada entre un if y un else, respectivamente. En caso de que no se cumpla la condicion, es decir, sea falso, se imprimira el mensaje a la derecha del else.

edad2 = 19

mensaje2 = "Es mayor" if edad2 > 17 else "Es menor"

print(mensaje2)

# operadores logicos: entrega un valor booleano y debe cumplir las siguientes condiciones
# and: (and, &) ambos argumentos deben ser true, si cualquiera de los dos es false, entonces el resultado final sera false
# or: (or, |, ||) 1 de los argumentos debe ser false para que el resultado final de true, sino, será false
# not: (not) invierte el resultado final, es decir, si resulta true, nor lo invertira a false.
# ejemplo

# se declaran variables

gas = False
encendido = True

if gas and encendido:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")

# operadores de corto circuito: se refiere a que evitará avanzar en la funcion de ser evidente el reesultad,
# ejemplo: si se esta usando un or, y ya el primero es true entonces se salta el resto de los argumentos

# cadena de comparadores

edad3 = 25

if edad3 >= 18 and edad3 <= 59:
    print("Puede ver la peli")
elif edad3 >= 60:
    print("Desea aplicar su super descuento")
else:
    print("No puede ver la peli")

# for: es un loop (se repite) y se utiliza para iterar/repetir una lista de elementos
#
# range: crea una secuencia de numeros entre el cero y el anterior al que se indica

for numero in range(5):
    print(numero, numero * "hola mundo")

# for else:
# break: detiene la ejecucion del codigo
# en esta seccion,
buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontrado")

# iterables

for char in "Ultimate python":
    print(char)

# while: es un loop y se utiliza para trabajar con algo siempre y cuando se cumpla cierta condicion
    # recolecta infinitamente informacion del usuario
# evalua lo que se encuentra a la derecha del while, si es que es verdadero o falso
    # si es verdadero: permite ejecutar el codigo dentro de while

numero2 = 1.0

while numero2 < 100:
    print(numero2)
    numero2 *= 2

""" comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando) """
# se agrega metodo "lower" para que el comando sea como sea que lo escriba el usuario este sea efectivo

# loops infinitos: es cuando no se tiene una condicion de salida, por lo tanto se ejecuta para siempre
# loop anidados

for j in range(3):  # ejeuta de arriba a abajo #outer for/loop
    for k in range(2):  # inner for/loop
        print(f"{j}, {k}")

# CREAR FUNCIONES
# estrufctura:
    # def nombreFuncion():
    # en esta seccion van las instrucciones de la nueva variable


def hola():
    print("holamundo")


hola()

# otra forma


def hola2(variable2, variable3):
    print(f"Bienvenido {variable2} {variable3}")


hola2("amalia", "parra")

# argumentos opcionales


def hola3(variable4, variable5="uvita"):
    print(f"Bienvenido {variable4} {variable5}")


hola3("amalia", "parra")
hola3("amalia")

# argumentos nombrados


def hola4(variable6, variable7="uvita"):
    print(f"Bienvenido {variable6} {variable7}")


hola4("amalia", "parra")
hola4("amalia")
hola4(variable7="salgado", variable6="paz")

# xargs


def suma(a, b):
    print(a + b)


suma(2, 5)

# _________________________________________________________________________________________________________
# BUCLE
# sentencias que permiten iterar

# for in: crea una variable
# 1. crea lista
# 2. bucle se ejecuta segun cuantos argumentos haya en la lista

flores = (["Doca", "Tara", "Espino", "Chagual", "Manzanilla"])
# la variable "flor" no se declara, porque solo se usa en esa variable de codigo
for flor in flores:
    print(f"Ahora la variable es igual a: {flor}")
