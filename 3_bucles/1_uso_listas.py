# Fecha: 9 de octubre de 2024
# Objetivo: aprender a usar range y listas

# Lista con los parametros de cada uno de los casos que mostrar por pantalla
# La primera posicion indica el inicio, la segunda posicion el final, y la 
# tercera posicion el incremento
parametros =[[0,10,1],[4,11,1], [-6, 0, 1], [-56, -49, 1], [1,18, 2], [-6,11,2], 
             [100, 1100, 100], [10, 3, -1], [-50, -57, -1], [17, 0, -2], [500, -100, -100] ]


for lista in parametros:
    print(list(range(lista[0], lista[1], lista[2])))
