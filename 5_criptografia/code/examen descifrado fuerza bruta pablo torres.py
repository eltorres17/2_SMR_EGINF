# Pablo Torres Serván
# 03/12/2024
# Este código es para el descifrado de la frase por fuerza bruta

def descifrado_cesar_fuerza_bruta(cad_cif):

    # Variable auxiliar
    global abc  # La declaración global indica que la variable abc existe fuera de la función
    abc = list("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUWXYZ")  # Lista con los elementos del abecedario español, añadimos las muyusculas para poder ver si pueden estar en eel mensaje o no
    lista_de_claves = []  # Lista para almacenar las cadenas descifradas con cada clave

    # Intentamos todas las posibles claves
    for clv in range(1, len(abc) + 1):
        new_cad = ""  # Cadena vacía donde se irá creando la nueva cadena descifrada

        # Desciframos la cadena con la clave actual
        for i in cad_cif:
            if i in abc:
                if clv > abc.index(i):
                    pos = len(abc) - (clv - abc.index(i))
                else:
                    pos = abc.index(i) - clv
                new_cad += abc[pos]
            else:
                new_cad += " "  # Si no está en el abecedario, se agrega un espacio

        # Almacenamos el mensaje descifrado con la clave actual
        lista_de_claves.append((clv, new_cad))

    # Mostramos todas las opciones de descifrado para que el usuario elija
    for clave, mensaje_descifrado in lista_de_claves:
        print(f"Clave {clave}: {mensaje_descifrado}")

# Parametro funcion
mensaje = "El hombre es el ser que al hablar se queda esperando"

# Llamamos a la función con el mensaje cifrado
descifrado_cesar_fuerza_bruta(mensaje)