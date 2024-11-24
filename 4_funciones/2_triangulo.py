# 9 de octubre de 2024
# Objetivo: Pintar un triangulo de * dada la anchura por el usuario

# Entrada de datos
anc = int(input("Anchura del triangulo: "))

# Forma 1: Dividiendo el problema en pequeñas partes utilizando funciones
def pinta_linea(n):
    for i in range(n):
        # Salida de datos
        print("*", end = " ")
    print()

def pinta_triangulo(lado):
    for i in range(1, lado):
        pinta_linea(i)
    for i in range(lado,0, -1):
        pinta_linea(i)

# Invocamos la funcion 
pinta_triangulo(anc)

print(30*"-") # Separamos las dos formas de hacerlo a la hora de visualizarlo

# Forma 2: Utilizando un doble bucle for donde ira pintando en las posiciones 
# indicadas por nosotros

# Variable auxiliar
posiciones = list(range(anc)) + list(range(anc, 0, -1)) 

for fila in posiciones:
    for columna in range(fila):
        # Salida de datos
        print("*", end =" ")
    print()

