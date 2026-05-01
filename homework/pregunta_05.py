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
        if clave not in result:
            result[clave]= [valor, valor]
        else:
            if valor > result[clave][0]:
                result[clave][0]=valor
            if valor < result[clave][1]:
                result[clave][1]=valor
    return result

def ordenar(result):
    result_ordenado=sorted(result.items())
    return result_ordenado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data= lectura_datos()
    mapper_result=mapper(data)
    reducer_result=reducer(mapper_result)
    ordenar_result=ordenar(reducer_result)
    final_result=[(clave, *max_min) for clave, max_min in ordenar_result]
    return final_result
