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
        dict={}
        for item in line.split("\t")[4].split(","):
            clave=item.split(":")[0]
            valor=1
            dict[clave]=valor
        result.append(dict)
    return result

def reducer(data):
    result={}
    for dict in data:
        for clave, valor in dict.items():
            if clave in result:
                result[clave]+=valor
            else:
                result[clave]=valor
    return result

def ordenar(result):
    result_ordenado=sorted(result.items())
    return result_ordenado



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    data= lectura_datos()
    map= mapper(data)
    reduce= reducer(map)
    result= ordenar(reduce)
    final_result={clave: valor for clave, valor in result}
    return final_result
