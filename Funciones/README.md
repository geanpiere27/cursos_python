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
# retorno ("nombre":"jose","edad":45)
```