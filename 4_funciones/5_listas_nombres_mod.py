# 9 de octubre de 2024
# Objetivo: Generador de listas con las palabras introducidas por el usuario


# Definicion de funciones
def introduce_elementos_lista(num_ele):
    # Variable auxiliar
    lis = [] # Lista que devolveremos con las palabras introducidas por el usuario
    for i in range(1, num_ele + 1):
        # Entrada de datos
        nom = input("Digame la palabra " + str(i) + ": ")
        lis.append(nom)
    return lis

def generador_listas(variable):
    lis = [] # Crearemos una lista de listas
    for i in range(1, variable + 1):
        num_pal = int(input("Digame cuantas palabras tiene la lista " + str(i) + ": "))
        lista = introduce_elementos_lista(num_pal) # Invocamos a la funcion
        lis.append(lista)
    return lis
        

# Entrada de datos
num_lis = int(input("¿Cuantas listas quiere escribir? "))

# Introducimos en una lista de listas todos los valores introducidos por el usuario
listas = generador_listas(num_lis) # Invocamos la funcion
for i in range(len(listas)):
    # Salida de datos
    print("La lista", i + 1, "es:", listas[i])

    


