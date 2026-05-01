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
            result[clave]= {valor}
        else:
            result[clave].add(valor)
    return result

def reducer(data):
    result=[]
    for clave, valor in data.items():
        result.append((clave, sorted(valor)))
    return result

def ordenar(result):
    result_ordenado=sorted(result)
    return result_ordenado

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    data = lectura_datos()
    map= mapper(data)       
    reduce= reducer(map)
    result= ordenar(reduce)
    return result