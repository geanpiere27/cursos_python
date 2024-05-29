# tipos de datos ectructurados (TDA -tipos de datos abstractos)
```PYTHON
#lista
#sus valores se pueden actualizar,eliminar
lista=["abel",20,5.2,5.5,False,["texto",.2] ]
#tuplas
#sus valores o elementos no pueden ser modificados o eliminados
tupla=("abel",20,5.2,False,[])
#diccionarios o objetos
# los diccionarios almacenan los datos con clave,valor
diccionario={"nombre":"antonio","edad":15,"sexo":False}
            # clave : # valor
```
-[!TIP]
-** observacion:** que los tipos de datos estructurados pueden almacenar, en su interior otros tipos de datos estructurados
```python
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":20
        "amigos":["no tiene"]
    },{
        "nombre":"ruth",
        "edad":13
        "amigos":["flor,"rocio"]
    },{
        "nombre":"jose ma",
        "edad":80
    },{
        "nombre":"rony"
        "edad":15
    }
]
```
## metodos
### 1. convertir texto a lista 
texto.split(",")
```python
# metodo list
texto="hola"
list(texto)
# =["h","o","l","a"]
# metodo split
texto="hola como estan alumnitos lindos"
texto.split(",")
```
### `.join ` 
 el metodo qiue utilizamos para unir elementos de una lista en un texto 
 ```python
 texto_largo="este es un texto largo chiquitas y chiquitos"
nuevo_texto=texto_largo.split(" ")
print(" ".join(nuevo_texto))
```
### 2. agregar elementos al final de una lista 
```python
# metodo append
# es el metodo que me permite agregar elemento al final de una lista
lista["hola"]
lsita.append("mundo")
print(lista)
#["hola","mundo"]

#metodo insert
# es el metodo que me permite agregar elementos en cualquier ubicacion de mi lista 
lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0,"anthony")
```
### 3. eliminar elementos de una lista
```python
# metodo pop
# es el metodo que elimina el ultimo elemento de una lista es el contrario de append.
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop()

# primera opcion:
# metodo remove
# este metodo elimina por nombre el elemento que coincida dentro de mi lista.
lista_nombres=["edith","ruth","luz"]
lista_nombre.remove("ruth")

# segunda opcion:
# metodo pop 
# al pasarle por pararmetro un indice este lo elimina de la lista.
lista_nombres=["edith","ruth","luz"]
lista_nombre.pop(0)
```
### 4. buscar un elemnto en una lista
``index`` elemento para buscar una palabra en una lista grande
```python
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombre[indice])
# 
pertenencia="edith"in lista_nombre #True False
```
### 5. comaparacion de listas
podemos hacer uso de los operadores de comparacion para comparar listas
**ejem:**
```python
compara=[1,2,3]<[1,2,4]
#1 no por que son iguales en ambas listas
#2 no por que son iguales en ambas listas
#3 evalua que es menor que 4 
#entonces la primera lista es menor que la segunda lista 
print(compara)
#salida
```
### 6. cuidado con las coplas 

### 7. FE de erratas (Actualizar listas)
#### ejemplo 1 modifica el valor de la lista 
```python
lista=[1,3,4,5,6]
copia_lista=lista[0]=2
print(copia_lista)
# [2,3,4,5,6]
# modificando lista con diccionario
alumnos=[
    {
        "nombre":"abel",
        "edad":11 
    },{
        "nombre":"anthony"
        "edad":29
    }]
alumnos[0]["edad"]=30
print(alumnos)
```
#### ejemplo 2 modificacion e lista de un valor
```python
lista=[1,3,4,5,6]
copia_lista=lista[0]=2
print(copia_lista)
# [2,3,4,5,6]
# modificando lista con diccionario
alumnos=[
    {
        "nombre":"abel",
        "edad":11 
    },{
        "nombre":"anthony"
        "edad":29
    }]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
print(alumnos)
```
#### ejemplo 3 aumentar un valor 
```python
lista=[1,3,4,5,6]
copia_lista=lista[0]=2
print(copia_lista)
# [2,3,4,5,6]
# modificando lista con diccionario
alumnos=[
    {
        "nombre":"abel",
        "edad":11 
    },{
        "nombre":"anthony"
        "edad":29
    }]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
# solucion
alumnos[1]["sexo"]="por definir"
print(alumnos)
```