"""La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
módulo math. Escribir un programa que utilice esta función para calcular la raíz 
cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
negativo."""

import math

def calcular_raiz_cuadrada() -> float:
    """
   Solicita al usuario un número positivo y calcula su raíz cuadrada.

    Returns:
        float: La raíz cuadrada del número ingresado si es positivo.

    Raises:
        ValueError: Si el número ingresado es negativo o no es válido.
    """
    try:
        num = int(input("Ingrese un número positivo: "))
        if num < 0:
            raise ValueError("El número debe ser positivo.")
        num_raiz = math.sqrt(num)
        return num_raiz
    except ValueError as e:
        print("Error:", e)

calcular_raiz_cuadrada()
