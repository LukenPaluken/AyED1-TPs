def reemplazar_palabra(
    cadena: str, palabra_a_reemplazar: str, nueva_palabra: str
) -> tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra completa en la cadena por otra palabra.
    """
    palabras = cadena.split()
    cantidad_reemplazos = 0

    for i, palabra in enumerate(palabras):
        if palabra == palabra_a_reemplazar:
            palabras[i] = nueva_palabra
            cantidad_reemplazos += 1

    cadena_modificada = " ".join(palabras)

    return cadena_modificada, cantidad_reemplazos


def main():
    """
    Muestra un menú para interactuar con la funcion.
    """
    cadena_original = "La casa es grande. La casa está en la ciudad."
    palabra_a_reemplazar = "casa"
    nueva_palabra = "hogar"

    cadena_resultante, cantidad_reemplazos = reemplazar_palabra(
        cadena_original, palabra_a_reemplazar, nueva_palabra
    )

    print(f"Cadena original: {cadena_original}")
    print(f"Cadena resultante: {cadena_resultante}")
    print(f"Cantidad de reemplazos: {cantidad_reemplazos}")


main()
