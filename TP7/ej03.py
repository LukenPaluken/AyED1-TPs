def suma_numeros_iterativa(n):
    """
    Calcula la suma de los N primeros números naturales de forma iterativa.

    Parameters:
    n (int): Número hasta el cual se calcula la suma (debe ser >= 0).

    Returns:
    int: La suma de los N primeros números naturales.
    """
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a 0.")
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
