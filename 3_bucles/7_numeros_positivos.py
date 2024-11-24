# 9 de octubre de 2024
# Objetivo: Pedir al usuario que introduzca varios numeros y contar cuantos numeros
# mayores que cero ha introducido

# Entrada de datos
n1 = int(input("Escriba la cantidad de numeros a escribir: "))

# Variables auxiliares
seguir = True # variable de control del bucle while
npos = 0
cont = 0

while seguir:
    if n1 < 0:
        # Entrada de datos
        n1 = int(input("La cantidad debe ser mayor que cero. Intentelo de nuevo: "))
    else:
        # Entrada de datos
        num = int(input("Escriba un numero: "))
        cont = cont + 1
        if num > 0:
            npos = npos + 1
        if cont == n1:
            seguir = False

if cont == 1 and npos == 1:
    # Salida de datos
    print("Ha escrito un numero positivo")
elif npos == 0:
    # Salida de datos
    print("No ha escrito ningun numero positivo")
else:
    # Salida de datos
    print("Ha escrito", cont, "numeros,",npos, "de ellos positivos")
