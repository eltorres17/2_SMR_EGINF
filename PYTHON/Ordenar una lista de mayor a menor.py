def ordenar_lista(lista):
   
    n = len(lista)
    
    for i in range(n):
        
        for j in range(0, n - i - 1):
           
            if lista[j] < lista[j + 1]:
               
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    
    return lista


numeros = input("Introduce una lista de números separados por comas: ")

lista_numeros = [int(num) for num in numeros.split(",")]


lista_ordenada = ordenar_lista(lista_numeros)


print("Lista ordenada de mayor a menor:", lista_ordenada)