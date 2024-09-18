import random as rnd

rnd.seed(1)


def normalizar_numeros(lista: list) -> list:
    """
    Normaliza una lista de números enteros de forma que la suma de los elementos normalizados sea 1.0.
    """
    suma_total = sum(lista)
    if suma_total == 0:
        return [0.0] * len(lista)

    lista_normalizada = [round(float(i) / suma_total, 2) for i in lista]
    return lista_normalizada


def probar_normalizacion():
    """
    Función de prueba para verificar el comportamiento de la función normalizar_numeros.

    Esta función genera varias listas de números enteros y utiliza la función
    normalizar_numeros para normalizarlas. Luego imprime las listas originales y
    las listas normalizadas, así como la suma de los elementos normalizados para verificar
    que suman 1.0.
    """
    ejemplos = [
        [1, 1, 2],
        [5, 10, 15],
        [0, 0, 0],
        [3, 6, 9],
        [],
    ]

    for i, ejemplo in enumerate(ejemplos, 1):
        normalizada = normalizar_numeros(ejemplo)
        suma_normalizada = sum(normalizada) if normalizada else 0
        print(f"Prueba {i}:")
        print(f"Lista original: {ejemplo}")
        print(f"Lista normalizada: {normalizada}")
        print(f"Suma de elementos normalizados: {suma_normalizada}\n")


probar_normalizacion()
