
### Problema 1: Comparación de números
#Escribe un programa que solicite al usuario dos números y determine si el primer número es mayor, menor o igual al segundo número.


# Solicitar al usuario dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Comparar los números
if num1 > num2:
    print(num1, "es mayor que", num2)
elif num1 < num2:
    print(num1, "es menor que", num2)
else:
    print(num1, "es igual a", num2)


### Problema 2: Verificar si un número es par o impar
#Escribe un programa que solicite al usuario un número y determine si es par o impar.


# Solicitar al usuario un número
num = int(input("Ingrese un número: "))

# Verificar si el número es par o impar
if num % 2 == 0:
    print(num, "es un número par")
else:
    print(num, "es un número impar")


### Problema 3: Comparación de strings
#Escribe un programa que solicite al usuario dos palabras y determine si son iguales o diferentes.


# Solicitar al usuario dos palabras
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

# Comparar las palabras
if palabra1 == palabra2:
    print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")


