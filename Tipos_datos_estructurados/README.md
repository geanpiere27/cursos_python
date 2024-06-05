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
>[!TIP]

>** observacion:** que los tipos de datos estructurados pueden almacenar, en su interior otros tipos de datos estructurados
```python
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":20,
        "amigos":["no tiene"]
    },{
        "nombre":"ruth",
        "edad":13,
        "amigos":["flor,"rocio"]
    },{
        "nombre":"jose ma",
        "edad":80
    },{
        "nombre":"rony",
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
# Metodos de python
## numeros
```python
len(154789)
# devuelve la cantiadad de digitos
# 6
```
## texto
```python
len("hola mundo")
# devuelve la cantidad de caracteres
# el espacio cuenta tambien como un caracter
# 10
```
1. *str.lower()*: Convierte todas las letras de la cadena a minúsculas.
   ```python
   "HELLO".lower()  # 'hello'
   ```
2. *str.upper()*: Convierte todas las letras de la cadena a mayúsculas.
   ```python
   "hello".upper()  # 'HELLO'
   ```
3. *str.strip()*: Elimina los espacios en blanco al principio y al final de la cadena.
   ```python
   "  hello  ".strip()  # 'hello'
   ```
4. *str.replace(old, new)*: Reemplaza todas las apariciones de una subcadena por otra.
   ```python
   "hello world".replace("world", "Python")  # 'hello Python'
   ```

5. *str.split(sep=None)*: Divide la cadena en una lista usando un separador específico (por defecto, cualquier espacio en blanco).
   ```python
   "hello world".split()  # ['hello', 'world']
   ```
## listas
```python
len("a","e,"i","o","u")
# devuelve la cantidad de elementos 
# el cuenta tambien como un caracter
# 4
```
1. *list.append(x)*: Añade un elemento al final de la lista.
   ```python
   my_list = [1, 2, 3]
   my_list.append(4)  # [1, 2, 3, 4]
    ```
2. *list.extend(iterable)*: Extiende la lista añadiendo todos los elementos de un iterable.
   ```python
   my_list = [1, 2, 3]
   my_list.extend([4, 5])  # [1, 2, 3, 4, 5]
   ```
3. *list.insert(i, x)*: Inserta un elemento en una posición específica.
   ```python
   my_list = [1, 2, 3]
   my_list.insert(1, 'a')  # [1, 'a', 2, 3]
   ```

4. *list.remove(x)*: Elimina la primera aparición de un valor.
   ```python
   my_list = [1, 2, 3, 2]
   my_list.remove(2)  # [1, 3, 2]
   ```

5. *list.pop([i])*: Elimina y devuelve el elemento en la posición indicada (por defecto, el último).
   ```python
   my_list = [1, 2, 3]
   my_list.pop()  # 3, my_list es ahora [1, 2]
   ```
## tuplas
Las tuplas son inmutables, así que no tienen métodos para modificar su contenido, pero puedes usar métodos comunes para inspeccionarlas:

1. *tuple.count(x)*: Devuelve el número de veces que un valor aparece en la tupla.
   ```python
   my_tuple = (1, 2, 2, 3)
   my_tuple.count(2)  # 2
   ```

2. *tuple.index(x[, start[, end]])*: Devuelve el índice de la primera aparición de un valor.
   ```python
   my_tuple = (1, 2, 3)
   my_tuple.index(2)  # 1
   ```
## diccionario
1. *dict.get(key[, default])*: Devuelve el valor para una clave, o un valor por defecto si la clave no existe.
    ```python
   my_dict = {"a": 1, "b": 2}
   my_dict.get("a")  # 1
   my_dict.get("c", 0)  # 0
    ```

2. *dict.keys()*: Devuelve una vista de todas las claves en el diccionario.
    ```python
   my_dict = {"a": 1, "b": 2}
   my_dict.keys()  # dict_keys(['a', 'b'])
    ```

3. *dict.values()*: Devuelve una vista de todos los valores en el diccionario.
    ```python
   my_dict = {"a": 1, "b": 2}
   my_dict.values()  # dict_values([1, 2])
    ```

4. *dict.items()*: Devuelve una vista de los pares clave-valor en el diccionario.
    ```python
   my_dict = {"a": 1, "b": 2}
   my_dict.items()  # dict_items([('a', 1), ('b', 2)])
    ```

5. *dict.update([other])*: Actualiza el diccionario con los pares clave-valor de otro diccionario u iterable de pares clave-valor.
    ```python
   my_dict = {"a": 1}
   my_dict.update({"b": 2, "c": 3})  # {"a": 1, "b": 2, "c": 3}
    ```

### 8. listas y diccionarios por compresion
es una tecnica pythonica que nos permite crear listas y diccionarios en una sola linea conbinado bucles y decisiones.
>[!NOTE]
> **VLC** value loop condicion
```python
# LISTA POR COMPRENSION
texto="1,4,8,9,6"
nueva_lista=[]
# "n" toma todos los valores de texto
for n in texto .split(","):
    # append agrega algo en la lista
    nueva_lista.append(int(n))
# aplicando la tecnica vlc "valor bucle y condicion"
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",")if int(n)%2==0]
print(nueva_lista)
# DICCIONARIO POR COMPRENSION
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)
# aplicando el vlc
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={amigo:len(amigo)for amigo in lista_amigos}
print(diccionario)
```
