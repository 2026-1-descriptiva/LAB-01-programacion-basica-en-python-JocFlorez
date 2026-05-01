"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.utils import lectura_datos

def mapper(data):
    result=[]
    for line in data:
        for items in line.split("\t")[3].split(","):
            clave=items
            result.append((clave, int(line.split("\t")[1])))
    return result

def reducer(data):
    result={}
    for clave, valor in data:
        if clave in result:
            result[clave]+=valor
        else:
            result[clave]=valor
    return result

def ordenar(result):
    result_ordenado=sorted(result.items())
    return dict(result_ordenado)


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    data = lectura_datos()
    map_result=mapper(data)
    reducer_result=reducer(map_result)
    ordenar_result=ordenar(reducer_result)
    return ordenar_result
