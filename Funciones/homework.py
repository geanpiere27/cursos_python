# crear una funcion que reciba por argumento n numeros y retorne una lista con los numeros

def crear_lista(*numeros):
    return list(numeros)

# Ejemplo de uso
resultado = crear_lista(1, 2, 3, 4, 5)
print(resultado)  # Salida: [1, 2, 3, 4, 5]
def num_pares(*args):
    lista_pares=[]
    for n in args:
        if n%2==0
            lista_pares.append(n)
    return lista_pares
# por compresion
        #return [n for n in args if n%2==0]
print(num_pares(8,5,4,7,9,25,4,7,12))
# crear tres funciones para los siguientes casos
#calcular el numero menor
#calcular el numero mayor
#calcular la suma de todos los numeros 
#se le pasara por argumento nn numeros
def min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor
def max(*args):
    mayor=args[0]
    for n in args:
        if n<mayor:
            mayor=n
    return mayor
def sum(*args):
    sujma=0
    for n in args:
        suma+=n
    return suma 
valores=4,5,3,2,1
print(min(*valores))
print(max(*valores))
print(sum(*valores))