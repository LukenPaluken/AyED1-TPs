def producto_por_sumas_iterativo(a, b):
    """
    Calcula el producto de dos números enteros usando sumas sucesivas.

    Parameters:
    a (int): Primer número.
    b (int): Segundo número.

    Returns:
    int: Producto de a y b.
    """
    resultado = 0
    negativo = False

    if b < 0:
        b = -b
        negativo = True

    for _ in range(b):
        resultado += a

    return -resultado if negativo else resultado
