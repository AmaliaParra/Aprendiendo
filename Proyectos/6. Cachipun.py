import random
def jugar():

    print("===========Bienvenido===========")
    print(" ")
    print("Instrucciones: ")
    print("Debes elegir una opción")
    print(" piedra, papel o tijera")
    print("Elige una opción")
    print(" ")

    usuario = str(input(usuario).lower())
    computadora = random.choice(["piedra", "papel", "tijera"])


    # REGLAS

    if usuario == computadora:
        return "Empate"
    
    if (( piedra > tijera
