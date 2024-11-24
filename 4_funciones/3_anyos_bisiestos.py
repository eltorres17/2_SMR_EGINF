# 9 de octubre de 2024
# Objetivo: Calcular cuantos años bisiestos hay entre dos años introducidos por el usuario

# Definicion de funciones
def es_bisiesto(variable):
    # Algoritmo para identificar años bisiestos
    if variable % 400 == 0:
        salida = True
    elif variable % 4 == 0 and variable % 100 != 0:
        salida = True
    else:
        salida = False

    return salida # Devuelve una variable booleana

def introduce_año(variable):
    # Entrada de datos
    anyo = int(input("Escribe otro año posterior a " + str(variable) + ": "))
    # Variable auxiliar
    seguir = True # Variable de control del bucle while
    while seguir:
        if anyo <= variable:
            texto = str(anyo) + " no es mayor que " + str(variable) + ". Intentelo de nuevo. "
            anyo = int(input(texto))
        else:
            seguir = False

    return anyo # Devuelve un año mayor que la variable anyo1

# Entrada de datos
anyo1 = int(input("Escriba un año: "))
anyo2 = introduce_año(anyo1)

# Variables auxiliares
num_any = 0
num_any_bis = 0

# Comprobamos entre el rango de años cuales son bisiestos
for i in range(anyo1, anyo2 + 1):
    num_any = num_any + 1
    if es_bisiesto(i): # Invocamos a la funcion
        num_any_bis = num_any_bis + 1

# Salida de datos
print("De", anyo1, "hasta", anyo2, "hay", num_any, "años,", num_any_bis, "de ellos bisiestos")