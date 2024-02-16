# variables
# input: obtiene datos del usuario
# int: indica que los datos que recibira del ususario seran numeros enteros

n1 = int(input("Ingresa el primer dato: "))
n2 = int(input("Ingresa el segundo dato: "))

suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

mensaje = f"""Para los números {n1} y {n2},
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicación es {mult}
el resultado de la división es {div}"""
print(mensaje)