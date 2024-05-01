
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


