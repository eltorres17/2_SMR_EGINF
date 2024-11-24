# 9 de octubre de 2024
# Objetivo: Contar los numeros negativos introducidos por el usuario

# Entrada de datos
n = int(input("¿Cuanto valores va a introducir? \n"))

# Variables auxiliares
cont = 0

if n < 0:
    # Salida de datos
    print("Imposible")
elif n == 0:
    # Salida de datos
    print("No ha escrito ningun numero negativo")
else:
    for i in range(1, n + 1):
        # Entrada de datos
        nuevo = int(input("Escriba el numero " + str(i) + ": "))
        if nuevo < 0:
            cont = cont + 1

# Salida de datos
print("Ha escrito", cont, "numeros negativos")
