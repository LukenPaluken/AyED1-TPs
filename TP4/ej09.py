def ordenar_palabras_por_longitud(cadena: str) -> str:
    """
    Recibe una cadena de caracteres con palabras separadas por uno o más espacios.
    Devuelve otra cadena con las palabras ordenadas por su longitud, conservando
    los signos de puntuación.
    """
    palabras_con_puntuacion = cadena.split()
    palabras_limpias = []

    for palabra in palabras_con_puntuacion:
        palabra_sin_puntuacion = "".join(
            [char for char in palabra if char not in [".", ",", ";"]]
        )
        palabras_limpias.append(palabra_sin_puntuacion)

    palabras_ordenadas = sorted(
        palabras_con_puntuacion,
        key=lambda palabra: len(
            "".join([char for char in palabra if char not in [".", ",", ";"]])
        ),
    )

    resultado = " ".join(palabras_ordenadas)

    return resultado


string = input("Ingresar cadena: ")
print(ordenar_palabras_por_longitud(string))
