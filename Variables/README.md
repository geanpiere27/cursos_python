###   VARIABLES


Una variable es un contenedor que almacena datos que pueden ser modificados durante la ejecución del programa. Las variables en Python son etiquetas que se asignan a ubicaciones de memoria donde se almacenan los valores de los datos. Cada variable tiene un nombre único que se utiliza para hacer referencia a ella y acceder al valor que contiene.

Aquí hay algunas características importantes sobre las variables en Python:

1. **Asignación dinámica**: En Python, no es necesario declarar el tipo de una variable antes de usarla. El tipo de datos de una variable se determina automáticamente según el valor que se le asigna.

2. **Nombres de variables**: Los nombres de variables en Python pueden contener letras, números y guiones bajos, pero deben comenzar con una letra o un guion bajo. Además, Python distingue entre mayúsculas y minúsculas en los nombres de las variables.

3. **Tipos de datos**: Una variable puede contener diferentes tipos de datos, como enteros, flotantes, cadenas, listas, diccionarios, conjuntos, etc.

4. **Reasignación de variables**: Puedes cambiar el valor de una variable simplemente asignándole un nuevo valor. Esto es útil para actualizar o modificar datos durante la ejecución del programa.

5. **Ámbito de las variables**: El ámbito de una variable en Python se refiere a la parte del programa donde la variable es accesible. Las variables pueden tener ámbito global (accesible en todo el programa) o ámbito local (accesible solo dentro de una función o bloque de código específico).

6. **Convenciones de nombres**: Existen convenciones de nombres comunes en Python, como usar nombres descriptivos y significativos para las variables (por ejemplo, `nombre`, `edad`, `lista_de_nombres`, etc.), evitar nombres de una sola letra, y utilizar snake_case para nombres de variables compuestas por varias palabras (por ejemplo, `mi_variable`, `otra_variable`, etc.).

Aquí hay un ejemplo de cómo se utilizan las variables en Python:

```python
# Asignación de valores a variables
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

# Acceso a los valores de las variables
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?", es_estudiante)

# Reasignación de variables
edad = 26
print("Nueva edad:", edad)

# Operaciones con variables
altura += 0.1
print("Altura después de aumentar:", altura)
```

En resumen, las variables en Python son contenedores que se utilizan para almacenar datos y acceder a ellos durante la ejecución del programa. Son fundamentales para trabajar con datos y realizar operaciones en Python.