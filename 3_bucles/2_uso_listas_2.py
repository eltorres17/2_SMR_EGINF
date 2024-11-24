# Objetivo: crear una lista de numeros consecutivos

# Entrada de datos
n1 = int(input("Escribe un numero entero: "))
n2 = int(input("Escribe otro numero entero: "))

# Identificamos el menor y el mayor de los dos numeros
if n1 <= n2:
    min = n1
    max = n2
else:
    min = n2
    max = n1

# Salida de datos
print(list(range(min + 1, max)))