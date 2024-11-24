# 9 de octubre de 2024
# Objetivo: Pedir al usuario dos numeros positivos y sumar el rango de valores 
# enteros entre ellos

# Entrada de datos
n1 = int(input("Escribe un numero positivo: "))

# Variables auxiliares
suma = 0

if n1 < 0:
    # Salida de datos
    print("Le he pedido un numero positivo")
else:
    # Entrada de datos
    n2 = int(input("Escribe un numero mayor que " + str(n1) + ": "))
    if n2 <= n1:
        # Salida de datos
        print("Le he pedido un numero entero mayor que", n1)
    else:
        for n in range(n1, n2 + 1):
            suma = suma + n
        # Salida de datos
        print("La suma desde", n1, "hasta", n2, "es", suma)