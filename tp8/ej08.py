def generar_diccionario() -> dict:
    """
    Genera un diccionario donde las claves son números enteros del 1 al 20,
    y los valores son los cuadrados de esas claves.

    Returns:
        dict: Diccionario con pares clave-valor, donde las claves son números
              del 1 al 20, y los valores son los cuadrados de dichas claves.
    """
    return {clave:clave**2 for clave in range(1,21)}

generar_diccionario()