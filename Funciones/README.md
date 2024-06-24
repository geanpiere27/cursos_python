# funciones
## concepto
matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos` y produce un valor denominado `resultado`.
> [!NOTE]
> todos los lenguajes de programacion tienen funciones incorporadas (funciones internas), y funciones creadas por el usuario(`funciones externas`)

En programacion es una funcion es un subprograma,estructura que nos permite agrupar codigo y sus principales objetivos son:
- `NO REPETIR` fragmentos de codigo.
- `REUTILIZAR` el codigo en distintos escenarios.
## Etructura de una funcion
Una funcion viene `definida` por un `nombre`, sus `parametros`() y su valor de `retorno`.
Una vez creada la funcion podremos solicitar su ejecucion `invocando` la funcion por su `nombre`.
## Definir una funcion en python
Para dfinir una funcion en python primero utilizaremos la palabra reservada `def` seguida por el `nombre` de la funcion. A continuacion especificaremos los `parametros` con `( )` si es una funcion sin parametros, `(a)` si es un funcion con parametros, si se tuviera mas de un parametro iran separados por `(,)`, finalizando la linea con `:`, en la siguiente linea sin olvidar el identado, coenzara el `cuerpo` de la funcion(microprograma) que puede contener uno o mas sentencias, finalmente debera `retornar` un resultado con la palabra reservada `return`.
> [!TIP]
> como retorno tambien se puede utilizar la `funcion interna`, `print`, para depuracion de codigo no es recomendable usarlo en produccion. `PRINT` dentro de una funcion es una herramienta que se utiliza para comprobar que una funcion haga el trabajo de manera correcta.

**ejemplo:**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return saludo+saludo_dos
    return f"{saludo},{saludo_dos}"
    # print(f"{saludo},{saludo_dos}")
print (saludo())
# saludo()
```
## Invocar una funcion
para invocra, (o llamar,ejecutar)una funcion solo tendremos que escribir el `nombre` de la funcion por `( )` parentesis. 
```python 
def saludo():
    print("hola")
# invocando la funcion 
saludo()
```
## Retornar un valor
las funciones pueden retornar (o devolver)un valor
```python
def uno():
    return
uno()
```
>[!WARNING]
> No confudir `print()` con `return`, el valor retornado por `return` nos permite usarlo fuera de su contexto, y `print()` solo mostrara el literal por terminal.

 **ejemplo**

en el archivo `lecture.py`
## retorno multiples valores
El secreto es hacerlo ,mediante un tipo de dato estructurado
```python
def varios():
    return2,3,4
varios()
# retorna (2,3,4)
def lista():
    return["hola",45]
#retorna ["hola",45]
def dicc():
    return{"nombre":"jose","edad":45}
dicc()
# retorna ("nombre":"jose","edad":45)
```
## parametros y argumentos
si una funcion no dipusiera de valores de entrada estaria limitada en su actuacion,
es por ello que los `parametros` nos permiten variar los datos que consumen una funcion para obtener distintos resultados.

**ejemplo**

*crear una funcion que recibe un valor numerico y retorna su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
sqrt(4)
```
cuando llamamos a un funcion con `argumentos`, los valores de estos argumentos se copian en los correspondiente `parametros` dentro de la funcion.
```pyhton
def ejm(a,b,c):
    return a+b+c
ejm(4,5,6)
```
### argumentos nominales
En estas aproximacion los argumentos no son copiados en un orden especifico, sino que **se asigna por nombre a cada parametro**. Ello nos permite evitar el problema de conocer o recordar cual es el orden de los parametros en la definicion de la funcion. para utilizarlo, basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f""""
        la cpu es de familia {familia}, 
        con {num_core} cores y con una 
        frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos nominales
build_cpu(num_core=4,familia="intel",frecuencia=2.7)
build_cpu("intel",4,2.7)
```
### argumentos posicionales
los argumentos no son copiados en un orden especifico, en este caso debemos conocer o recordar cual es el orden de los parametros.

***ejemplo***
```python
def build_cpu(familia,num_core,frecuencia):
    print(f""""
        la cpu es de familia {familia}, 
        con {num_core} cores y con una 
        frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos posicionales
build_cpu("intel",4,2.7)
```
### parametros por defecto
Es posible especificar **valores por defecto** en los parametros de una funcion, en el caso de que no se proporcione un valor al argumento en la llamada a la funcion, el parametro correspondiente tomara el valor definido por defecto.
***ejemplo***
```python
def alumnos(nom,apellido,estado="aprobado"):

alumno("ruth","castillo")
alumnos("anthony","crucez","desaprobado")
```
## desempaquetado/empaquetado de argumento(tarea)
El desempaquetado y empaquetado de argumentos se refieren a técnicas para pasar un número variable de argumentos a una función. Aquí te explico cómo funcionan:

1. **args (Desempaquetado de argumentos posicionales)*

   Utilizando *args, puedes pasar un número variable de argumentos posicionales a una función. Dentro de la función, args será una tupla que contiene todos los argumentos posicionales pasados.

   ```python
   def suma(*args):
       return sum(args)

   print(suma(1, 2, 3))  # Devuelve 6
   ```

2. ****kwargs (Desempaquetado de argumentos de palabra clave)**

   Utilizando **kwargs, puedes pasar un número variable de argumentos de palabra clave (key-value pairs) a una función. Dentro de la función, kwargs será un diccionario que contiene todos los argumentos de palabra clave.

   ```python
   def imprimir_info(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   imprimir_info(nombre="Juan", edad=30, ciudad="Madrid")
   # Imprime:
   # nombre: Juan
   # edad: 30
   # ciudad: Madrid
   ```

### Empaquetado de Argumentos

El empaquetado de argumentos es el proceso de pasar una colección (tupla, lista, diccionario) como un conjunto de argumentos posicionales o de palabra clave a una función.

1. **Empaquetado usando * (tupla/lista)**

   Puedes usar * para pasar los elementos de una tupla o lista como argumentos posicionales a una función.

   ```python
   def suma(a, b, c):
       return a + b + c

   numeros = (1, 2, 3)
   print(suma(*numeros))  # Desempaqueta la tupla y devuelve 6
   ```

2. **Empaquetado usando ** (diccionario)**

   Puedes usar ** para pasar los elementos de un diccionario como argumentos de palabra clave a una función.

   ```python
   def imprimir_info(nombre, edad, ciudad):
       print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

   info = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
   imprimir_info(**info)  # Desempaqueta el diccionario
   # Imprime: Nombre: Juan, Edad: 30, Ciudad: Madrid
   ```

### Ejemplos Combinados

Puedes combinar *args y **kwargs en una sola función para aceptar cualquier tipo y cantidad de argumentos.

```python
def funcion_combinada(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos de palabra clave:", kwargs)

funcion_combinada(1, 2, 3, nombre="Juan", edad=30)
# Imprime:
# Argumentos posicionales: (1, 2, 3)
# Argumentos de palabra clave: {'nombre': 'Juan', 'edad': 30}
```
>[!TIP]
>Estas técnicas son muy útiles cuando necesitas escribir funciones que pueden manejar un número variable de argumentos, lo que las hace más flexibles y reutilizables.
### funciones internas de python(tarea)
Las funciones internas (o "built-in functions") de Python son funciones que están disponibles por defecto sin necesidad de importar ningún módulo. Aquí hay una lista de algunas de las funciones internas más comunes en Python:

1. *abs()*: Devuelve el valor absoluto de un número.
   ```python
   abs(-5)  # Devuelve 5
   ```

2. *len()*: Devuelve la longitud (el número de elementos) de un objeto.
   ```python
   len("hello")  # Devuelve 5
   ```

3. *max()*: Devuelve el valor máximo de un iterable o de varios argumentos.
   ```python
   max(1, 2, 3)  # Devuelve 3
   ```

4. *min()*: Devuelve el valor mínimo de un iterable o de varios argumentos.
   ```python
   min(1, 2, 3)  # Devuelve 1
   ```

5. *sum()*: Devuelve la suma de un iterable.
   ``` python
   sum([1, 2, 3])  # Devuelve 6
   ```

6. *sorted()*: Devuelve una lista ordenada de los elementos de un iterable.
   ```python
   sorted([3, 1, 2])  # Devuelve [1, 2, 3]
   ```

7. *type()*: Devuelve el tipo de un objeto.
   ```python
   type(5)  # Devuelve <class 'int'>
   ```

8. *str()*: Convierte un objeto en una cadena de texto.
   ```python
   str(123)  # Devuelve '123'
   ```

9. *int()*: Convierte un objeto en un entero.
   ```python
   int("123")  # Devuelve 123
   ```

10. *float()*: Convierte un objeto en un número de punto flotante.
    ```python
    float("123.45")  # Devuelve 123.45
    ```

11. *bool()*: Convierte un objeto en un valor booleano.
    ```python
    bool(1)  # Devuelve True
    ```

12. *input()*: Permite la entrada del usuario como una cadena de texto.
    ```python
    name = input("Enter your name: ")  # Espera la entrada del usuario
    ```

13. *print()*: Imprime un mensaje en la consola.
    ```python
    print("Hello, world!")  # Imprime 'Hello, world!'
    ```

14. *range()*: Devuelve una secuencia de números.
    ```python
    range(5)  # Devuelve una secuencia de 0 a 4
    ```

15. *enumerate()*: Devuelve un objeto enumerado, que contiene pares de índice y valor.
    ```python
    enumerate(['a', 'b', 'c'])  # Devuelve [(0, 'a'), (1, 'b'), (2, 'c')]
    ```

16. *zip()*: Combina varios iterables en un iterador de tuplas.
    ```python
    zip([1, 2, 3], ['a', 'b', 'c'])  # Devuelve [(1, 'a'), (2, 'b'), (3, 'c')]
    ```
>[!NOTE]
>Estas funciones son solo una parte de las muchas funciones internas que ofrece Python.

## tipos de funciones
### funciones anonimas (funciones lambda)
Las funciones lambda en Python son funciones pequeñas y anónimas (sin nombre). Se usan generalmente para operaciones pequeñas y son muy útiles cuando se utilizan como argumentos para funciones de orden superior.
```python
# Ejemplo de función lambda que suma dos números
sumar = lambda x, y: x + y

# Uso de la función lambda
resultado = sumar(3, 5)
print(resultado)  # Salida: 
```
EJEMPLO 2:
```python
lambda:"hola"
# normal
def saludo():
    return"hola"
```
### funciones closure
Las closures en Python son funciones que recuerdan el entorno en el que fueron creadas. Esto significa que pueden recordar valores de variables que estaban en su ámbito cuando fueron creadas, incluso si esas variables ya no están en el alcance actual.
```python
def crear_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

# Crear una función closure que multiplica por 3
multiplicar_por_3 = crear_multiplicador(3)

# Uso de la función closure
resultado = multiplicar_por_3(10)
print(resultado)  # Salida: 30
```
### funciones callback
Las funciones callback son funciones que se pasan como argumentos a otras funciones y se llaman (o "devuelven la llamada") dentro de la función externa para completar algún tipo de rutina o acción.
```python
def procesar_datos(datos, funcion_callback):
    # Procesa los datos
    resultado = [funcion_callback(dato) for dato in datos]
    return resultado

# Ejemplo de una función callback que duplica el valor
def duplicar(x):
    return x * 2

datos = [1, 2, 3, 4, 5]
resultado = procesar_datos(datos, duplicar)
print(resultado)  # Salida: [2, 4, 6, 8, 10]
```
### porgramacion funcional
La programación funcional es un paradigma de programación donde se usan funciones puras, inmutabilidad y evita cambios de estado y efectos secundarios. Se enfoca en el uso de funciones como valores de primera clase.

>Características Principales:

*Funciones Puras:* Funciones que no tienen efectos secundarios y siempre producen la misma salida para los mismos argumentos.

*Inmutabilidad:* Los datos no pueden ser modificados una vez creados.
Funciones de Orden Superior: Funciones que pueden tomar otras funciones como argumentos o devolverlas como resultados.

*Recursión:* Uso de la recursión en lugar de la iteración tradicional (bucles).
```python
from functools import reduce

# Uso de funciones puras
def sumar(x, y):
    return x + y

# Lista de datos
numeros = [1, 2, 3, 4, 5]

# Uso de map para aplicar una función a todos los elementos de una lista
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # Salida: [2, 4, 6, 8, 10]

# Uso de filter para filtrar elementos en una lista
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]

# Uso de reduce para reducir una lista a un único valor
suma_total = reduce(sumar, numeros)
print(suma_total)  # Salida: 15
```
### Resumen:
`Funciones Lambda:` Pequeñas funciones anónimas usadas para operaciones cortas.

`Funciones Closure:` Funciones que recuerdan el entorno en el que fueron creadas.

`Funciones Callback:` Funciones que se pasan como argumentos y se llaman dentro de otras funciones.

`Programación Funcional:` Paradigma que enfatiza el uso de funciones puras, inmutabilidad y evita efectos secundarios.

### PROGRAMACION FUNCIONAL
la programacion funcional no requiere que sepas como se desarrolla y ejecuta el parametro dela informacion 
```python
lista=[5,7,8,4,1]
def num_minimo(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
#programacion funcional
min(lista)
```
#### averiguar sobre map(),filter(), reduce()
### `map()`
La función `map()` aplica una función a cada elemento de una lista (o de cualquier iterable) y devuelve una lista de los resultados.

**Ejemplo 1:**
Sumar 2 a cada elemento de una lista.

```python
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x + 2, numbers))
print(result)  # Output: [3, 4, 5, 6, 7]
```

**Ejemplo 2:**
Convertir una lista de cadenas de texto a mayúsculas.

```python
words = ['hello', 'world', 'python']
result = list(map(lambda x: x.upper(), words))
print(result)  # Output: ['HELLO', 'WORLD', 'PYTHON']
```

### `filter()`
La función `filter()` crea una lista de elementos para los cuales la función retorna verdadero.

**Ejemplo 1:**
Filtrar números pares de una lista.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)  # Output: [2, 4, 6, 8, 10]
```

**Ejemplo 2:**
Filtrar palabras que tienen más de 5 letras.

```python
words = ['hello', 'world', 'Pythonista', 'AI', 'openai']
result = list(filter(lambda x: len(x) > 5, words))
print(result)  # Output: ['Pythonista', 'openai']
```

### `reduce()`
La función `reduce()` aplica una función de dos argumentos acumulativamente a los elementos de una lista, de tal manera que se reduce la lista a un solo valor.

**Ejemplo 1:**
Calcular el producto de todos los elementos de una lista.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 120
```

**Ejemplo 2:**
Encontrar el mayor número en una lista.

```python
from functools import reduce

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)  # Output: 9
```

### Combinación de `map()`, `filter()` y `reduce()`
A menudo se pueden combinar estas funciones para realizar operaciones complejas de manera concisa.

**Ejemplo:**
Dado una lista de números, sumar los cuadrados de los números pares.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_evens = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
result = reduce(lambda x, y: x + y, squares_of_evens)
print(result)  # Output: 220
```

Estos ejemplos muestran cómo `map()`, `filter()` y `reduce()` pueden ser utilizados para manipular y procesar datos de manera eficiente en Python.