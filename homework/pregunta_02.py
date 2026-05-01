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
        clave=line.split("\t")[0]
        result.append((clave, 1))
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
    return result_ordenado




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    data = lectura_datos()
    map_result=mapper(data)
    reducer_result=reducer(map_result)
    ordenar_result=ordenar(reducer_result)
    return ordenar_result
