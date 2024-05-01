
### Problema 1: Concatenación de cadenas
#Escribe un programa que solicite al usuario su nombre y su apellido, y luego muestre un saludo completo con ambos nombres.


# Solicitar al usuario su nombre y apellido
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Concatenar los nombres para formar el saludo completo
saludo = "Hola, " + nombre + " " + apellido + "!"

# Mostrar el saludo completo
print(saludo)


### Problema 2: Contar la longitud de una cadena
#Escribe un programa que solicite al usuario una palabra o frase y luego muestre la cantidad de caracteres que contiene.


# Solicitar al usuario una palabra o frase
cadena = input("Ingrese una palabra o frase: ")

# Contar la cantidad de caracteres en la cadena
longitud = len(cadena)

# Mostrar la longitud de la cadena
print("La longitud de la cadena es:", longitud)

### Problema 3: Reverso de una cadena
#Escribe un programa que solicite al usuario una palabra o frase y luego muestre la misma cadena pero al revés.


# Solicitar al usuario una palabra o frase
cadena = input("Ingrese una palabra o frase: ")

# Obtener el reverso de la cadena
reverso = cadena[::-1]

# Mostrar el reverso de la cadena
print("El reverso de la cadena es:", reverso)

