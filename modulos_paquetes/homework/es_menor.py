"""funcion para saber la menor edad de una lista"""
def f_es_menor(lista:list):
    """funcion para saber si es menor de una lista"""
    menor=lista[0]
    for n in lista:
        if n < menor:
            menor=n
    return menor
