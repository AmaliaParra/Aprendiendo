# este proyecto se trata de concatenar cadenas de caracteres

# creacion de variables

print("Encuentra las palabras ocultas: ")
print(" ")
print("la ______ no es más que perversión en sí misma a menos que tenga como _________ último mejorar la __________")
print(" ")

print("Cuál es la primera palabra: ")
p1 = input("Escribe aquí la palabra: ")
print("Cuál es la segunda palabra: ")
p2 = input("Escribe aquí la palabra: ")
print("Cuál es la tercera palabra: ")
p3 = input("Escribe aquí la palabra: ")

if p1 == "ciencia" and p2 == "objetivo" and p3 == "humanidad":
    texto = f"La {p1} no es más que perversión en sí misma a menos que tenga como {
        p2} último mejorar la {p3}"
    print(texto)
else:
    print("Alguna de tus respuestas no fue acertada")
    print("Vuelve a intentarlo")
    print("No te rindas")
    