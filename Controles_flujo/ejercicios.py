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
