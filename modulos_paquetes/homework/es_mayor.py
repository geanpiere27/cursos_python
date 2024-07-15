"""funcion para saber la mayor de edad de una lista"""
def f_es_mayor(lista:list):
    """funcion para saber si es menor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n < mayor:
            mayor=n
    return mayor
