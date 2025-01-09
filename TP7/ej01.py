def contar_cantidad_de_digitos(num: int) -> int:
    """
    Función recursiva que devuelve la cantidad de dígitos de un número entero positivo o negativo.
    
    Parameters:
        numero (int): El número entero cuya cantidad de dígitos se desea calcular.

    Returns:
        int: La cantidad de dígitos en el número.
    """
    if abs(num) < 10:
        return 1
    else:
        return 1 + contar_cantidad_de_digitos(num // 10)
