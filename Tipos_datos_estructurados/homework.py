# crear una listan de 5 alumnos en cada alumno almacenaremos su nombre apellido edad 
# insertar al final de lista los datos de anthony
# eliminar de la lista los datos de abel 
# buscar y mostrar el alumno en la posicion 4 de la lista

lista_alumnos=[
    {
        "nombre":"abel",
        "apellido":"flores",
        "edad":20
    },{
        "nombre":"ruth",
        "apellido":"dominguez",
        "edad":13
    },{
        "nombre":"jose ma",
        "apellido":"garriazo",
        "edad":80
    },{
        "nombre":"rony",
        "apellido":"cardenas",
        "edad":15
    },{
        "nombre":"miguel",
        "apellido":"hurtado",
        "edad":16
    }
]
# primer problema
#lista_nueva=[
#    {
#        "nombre":"anthony",
#        "apellido":"quispe",
#        "edad":25
#    }
#]
#lista_alumnos.append(lista_nueva)
#print(lista_alumnos)
#segundo problema
#lista_alumnos.pop(0)
#print(lista_alumnos)
# tercer problema
#lista_alumnos.index(3)["nombre","apellido","edad"]
#print(lista_alumnos)
# 2. Crear una lista con tres DICCIONARIO donde tendran los datos de su mascotas nombre, edad, sexo, raza
## dic=[{}]
#tareas
# mostrar la lista con los cuatro diccionario
# editar el 3 registro y cambiar la edad sin modificar la lista original
# mostrar la lista original y luego la lista con el 3 registro modificado

dato_mascota=[
     {"nombre":"pipo",
     "edad":5,
     "sexo":"macho",
     "raza":"pitbull"
     },{"nombre":"blanca",
     "edad":6,
     "sexo":"hembra",
     "raza":"poodle"
     },{"nombre":"bianca",
     "edad":4,
     "sexo":"hembra",
     "raza":"chiwawa"
     },{"nombre":"alma",
     "edad":7,
     "sexo":"hembra",
     "raza":"shi tzu"
     }
     ] 
for diccionario in dato_mascota:
    print(diccionario)
print()
copia_mascotas=dato_mascota.copy()
copia_mascotas[2]["edad"]=7
for copy in copia_mascotas:
    print(copy)

# un empresario de alquiler de autos desea guardar en una base de datos de la informacion de sus vehiculos, proceso que desea automizar con un sistema 
# informatico, las acciones que pueden realizar el empresario son ver las listas de autos que tienen, podra tambien actulizar la lista y agregar un 
# nuevo vehiculo.
#######
# casos de uso
# 1. Ver la lista de autos: El empresario puede consultar la lista completa de autos disponibles en la base de datos.
# 2. Actualizar la lista de autos: El empresario puede modificar la información de un vehículo existente.
# 3. Agregar un nuevo vehículo: El empresario puede añadir nuevos vehículos a la base de datos.
# programacion
lista_autos=[
    {
        "nombre":"supra mk4",
        "marca":"toyota",
        "año":1985
    },{
        "nombre":"GT-R",
        "marca":"nissan",
        "año":1969
    },{
        "nombre":"Golf",
        "marca":"volkswagen",
        "año":1985
    },{
        "nombre":"Q5",
        "marca":"audi",
        "año":1994
    },{
        "nombre":"elantra",
        "marca":"hyundai",
        "año":1990
    }]
lista_autos[3]={"nombre":"G-class","marca":"mercedes-benz","año":1979}
lista_autos.insert(5,{"nombre":"A6","marca":"audi","año":1998})

print(lista_autos)

# crear una lista de los primeros 20 numeros primos haciendo uso de comprension

num_primos=[]
lista_nueva=[num_primos for num_primos in range(2,100)if int(num_primos)%2==+1][:20]
print(lista_nueva)