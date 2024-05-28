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
indice=lista_alumnos.index(3)
print(lista_alumnos[indice])
pertenencia=3 in lista_alumnos