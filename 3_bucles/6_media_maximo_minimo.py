# 9 de octubre de 2024
# Objetivo: Pedir al usuario que introduzca varios numeros y obtener el maximo, el minimo
# y la media de todos ellos

# Entrada de datos
n1 = int(input("¿Cuantos valores va a introducir? "))

# Variables auxiliares
suma = 0

if n1 < 0:
    # Salida de datos
    print("Imposible")
else:
    for i in range(1, n1+1):
        # Entrada de datos
        n2 = int(input("Escribe el numero " + str(i) + ": "))
        suma = suma + n2
        if i == 1:
            min = n2
            max = n2
        else:
            if n2 <= min:
                min = n2
            if n2 >= max:
                max = n2
    # Salida de datos
    print("El numero mas pequeño de los introducidos es", min)
    print("El numero mas grande de los introducidos es", max)
    print("La media de los numeros introducidos es", suma/n1)
   