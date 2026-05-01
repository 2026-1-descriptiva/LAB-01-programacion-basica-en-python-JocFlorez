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
            valor=int(item.split(":")[1])
            dict[clave]=valor
        result.append(dict)
    return result

def reducer(data):
    result={}
    for dict in data:
        for clave, valor in dict.items():
            if clave not in result:
                result[clave]= [valor, valor]
            else:
                if valor < result[clave][0]:
                    result[clave][0]=valor
                if valor > result[clave][1]:
                    result[clave][1]=valor
    return result

def ordenar(result):
    result_ordenado=sorted(result.items())
    return result_ordenado

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    data= lectura_datos()
    map= mapper(data)
    reduce= reducer(map)
    result= ordenar(reduce)
    final_result=[(clave, *max_min) for clave, max_min in result]
    return final_result