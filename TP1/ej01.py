def ingresar_numeros() -> list:
    """
    Solicita al usuario que ingrese tres números positivos y los almacena en una lista.

    El usuario tiene que ingresar un número válido (entero). Si el usuario ingresa un
    valor no entero, se le pedirá que lo intente de nuevo hasta que ingrese un número válido.
    """
    numeros = []
    for i in range(3):
        while True:
            try:
                num = int(input(f"Ingrese el {i + 1}° número positivo: "))
                numeros.append(num)
                break
            except ValueError:
                print("Ingresar un número válido.")
    return numeros


def verificar_numeros_positivos(numeros: list) -> bool:
    """
    Verifica si todos los números en la lista son positivos.
    """
    for item in numeros:
        if item < 0:
            return False
    return True


def encontrar_mayor_estricto(numeros: list) -> int:
    """
    Determina el mayor número de la lista, si este es único.

    Si el mayor número en la lista aparece más de una vez, se devuelve -1 para indicar que
    no hay un mayor estricto.
    """
    mayor = max(numeros)

    if numeros.count(mayor) > 1:
        return -1
    return mayor


def app() -> None:
    """
    Ejecuta la aplicación principal que solicita números al usuario, verifica que sean positivos,
    y determina si hay un número mayor estricto.

    Si todos los números ingresados son positivos, se verifica si existe un mayor estricto.
    Dependiendo de los resultados, se imprimirá un mensaje adecuado.
    """
    numeros = ingresar_numeros()
    mayor = encontrar_mayor_estricto(numeros)

    if verificar_numeros_positivos(numeros):
        if mayor == -1:
            print("No hay un mayor estricto.")
        else:
            print(f"El número mayor es {mayor}.")
    else:
        print("Por favor, solo ingrese números positivos.")
    return None


app()
