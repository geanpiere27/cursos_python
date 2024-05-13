### CONTROLES DE FLUJO


Los controles de flujo son estructuras utilizadas en programación para controlar el flujo de ejecución de un programa. Permiten tomar decisiones basadas en condiciones específicas y repetir acciones varias veces según ciertas condiciones. Los controles de flujo permiten que un programa ejecute diferentes bloques de código dependiendo de ciertas condiciones y también permiten que un bloque de código se repita varias veces.

Los controles de flujo más comunes en la mayoría de los lenguajes de programación incluyen:

1. **Condicionales (`if`, `elif`, `else`)**: Permiten ejecutar bloques de código si se cumple una condición específica. Se utilizan para tomar decisiones en base a valores booleanos (verdadero o falso).

2. **Bucles (`for`, `while`)**: Permiten repetir bloques de código varias veces. Los bucles `for` se utilizan para iterar sobre una secuencia (como una lista o una cadena), mientras que los bucles `while` se ejecutan mientras una condición específica sea verdadera.

3. **Instrucciones de control (`break`, `continue`, `pass`)**: Permiten modificar el comportamiento de los bucles y las estructuras condicionales. Por ejemplo, `break` se utiliza para salir de un bucle, `continue` se utiliza para pasar a la siguiente iteración de un bucle y `pass` se utiliza como un marcador de posición para un bloque de código vacío.

Estas estructuras de control de flujo son fundamentales para escribir programas que puedan tomar decisiones, repetir tareas y responder dinámicamente a diferentes situaciones durante la ejecución.
> ejemplos
```python
edad:int=int(input("escribe tu edad:"))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")
```
almacenar *if* en una variable 
```python
eda:int=int(input("escribe tu nombre:"))
respuesta:str="eres mayor" if edad>=18 else "eres menor"
print(respuesta)
```

###  `FOR`:
> este codigo imprime los numeros del 1 al 10
```python
for n in range(1.11):
    print(n)
```
`ejemplo:`

 crear un programa que me muestre los ocho primeros numeros pares
```python
for n in range(1,17):
    if n%2==0:
        contador+=1
        print(f"{n} es par numero {contador}")
```
`ejemplo_2:`

crear un programa que pida al usuario escribir una oracion y mostar por la terminal la cantidad de vocales "a" que tiene esa oracion "solo las a minusculas"
```python
oracion:str=input("escribe una oracion:")
contador:int=0
for n in range(0,len(oracion)):
    if oracion[n]=="a":
        contador=contador+1
        #contador+=1
print(f"la cantidad de letras a que es {contador}")
```
**"[]"acede al indice del codigo**

`ejemplo_3:`
```python
for n in "aeiou":
    print(n)

for i,l in enumerate("aeiou"):
    print(f"el indice es {i} y la letra es {l}")
```
