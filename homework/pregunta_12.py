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
        valor=0
        clave=line.split("\t")[0]
        for items in line.split("\t")[4].split(","):
            valor_interno=int(items.split(":")[1])
            valor+=valor_interno
        if clave not in result:
            result[clave]=valor
        else:
            result[clave]+=valor
    return result

def reducer(data):
    result={}
    for clave, valor in data.items():
        if clave not in result:
            result[clave]=valor
        else:
            result[clave]+=valor
    return result

def ordenar(result):
    result_ordenado=sorted(result.items())
    return dict(result_ordenado)

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    data = lectura_datos()
    map= mapper(data)       
    reduce= reducer(map)
    result= ordenar(reduce)
    return result
