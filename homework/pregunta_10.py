"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.utils import lectura_datos

def mapper_interno(data):
    result = []
    for line in data:
        letra = line.split("\t")[0]
        col4_count = len(line.split("\t")[3].split(","))
        col5_count = len(line.split("\t")[4].split(","))
        result.append((letra, col4_count, col5_count))
    return result

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    data = lectura_datos()
    result = mapper_interno(data)
    return result
