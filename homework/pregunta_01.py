"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.utils import lectura_datos

def suma(data):
    suma=0
    for line in data:
        suma+=int(line.split("\t")[1])
    return suma


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = lectura_datos()
    sum = suma(data)
    return sum

