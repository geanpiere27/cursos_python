# config.py
"""
Archivo de configuración que contiene variables y funciones para cálculos geométricos.
"""

# Constantes
LENGTH = 10
WIDTH = 5
HEIGHT = 15
RADIUS = 7
PI = 3.14159

def calculate_area_and_volume(length, width, height, radius, pi):
    """
    Calcula el área y el volumen de un rectángulo y un cilindro.

    Args:
        length (float): Longitud del rectángulo.
        width (float): Ancho del rectángulo.
        height (float): Altura del rectángulo/cilindro.
        radius (float): Radio del cilindro.
        pi (float): Valor de π (pi).

    Returns:
        dict: Diccionario con el área y el volumen del rectángulo y el cilindro.
    """
    area_rect = length * width
    vol_rect = length * width * height
    area_cyl = 2 * pi * radius * (radius + height)
    vol_cyl = pi * radius**2 * height
    return {
        "area_rect": area_rect,
        "vol_rect": vol_rect,
        "area_cyl": area_cyl,
        "vol_cyl": vol_cyl
    }
