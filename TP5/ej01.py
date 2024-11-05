def ingresar_numero_natural() -> int:
    """
    Solicita al usuario que ingrese un número natural (entero mayor que 0).

    Returns:
        int: El número natural ingresado por el usuario.

    Raises:
        ValueError: Si el valor ingresado no es un número entero o es menor o igual a 0.
        Exception: Captura cualquier otro error inesperado durante la ejecución.
    """
    while True:
        try:
            num = int(input("Ingrese un numero natural: "))
            if num <= 0:
                raise ValueError("El numero debe ser mayor a 0.")
            return num
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


numero = ingresar_numero_natural()
print(f"Numero natural ingresado: {numero}")
