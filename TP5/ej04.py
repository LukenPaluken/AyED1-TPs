"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C."""


def imprimir_numeros(num_inicio: int) -> None:
    """
    Imprime números consecutivos comenzando desde `num_inicio` hasta 100,000.

    Parameters:
        num_inicio (int): Número inicial desde el cual comenzará la impresión en pantalla.

    Returns:
        None

    Exceptions:
        KeyboardInterrupt: Permite al usuario detener la ejecución del programa.
    """
    try:
        while num_inicio <= 100_000:
            print(num_inicio)
            num_inicio += 1
    except KeyboardInterrupt:
        confirmacion = input("Desea frenar el programa? (y/n): ")
        if confirmacion.lower() == "y":
            print("Programa detenido.")
        else:
            print("Continuando...")
            imprimir_numeros(num_inicio)
    return None


imprimir_numeros(1)
