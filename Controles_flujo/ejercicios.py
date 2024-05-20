# crear un programa que pida la cantidad de notas que se debe registrar luego pedira las notas e imprimira el promedio
# Ejemplo de internet

cantidad_notas = int(input("Ingrese la cantidad de notas a registrar: "))
suma_notas = 0
contador = 0

while contador < cantidad_notas:
    suma_notas += float(input(f"Ingrese la nota {contador + 1}: "))
    contador += 1

promedio = suma_notas / cantidad_notas
print(f"El promedio de las {cantidad_notas} notas es: {promedio}")

# crear un programa que me muestre la tabla de multiplicar del 1 al 5

for numero in range(1, 6):
    print(f"Tabla del {numero}")
    for i in range(1, 13):
        print(f"{numero} x {i} = {numero * i}")
    print()

# crear un programa que pida un numero y que muestre y que muestre la tabla de multiplicar de ese numero
numero = input("Introduce un número para mostrar su tabla de multiplicar: ")
if numero.isdigit():
    numero = int(numero)
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Por favor, introduce un número válido.")

#Escribir un programa que pregunte a un usuario su edad y muestre por pantalla si es mayor o no.
edad=int(input("ingrese su edad:"))
if edad >=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
#Escribir un programa que almacene la cadena de carateres contraseña en una variable, pregunte al usuario por la 
#contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
#sin tener en cuenta mayusculas y minusculas.
key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")
#Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese 
#numero hasta cero separados por comas.
numero=int(input("ingrese un numero: "))
resultado=""
for i in range(numero, -1, -1):
    resultado += str(i)
    if i >0:
        resultado += ","
print(resultado)
# crear un programa que me imprima las cinco vocales 
def imprimir_vocales():
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        print(vocal)

imprimir_vocales()

# crear un programa que me muestre los ocho primeros numeros pares

for numero in range(0, 16, 2):
    print(numero)
# forma 2
def numeros_pares():
    contador = 0
    numero = 0
    while contador < 8:
        if numero % 2 == 0:
            print(numero)
            contador += 1
        numero += 1

numeros_pares()
# crear un programa que pida al usuario escribir un texto y me cuente la cantidad de comas y me muestre sus indices
texto = input("Escribe un texto: ")
contador_comas = 0
indices_comas = []

for indice, caracter in enumerate(texto):
    if caracter == ',':
        contador_comas += 1
        indices_comas.append(indice)

print("La cantidad de comas en el texto es:", contador_comas)
print("Los índices de las comas son:", indices_comas)

# ejemplo
texto = input("escribe un texto:")
cantidad_comas=0
indices_comas=[]
for indice in range(len(texto)):
    if texto [indice]==',':
        cantidad_comas +=1
        indices_comas += [indice]
print(f"la cantidad de comas en el texto es:(cantidad_comas)")
print(f"los indices de las comas son:(indices_comas)")

# escribir un programa que le pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
# (desde 1 hasta su edad)
#solucion:
edad=int(input("ingrese su edad:"))
for edad in range(edad+1):
    print(f"su edad es:{edad}") 
#ejemplo:
edad = int(input("Por favor, introduce tu edad: "))
for i in range(1, edad + 1):
    print("Has cumplido", i, "años.")
# crear un programa que me pida el nombre de tres personas y guarde en una variable global la ultima 
# letra de sus nombres. mostrar por pantalla la variable global con las tres ultimas letras del nombre
# de cada persona
# ejemplo:
# abel
# antony
# edith
# salida: lyh
# ejemplo:
# Variable global para almacenar las últimas letras de los nombres
ultimas_letras = []

# Función para obtener y almacenar las últimas letras de los nombres
def obtener_ultimas_letras():
    global ultimas_letras
    for i in range(3):
        nombre = input("Ingrese el nombre de la persona {}: ".format(i+1))
        ultimas_letras.append(nombre[-1])  # Agrega la última letra del nombre a la lista global

# Llamada a la función principal
obtener_ultimas_letras()

# Mostrar las últimas letras de los nombres ingresados
print("Las últimas letras de los nombres son:", ultimas_letras)

# crear un programa que muestre por terminal la siguiente figura:
# a 
# ee
# iii
# oooo
# uuuuu

def imprimir_figura():
    letras = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(letras)):
        print(letras[i] * (i+1) * (i+1))

imprimir_figura()

