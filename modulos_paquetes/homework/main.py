# main.py
#"""
#Archivo principal para importar y utilizar las variables y funciones de config.py.
#"""

# Importar constantes y función desde config.py
#from config import LENGTH, WIDTH, HEIGHT, RADIUS, PI, calculate_area_and_volume

#def main():
#    """
 #   Función principal para calcular y mostrar el área y el volumen de un rectángulo y un cilindro.
 #   """
 #   result = calculate_area_and_volume(LENGTH, WIDTH, HEIGHT, RADIUS, PI)

#     Imprimir los resultados
#    print("Área del rectángulo:", result["area_rect"])
#    print("Volumen del rectángulo:", result["vol_rect"])
#    print("Área del cilindro:", result["area_cyl"])
#    print("Volumen del cilindro:", result["vol_cyl"])

#if __name__ == "__main__":
#    main()
"""este es el script principal"""
import es_mayor_edad
import es_menor
import cuenta_vocales
import es_mayor
es_mayor_edad.funcion_mayor_edad(20)
print(es_mayor.f_es_mayor([4,5,8,9,6,2]))
print(es_menor.f_es_menor([4,8,10,2,3,0]))
print(cuenta_vocales.f_cuenta_vocales("mi mama me mima yo mimo a mi mama"))