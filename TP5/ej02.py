def sumar_cadenas(cadena_uno: str, cadena_dos: str) -> float:
    """
    Suma dos cadenas de caracteres que representan números reales.

    Parameters:
        cadena1 (str): Primera cadena con un número real.
        cadena2 (str): Segunda cadena con un número real.

    Returns:
        float: La suma de los dos números reales o -1 si alguna conversión falla.
    """
    while True:
        try:
            num_uno = float(cadena_uno)
            num_dos = float(cadena_dos)
            return num_uno + num_dos
        except ValueError:
            return -1


cadena_uno = input("Ingrese la primer secuencia de numeros: ")
cadena_dos = input("Ingrese la segunda secuencia de numeros: ")
resultado = sumar_cadenas(cadena_uno, cadena_dos)
print(f"Resultado: {resultado}")
