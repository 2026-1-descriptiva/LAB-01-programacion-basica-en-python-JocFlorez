"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.utils import lectura_datos

def mapper(data):
    result={}
    for line in data:
        clave=int(line.split("\t")[1])
        valor=line.split("\t")[0]
        if clave not in result:
            result[clave]= [valor]
        else:
            result[clave].append(valor)
    return result

def reducer(data):
    result=[]
    for clave, valor in data.items():
        result.append((clave, valor))
    return result

def ordenar(result):
    result_ordenado=sorted(result)
    return result_ordenado

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    data = lectura_datos()
    map= mapper(data)       
    reduce= reducer(map)
    result= ordenar(reduce)
    return result
