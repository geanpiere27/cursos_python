

### Problema 1: Calculadora simple
#Escribe un programa que solicite al usuario dos números y realice las siguientes operaciones con ellos: suma, resta, multiplicación, división y potencia.


# Solicitar al usuario dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
potencia = num1 ** num2

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Potencia:", potencia)

### Problema 2: Calcular el área de un rectángulo
#Escribe un programa que solicite al usuario la longitud y el ancho de un rectángulo y calcule su área.


# Solicitar al usuario la longitud y el ancho del rectángulo
longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Calcular el área del rectángulo
area = longitud * ancho

# Mostrar el resultado
print("El área del rectángulo es:", area)


### Problema 3: Conversión de temperaturas
#Escribe un programa que solicite al usuario una temperatura en grados Celsius y la convierta a grados Fahrenheit.


# Solicitar al usuario la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir la temperatura a grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print("La temperatura en grados Fahrenheit es:", fahrenheit)
