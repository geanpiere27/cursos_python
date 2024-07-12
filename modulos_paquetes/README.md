# Modulos paquetes en python

> Un módulo en Python es un archivo con extensión .py que contiene definiciones y declaraciones de Python, como funciones, clases y variables. Los módulos permiten organizar el código en partes lógicas y reutilizables.

### Creación de un módulo
> Crear un archivo llamado mi_modulo.py:
```python
# mi_modulo.py
def saludar(nombre):
    return f"Hola, {nombre}!"

def despedir(nombre):
    return f"Adiós, {nombre}!"
```
### Utilizar el módulo en otro archivo:
```python
# main.py
import mi_modulo

print(mi_modulo.saludar("Carlos"))
print(mi_modulo.despedir("Carlos"))
```
### Paquetes
Un paquete es una forma de estructurar los módulos en una jerarquía de directorios. Cada directorio en un paquete contiene un archivo especial __`init`__.py (puede estar vacío o con código) que indica a Python que el directorio debe ser tratado como un paquete.

#### Creación de un paquete
1.- Crear una estructura de directorios para el paquete:

```python
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
```
2.- Crear el archivo __init__.py (puede estar vacío o contener código de inicialización):

```python
# mi_paquete/__init__.py
```
3.- Crear los módulos modulo1.py y modulo2.py:

```python
# mi_paquete/modulo1.py
def funcion1():
    return "Función 1 del módulo 1"

# mi_paquete/modulo2.py
def funcion2():
    return "Función 2 del módulo 2"
```
4.- Utilizar el paquete y sus módulos:

```python
# main.py
from mi_paquete import modulo1, modulo2

print(modulo1.funcion1())
print(modulo2.funcion2())
```
#### Beneficios de usar módulos y paquetes
- Reutilización: Permiten reutilizar código en diferentes partes de un proyecto o en proyectos diferentes.
- Mantenibilidad: Facilitan la localización y corrección de errores al dividir el código en partes más pequeñas y manejables.
- Organización: Ayudan a organizar el código de manera lógica y estructurada.
- Namespace: Evitan conflictos de nombres al encapsular las definiciones dentro de módulos y paquetes.

# Averiguar diferencias de modulos y paquetes
> Las diferencias entre módulos y paquetes en Python son fundamentales para entender cómo organizar y estructurar el código de manera eficiente. A continuación se detallan las diferencias clave:

### Módulos

1. **Definición**: Un módulo es un solo archivo `.py` que puede contener funciones, clases y variables.
2. **Tamaño**: Son generalmente más pequeños, ya que se limitan a un solo archivo.
3. **Importación**: Se importan usando la declaración `import` o `from ... import ...`.
4. **Estructura**: Un módulo es una unidad básica de organización en Python y no requiere ninguna estructura especial de directorios.
#### **Ejemplo**:
```python
    # modulo.py
    def saludar(nombre):
        return f"Hola, {nombre}!"

    # main.py
    import modulo

    print(modulo.saludar("Carlos"))
 ```

### Paquetes

1. **Definición**: Un paquete es una colección de módulos organizados en una estructura de directorios. Un paquete siempre contiene un archivo especial `__init__.py`.
2. **Tamaño**: Suelen ser más grandes ya que pueden contener múltiples módulos y subpaquetes.
3. **Importación**: Se importan usando la declaración `import` o `from ... import ...`. La importación puede ser más compleja debido a la jerarquía de directorios.
4. **Estructura**: Un paquete requiere una estructura de directorios específica donde cada subdirectorio que actúa como subpaquete debe contener su propio archivo `__init__.py`.
#### **Ejemplo**:
```plaintext
    mi_paquete/
        __init__.py
        modulo1.py
        modulo2.py
```

```python
    # mi_paquete/modulo1.py
    def funcion1():
        return "Función 1 del módulo 1"

    # mi_paquete/modulo2.py
    def funcion2():
        return "Función 2 del módulo 2"

    # main.py
    from mi_paquete import modulo1, modulo2

    print(modulo1.funcion1())
    print(modulo2.funcion2())
```

> ### `Comparación Directa`

| Característica        | Módulo                          | Paquete                          |
|-----------------------|---------------------------------|----------------------------------|
| Estructura            | Un solo archivo `.py`           | Colección de módulos en directorios |
| Tamaño                | Más pequeño                     | Más grande                       |
| Organización          | Unidad básica de organización   | Colección de módulos organizados |
| Importación           | `import modulo`                 | `import paquete.modulo`          |
| `__init__.py`         | No necesario                    | Necesario en cada directorio de paquete |
| Ejemplo de uso        | `import modulo`                 | `from paquete import modulo`     |

> ##### En resumen, los módulos son archivos únicos que contienen código Python, mientras que los paquetes son una colección de módulos organizados en una jerarquía de directorios. Los paquetes permiten organizar proyectos más grandes y complejos de manera estructurada y lógica.

