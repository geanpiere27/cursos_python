
### Problema 1: Determinar si un número es positivo, negativo o cero
#Escribe un programa que solicite al usuario un número e imprima si es positivo, negativo o cero.


# Solicitar al usuario un número
numero = float(input("Ingrese un número: "))

# Determinar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

### Problema 2: Determinar si un año es bisiesto
#Escribe un programa que solicite al usuario un año e imprima si es bisiesto o no.


# Solicitar al usuario un año
año = int(input("Ingrese un año: "))

# Determinar si el año es bisiesto
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("El año", año, "es bisiesto.")
else:
    print("El año", año, "no es bisiesto.")


### Problema 3: Calcular el descuento en una tienda
#Escribe un programa que solicite al usuario el monto total de una compra y calcule el descuento aplicado según el siguiente criterio:
#- Si el monto es mayor o igual a $100, se aplica un descuento del 10%.
#- Si el monto es mayor o igual a $50 pero menor a $100, se aplica un descuento del 5%.
#- Si el monto es menor a $50, no se aplica descuento.

# Solicitar al usuario el monto de la compra
monto = float(input("Ingrese el monto total de la compra: "))

# Calcular el descuento según el monto de la compra
if monto >= 100:
    descuento = monto * 0.10
elif monto >= 50:
    descuento = monto * 0.05
else:
    descuento = 0

# Mostrar el monto total con descuento aplicado
monto_total = monto - descuento
print("El monto total con descuento es:", monto_total)

# ejemplos
# ejemplo estructurado
edad:int=int(input("escribe tu edad:"))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")

#almacenar *if* en una variable 
eda:int=int(input("escribe tu nombre:"))
respuesta:str="eres mayor" if edad>=18 else "eres menor"
print(respuesta)

# programa que me imprima las vocales
def imprimir_vocales():
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        print(vocal)

imprimir_vocales()

# otra forma
vocales:str="aeiou"
for n in range(0,5):
    print(vocales[n])
# crear un programa que me muestre los ocho primeros numeros pares

for numero in range(0, 16, 2):
    print(numero)
# otrpo ejemplo
def numeros_pares():
    contador = 0
    numero = 0
    while contador < 8:
        if numero % 2 == 0:
            print(numero)
            contador += 1
        numero += 1

numeros_pares()
#crear un programa que pida al usuario escribir una oracion y mostar por la terminal la cantidad 
# de vocales "a" que tiene esa oracion "solo las a minusculas"

oracion:str= input("Escribe una oración: ")
contador_a:int= 0

for caracter in oracion:
    if caracter == 'a':
        contador_a += 1

print("La cantidad de vocales 'a' en la oración es:", contador_a)

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
