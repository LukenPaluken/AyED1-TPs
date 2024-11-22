def unir_fichas(ficha_uno: tuple, ficha_dos: tuple) -> bool:
    """
    Determina si dos fichas de dominó pueden unirse.

    Parameters:
        ficha_uno (tuple): Tupla que representa la primera ficha (dos valores enteros entre 0 y 6).
        ficha_dos (tuple): Tupla que representa la segunda ficha (dos valores enteros entre 0 y 6).

    Retorna:
        bool: 
            - True si las fichas comparten al menos un número (pueden unirse), false si no 
            tienen ningún número en común
    """
    return not set(ficha_uno).isdisjoint(set(ficha_dos))

ficha = (3, 4)
ficha2 = (5, 4)

unir_fichas(ficha, ficha2)
