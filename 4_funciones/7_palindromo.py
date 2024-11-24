# 9 de octubre de 2024
# Objetivo: Pedir una cadena de texto al usuario y determinar si es o no palindroma

# Definicion de funciones
def elimina_espacios(cadena):
    # Variable auxiliar
    lista = list(cadena)
    for i in lista:
        if i == " ":
            lista.remove(i) # Eliminamos el elemento de la lista
    return lista

def palindromo(cadena):
    # Invocamos a la funcion elimina espacios
    lista = elimina_espacios(cadena)
    # Variables auxiliares
    cont = 0
    es_pal = False
    for i in range(len(lista)):
        if lista[i] == lista[len(lista) - 1 - i]:
            cont = cont + 1
    if cont == len(lista):
        es_pal = True
    return es_pal # Variable booleana que indica si la palabra introducida es palindromo o no


# Entrada de datos
tex = input("Digame algo: ")

if palindromo(tex): #Invocamos a la función
    print(tex, "es palindroma") # Salida de datos
else:
    print(tex, "no es palindroma") # Salida de datos
