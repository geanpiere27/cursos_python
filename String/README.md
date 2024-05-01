### STRING


Un string (cadena de caracteres) es una secuencia de caracteres Unicode encerrados entre comillas simples (`'`) o comillas dobles (`"`). Los strings son utilizados para representar texto y son uno de los tipos de datos más comunes en Python. Aquí tienes algunos ejemplos de strings en Python:

```python
mensaje = 'Hola, mundo!'
nombre = "Juan"
dirección = "Calle del Sol, 123"
```

En los ejemplos anteriores, `'Hola, mundo!'`, `"Juan"`, y `"Calle del Sol, 123"` son strings. Puedes utilizar comillas simples o dobles para definir strings, pero debes ser consistente dentro de tu código.

Los strings pueden contener cualquier carácter Unicode, incluyendo letras, números, espacios, signos de puntuación y caracteres especiales. También pueden ser vacíos, es decir, no contener ningún carácter.

Los strings en Python son inmutables, lo que significa que una vez que se crea un string, no se puede modificar. Sin embargo, puedes crear nuevos strings a partir de strings existentes mediante operaciones como la concatenación y la división.

```python
# Concatenación de strings
saludo = "Hola"
nombre = "Juan"
mensaje = saludo + ", " + nombre  # resultado: "Hola, Juan"

# División de strings
mensaje = "Hola, mundo!"
partes = mensaje.split(",")  # resultado: ['Hola', ' mundo!']
```

Los strings en Python son objetos de primera clase, lo que significa que tienen métodos y funciones asociadas que puedes utilizar para realizar diversas operaciones, como la búsqueda de subcadenas, la conversión de mayúsculas y minúsculas, la eliminación de espacios en blanco, etc.

```python
mensaje = "Hola, mundo!"
longitud = len(mensaje)  # longitud del string
mayusculas = mensaje.upper()  # convertir a mayúsculas
minusculas = mensaje.lower()  # convertir a minúsculas
```

En resumen, en Python, un string es una secuencia de caracteres Unicode que se utiliza para representar texto. Los strings son inmutables y pueden ser definidos utilizando comillas simples o dobles. Se pueden realizar diversas operaciones y manipulaciones de strings utilizando los métodos y funciones incorporados en Python.