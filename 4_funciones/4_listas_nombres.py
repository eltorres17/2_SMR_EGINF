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


# Entrada de datos
num_lis = int(input("¿Cuantas listas quiere escribir? "))

for i in range(1, num_lis + 1):
    num_pal = int(input("Digame cuantas palabras tiene la lista " + str(i) + ": "))
    lista = introduce_elementos_lista(num_pal) # Invocamos a la funcion
    # Salida de datos
    print("La lista", i, "es:", lista)

