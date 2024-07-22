# PASOS PARA CREAR ENTORNOS VIRTUALES

- PASO 1
  
  Crear una carpeta en `vs code` para eso hay que instalar open git bash
- PASO 2
  
  Una vez istalado abrir `vs code` con git bash con el:
  
  `code .`
-  PASO 3
  
   Una vez dentro crear la carpeta entornos_virtulescon el codigo:

   >`mkdir "nombre del documento"`

   >`mkdir entornos_virtuales`
- PASO 4

  Una vez creada la carpeta nos vamos a git bash para descargar los paquetes con el codigo siguiente:

  >`python venv "nombre con el quieres descargar"`
  >`python venv .venv`
- PASO 5

  Una vez instalado los paquetes vamos a activar con el cidigo:

  >`nombre_del_entorno\Scripts\activate`
  >`.venv\Scripts\activate`
- PASO 6
  
  despues para actualizar a una version actual utilizamos el codigo:
  > `python -m pip install --upgrade pip`
- PASO 7

  Ahora para instalar aplicaciones utilizamos el codigo:
  >`pip install " nombre_de _aplicacion"`
-PASO 8

  Para guardar tulizamos los codigos en git bash:
  >`git add .`
  >`git commit -m "especificacion"`

