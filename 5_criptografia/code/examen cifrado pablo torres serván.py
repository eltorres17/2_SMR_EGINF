# Pablo Torres Serván
# 03/12/2024
# Este código es para el descifrado de la frase desde el método cifrado cesar

def descifrado_cesar(cad_cif, clv):
    # Entrada: La cadena original cifrada (criptograma) y la clave del algoritmo
    # Salida: mensaje descifrado con la clave de entrada

    # Variable auxiliar
    global abc # La declaracion global indica que la variable abc existe fuera de la función
    abc = list("abcdefghijklmnñopqrstuvwxyz") # Lista con los elementos del abecedario
    global abc1
    cad_cif = cad_cif.lower()
    abc1 = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    new_cad = "" # Cadena vacía donde se irá creando la nueva cadena descifrada
    if clv >= len(abc1):
        clv = clv % len(abc1)
    if clv >= len(abc):
        clv = clv % len(abc)
    
        

    # En este código he añadido en el abecedario la letra "ñ" debido a que se usa el abecedario español y se puede observar el mansaje más claro,
    # Lo he deducido ya que si el código la clave es +5 podemos observar que la letra "k" se cambia por la letra "l" al ser una letra más se suma.

    # Desciframos la cadena cambiando las posiciones
    for i in cad_cif:
        if i in abc:
            if i in abc1:
                if clv > abc.index(i):
                    pos = len(abc) - (clv - abc.index(i))
                if clv > abc1.index(i):
                    pos = len(abc1) - (clv - abc1.index(i))
            if i in abc1:
                if clv > abc1.index(i):
                    pos = len(abc1) - (clv - abc1.index)
            else:
                pos = abc.index(i) + clv        
            new_cad += abc[pos]

        else:
            new_cad += " "

    return new_cad

# Parametro funcion
mensaje = "El hombre es el ser que al hablar se queda esperando"
clave = 5


#Llamo a la funcion
print(descifrado_cesar(mensaje,clave))