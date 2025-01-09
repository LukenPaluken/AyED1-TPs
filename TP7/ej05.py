def resto_por_restas_iterativo(dividendo, divisor):
    """
    Calcula el resto de la división entre dos números enteros usando restas sucesivas.

    Parameters:
    dividendo (int): Número que será dividido.
    divisor (int): Número que divide (debe ser distinto de 0).

    Returns:
    int: El resto de la división.
    """
    if divisor == 0:
        raise ValueError("El divisor no puede ser 0.")
    
    dividendo_absoluto = abs(dividendo)
    divisor_absoluto = abs(divisor)

    while dividendo_absoluto >= divisor_absoluto:
        dividendo_absoluto -= divisor_absoluto

    return dividendo_absoluto if dividendo >= 0 else -dividendo_absoluto
