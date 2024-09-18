import random as rnd

rnd.seed(1)


def lista_ordenada(lista: list) -> bool:
    """
    Verifica si una lista está ordenada en forma ascendente.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


letras = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
}


letras_valores = list(letras.keys())


lista_ordenada_numeros = [(i + 1) for i in range(10)]
lista_desordenada_numeros = [rnd.randint(1, 10) for _ in range(10)]
lista_ordenada_letras = letras_valores.copy()
lista_desordenada_letras = letras_valores.copy()


rnd.shuffle(lista_desordenada_letras)


def probar_lista_ordenada():
    """
    Función de prueba para verificar el comportamiento de la función lista_ordenada.
    """
    print("Lista ordenada de números:", lista_ordenada_numeros)
    print("Lista desordenada de números:", lista_desordenada_numeros)
    print("Lista ordenada de letras:", lista_ordenada_letras)
    print("Lista desordenada de letras:", lista_desordenada_letras)

    print("\nResultados de la función lista_ordenada:")
    print(f"Lista ordenada de números: {lista_ordenada(lista_ordenada_numeros)}")
    print(f"Lista desordenada de números: {lista_ordenada(lista_desordenada_numeros)}")
    print(f"Lista ordenada de letras: {lista_ordenada(lista_ordenada_letras)}")
    print(f"Lista desordenada de letras: {lista_ordenada(lista_desordenada_letras)}")


probar_lista_ordenada()
