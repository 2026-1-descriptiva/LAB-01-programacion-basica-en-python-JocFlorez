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
        valor=int(line.split("\t")[1])
        result.append((clave, valor))
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




def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    data = lectura_datos()
    map_result=mapper(data)
    reducer_result=reducer(map_result)
    ordenar_result=ordenar(reducer_result)
    return ordenar_result
