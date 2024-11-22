def contarvocales(palabra: str) -> dict:
    """
    Cuenta cuántas vocales contiene una palabra y la cantidad de cada una.

    Parameters:
        palabra (str): La palabra en la que se contarán las vocales.

    Returns:
        dict: Un diccionario con la cantidad de cada vocal (a, e, i, o, u) en la palabra.
    """
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in palabra.lower():
        if letra in vocales:
            vocales[letra] += 1
    return vocales


def procesar_frase(frase: str) -> None:
    """
    Procesa una frase, contando las vocales en cada palabra e imprimiendo el resultado.

    Parameters:
        frase (str): La frase que contiene las palabras a analizar.
    """
    palabras = frase.split()
    for palabra in palabras:
        resultado_vocales = contarvocales(palabra)
        print(f"Palabra: {palabra} - Vocales: {resultado_vocales}")


def main():
    """
    Programa principal que lee una frase y llama a la función contarvocales para cada palabra.
    """
    frase = input("Ingrese una frase: ")
    procesar_frase(frase)


main()
