#  CODIGO ORIGINAL

# import random

# def adivina_el_numero(x):
#     print("===========================================================")
#     print(" Bienvenido al juego ")
#     print("   Debes adivinar el número generado por la computadora")
#     print("==========================================================")

#     numero_aleatorio = random.randint(1, x)

#     prediccion = 0

#     while prediccion != numero_aleatorio:
#         prediccion = int(input(f"Ingresa un número entre 1 y {x}: "))

#         if prediccion < numero_aleatorio:
#             print("Este número es muy pequeño, intenta otra vez")
#         elif prediccion > numero_aleatorio:
#             print("Este número es muy grande, intenta otra vez")

#     print(f"Felicidades, adivinaste el número {numero_aleatorio} correctamente!!")

# adivina_el_numero(10)


# MI CODIGO

import random


print("===========================================================")
print("                     Adivina el número")
print(" ")
print("                       Instrucciones: ")
print("   Debes adivinar el número generado por la computadora")
print(" ")
print("==========================================================")
print(" ")

# Aquí se indica que "X" será un numero (int) entregado por el ususario (input)
x = int(input("Ingresa el rango máximo ---->   "))
# Aquí se indica que el "numeroAleatrio" será un número entregado por el pc y tendrá la característica de ser aleatorio entre (1 , 10)
numeroAleatorio = random.randint(1, x)
intento = 0  # En esta línea se indica que la variable vale 0

while intento != numeroAleatorio:
    intento = int(input("Ingresa el número: "))

    if intento < numeroAleatorio:
        print("Este número es muy pequeño, intenta otra vez")
    elif intento > numeroAleatorio:
        print("Intenta otra vez")
print(f"Felicidades, acertaste el número: {numeroAleatorio} correctamente!!")

