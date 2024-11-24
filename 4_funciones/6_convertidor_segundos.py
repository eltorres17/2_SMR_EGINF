# 9 de octubre de 2024
# Objetivo: Convertir a segundos un total de dias, horas, minutos y segundos introducidos
# por el usuario


# Definicion de funciones
def cdh(variable):
    # Convierte dias en horas
    return variable*24

def chm(variable):
    # Convierte horas en minutos
    return variable*60

def cms(variable):
    # Convierte minutos en segundos
    return variable*60

def cdhms(dias, horas,minutos,segundos):
    # Toma como parametros dias, horas, minutos y segundos y los tranforma a segundos
    return cms(chm(cdh(dias))) + cms(chm(horas)) + cms(minutos) + segundos

# Entrada de datos
num_dia = int(input("Digame un numero de dias: "))
num_hor = int(input("Digame un numero de horas: "))
num_min = int(input("Digame un numero de minutos: "))
num_seg = int(input("Digame un numero de segundos: "))

# Salida de datos
tot = cdhms(num_dia, num_hor,num_min,num_seg)
print(num_dia, "dias,", num_hor, "horas,", num_min, "minutos y", num_seg, 
      "segundos son", tot, "segundos")
