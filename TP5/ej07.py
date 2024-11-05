import random as rn

def generar_numero_random() -> int:
    """
    Genera un número aleatorio entre 1 y 500.

    Returns:
        int: Número entero aleatorio entre 1 y 500.
    """
    return rn.randint(1, 500)


def juego() -> None:
    """
    Inicia un juego donde el usuario intenta adivinar un número aleatorio entre 1 y 500.
    
    Returns:
        None
    """
    contador = 0
    numero_random = generar_numero_random()
    while True:
        try:
            numero_usuario = int(input("Ingrese un número entre 1 y 500: "))
            if numero_usuario < 1 or numero_usuario > 500:
                contador += 1
                raise ValueError("El número debe estar entre 1 y 500.")

            contador += 1
            if numero_usuario > numero_random:
                print("El número ingresado es mayor que el número a adivinar.")
            elif numero_usuario < numero_random:
                print("El número ingresado es menor que el número a adivinar.")
            else:
                print(f"¡Número adivinado en {contador} intentos!")
                break
        except ValueError as e:
            contador += 1
            print(f"{e} Inténtelo de nuevo.")

juego()
