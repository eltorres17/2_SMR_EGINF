# 9 de octubre de 2024
# Objetivo: Pintar un cuadrado con * de altura y anchura dados por el usuario

# Entrada de datos
anc = int(input("Anchura del rectangulo: "))
alt = int(input("Altura del rectangulo: "))

# Forma 1: Definiendo una función que nos permite pintar lineas de astericos de una determinada de anchura
def pintar_linea(n):
    for variable in range(n):
        # Salida de datos
        print("*", end = " ")
    print()

# Pintamos tantas lineas como nos indique la altura del rectangulo
for n in range(alt):
    # Invocamos la funcion
    pintar_linea(anc)

print(30*"-") # Separamos las dos formas de hacerlo a la hora de visualizarlo

# Forma 2: Utilizamos un doble bucle for, uno exterior que indicará la fila que hay que pintar,
# y uno interior que indicará la columna exacta que hay que pintar
for fila in range(alt):
    for columna in range(anc):
        # Salida de datos
        print("*", end =" ")
    print()