# 9 de octubre de 2024
# Objetivo: Pedir al usuario que introduzca varios numeros y contar el cuantos numeros
# pares ha introducido

# Entrada de datos
n1 = int(input("Escriba un numero par: "))

# Variables auxiliares
seguir = True # Variable de control del bucle while
cont = 0

while seguir:
    if n1 % 2 != 0:
        # Entrada de datos
        n1 = int(input(str(n1)+ " no es par. Intentelo de nuevo: "))
    else:
        cont = cont + 1
        # Entrada de datos
        continuar = input("¿Quieres escribir otro numero par? (S/N) ")
        if not(continuar in ('S', 's')):
            seguir = False
        else:
            # Entrada de datos
            n1 = int(input("Escriba un numero par: "))

if cont == 1:
    # Salida de datos
    print("Ha escrito un numero par")
else:
    # Salida de datos
    print("Ha escrito", cont, "numeros pares")