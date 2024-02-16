print("          Calculadora")
print("          Instrucciones: ")
print("                        Para salir escriba \"salir\"")
print("                        Debes ingresar el simbolo de la operación que deseas")

# se guarda como un string "" vacio porque se usa comúnmente como un valor inicial para acumular información en un programa.
resultado = ""
while True:  # el bloque de código dentro del bucle se ejecutará repetidamente mientras la condición sea verdadera.
    if not resultado:  # es decir que resultado sea: "", None, false, 0
        resultado = input("Ingrese primer dato: ")
        if resultado.lower() == "salir":
            break
        resultado = float(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el siguiente dato: ")
    if n2.lower() == "salir":
        break
    n2 = float(n2)

    if op.lower() == "+":
        resultado += n2
    elif op.lower() == "-":
        resultado -= n2
    elif op.lower() == "*":
        resultado *= n2
    elif op.lower() == "/":
        resultado /= n2
    else:
        print("Operación no valida")
    print(f"El resultado es: {resultado}")