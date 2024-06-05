lista=["abel","anthony","miguel"]
print(lista[1:])#ciba una lista 
diccionario={"nombre":"antonio","edad":15,"sexo":False}
print(diccionario["nombre"])
# ejemplo de split
texto="hola como estan, alumnitos lindos"
texto.split(",")
print()
## ejemplo de lista
texto="hola"
lista_texto=list(texto)
lista_2=list[e for in texto]
print(lista_2)

texto_largo="hola como estan bienvenidos al salon"
nueva_lista=texto_largo.split(" ")
print(nueva_lista)
texto_largo="hola como estan bienvenidos al salon"
nuevo_texto=texto_largo[16:]
nueva_lista=nuevo_texto.split(" ")
print(nueva_lista)
texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split("_")
print(" ".join(nuevo_texto))
# .join 
# el metodo que utilizamos para unir
# elementos de una lista en un texto 
texto_largo="este es un texto largo chiquitas y chiquitos"
nuevo_texto=texto_largo.split(" ")
print(" ".join(nuevo_texto))
## datos estructurados
lista_original=[1,2,3,4]
copia_lista=lista_original
lista_original[-1]=15
print(copia_lista)

## craer un programa que recibe 
lista=[4,76,1,3,6,8,2]
copia_lista=lista.copy()
copia_lista.sort()
print(lista)
print(copia_lista)

texto="1,4,8,9,6"
nueva_lista=[]
# "n" toma todos los valores de texto
for n in texto .split(","):
    # append agrega algo en la lista
    nueva_lista.append(int(n))
# aplicando la tecnica vlc "valor bucle y condicion"
texto="1,4,8,9,6"
nueva_lista=[(n) for n in texto.split(",")]
print(nueva_lista)

# DICCIONARIO POR COMPRENSION
lista_amigos=["abel","anthony","edith","ruth"]
# "_,v" indice valor
# "len" es la longitud
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)
# aplicando el vlc
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={amigo:len(amigo)for amigo in lista_amigos}
print(diccionario)