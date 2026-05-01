"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.utils import lectura_datos

def extraer_mes(data):
    meses=[]
    for line in data:
        fecha=line.split("\t")[2]
        mes=fecha.split("-")[1]
        meses.append(mes)
    return meses

def mapper_mes(meses):
    result=[]
    for mes in meses:
        result.append((mes,1))
    return result

def reducer_mes(meses):
    result={}
    for mes, valor in meses:
        if mes in result:
            result[mes]+=valor
        else:
            result[mes]=valor
    return result

def ordenar_mes(result):
    result_ordenado=sorted(result.items())
    return result_ordenado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    data = lectura_datos()
    meses=extraer_mes(data)
    mapper_mes_result=mapper_mes(meses)
    reducer_mes_result=reducer_mes(mapper_mes_result)
    ordenar_mes_result=ordenar_mes(reducer_mes_result)

    return ordenar_mes_result
