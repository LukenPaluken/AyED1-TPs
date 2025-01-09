"""Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal"""

def binario_a_decimal(binario, exponente=0) -> int:
    """
    Convierte un número binario a base decimal usando recursividad.
    
    Parameters:
    binario (int): Número binario a convertir.
    exponente (int): Exponente inicial para calcular las potencias de 2 (interno para la recursión).
    
    Returns:
    int: Valor decimal equivalente al número binario.
    """
    if binario == 0:
        return 0
    else:
        digito = binario % 10
        return digito * (2 ** exponente) + binario_a_decimal(binario // 10, exponente + 1)