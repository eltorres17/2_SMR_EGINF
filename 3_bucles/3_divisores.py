# 9 de octubre de 2024
# Objetivo: Mostrar los divisores de un numero

# Entrada de datos
n = int(input("Introduce un numero: "))

# Variables auxiliares
divisores = []

if n > 0:
    for i in range(1,n + 1):
        if n % i == 0:
            divisores.append(i)
    # Salida de datos
    print("Los divisores de ", n, "son", divisores)
else:
    # Salida de datos
    print("Tiene que ser mayor de cero")


