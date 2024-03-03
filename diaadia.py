# FUNCIONES PROPIAS
# def
# PODEMOS USARLAS PARA SIMPLIFICAR A LA HORA DE VOLVER A LLAMARLAS MAS ADELANTE

def funcion_amalia_flor():
    print("La flor más bella de todas")


# despues puede continuar el codigo, bla, bla ,bla
# y de la nada, bam!! llamamos a la funcion: funcion_amalia_saludar
# esta funcion se ejecutará

funcion_amalia_flor()
funcion_amalia_flor()
funcion_amalia_flor()
funcion_amalia_flor()

# FUNCION CON PARAMETROS (VARIABLE PARA SER USADA SOLO DENTRO DE LA FUNCION)


def funcion_amalia_saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "amiga"
    elif (sexo == "hombre"):
        adjetivo = "amigo"
    else:
        adjetivo = "qué tal?"

    print(f"Hola {nombre},{adjetivo}, salimos a pasear a nuestros gatos?")


funcion_amalia_saludar("Amalia", "mujer")
funcion_amalia_saludar("Joaquín", "hombre")
funcion_amalia_saludar("Bel", "N/B")
