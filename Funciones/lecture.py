# return devuelve valores que podre hacer uso
# crear una funcion que retorne el numero 10 y muestre por terminal
# si es par.
# siempre el valor que retorne mi funcion se utiliza en mas sentencias
# u operaciones hacer uso de return
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es impar")
# "print" solo muestra por terminal
# print solo muestra por terminal
#crear una funcion que me muestre el producto de dos numeros
def productos(a,b):
    return a*b
print(productos(4,5))
# crear una funcion que me retorne una lista de tres numeros 
def lista_numeros():
    return [3,2,1]
# print usaremos cada vez que muestra funcion retorne un mensaje
# crear una funcion que por parametro reciba un nombre y retorne un mensaje de bienvenida con el nombre.
def mensaje(nombre):
    print(f"hola,{nombre},bienvenido al chongo")
# argumento
mensaje("jose")

# crear una funcion que resiva por parametro una lista de numeros y me devuelva el numero menor, mostrar por terminal el valor retornado por la funcion

def numero_menor(lista):
    return min(lista)

# Ejemplo de uso                  
numeros = [5, 2, 9, 1, 6]
menor_numero = numero_menor(numeros)
print("El número menor es:", menor_numero)
# crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debera retornar un diccionario con los datos, luego mostar 
# por terminal el valor de retorno de mi funcion.
def crear_diccionario(nombre, edad):
    return {'nombre': nombre, 'edad': edad}

# Ejemplo de uso
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))

resultado = crear_diccionario(nombre, edad)
print("Resultado:", resultado)
nombre="abel"
edad=19
def persona(nom,edad):
    #return {
    #          "nombre":nom,
    #           "edad":19,
    #}
    return dict(
        nombre=nom,
        edad=edad
    )
print(persona(nombre.edad))