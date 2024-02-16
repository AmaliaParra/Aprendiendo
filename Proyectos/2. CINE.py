edad = int(input("Ingrese su edad=  "))

if edad >= 18 and edad <= 59:
    print("Puede ver la peli")
elif edad >= 60:
    print("Desea aplicar su super descuento")
else:
    print("No puede ver la peli")

print("Hasta pronto")