"""Escribir una función filtrar_palabras() que reciba una cadena de caracteres conte
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten
gan N o más caracteres de la cadena original. Escribir también un programa para 
verificar el comportamiento de la misma. Hacer tres versiones de la función, para 
cada uno de los siguientes casos:"""


def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """
    Devuelve una cadena con las palabras de la frase que tienen N o más caracteres, usando ciclos normales.
    """
    palabras = frase.split()
    resultado = []

    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)

    return " ".join(resultado)


def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """
    Devuelve una cadena con las palabras de la frase que tienen N o más caracteres, usando listas por comprensión.
    """
    return " ".join([palabra for palabra in frase.split() if len(palabra) >= n])


def filtrar_palabras_filter(frase: str, n: int) -> str:
    """
    Devuelve una cadena con las palabras de la frase que tienen N o más caracteres, usando la función filter.
    """
    return " ".join(filter(lambda palabra: len(palabra) >= n, frase.split()))


string = "Esto es un string super duper largo que sirve para testear"

filtrar_palabras_ciclos(string, 5)
filtrar_palabras_comprension(string, 5)
filtrar_palabras_filter(string, 5)
