import re

def procesar_frase(frase: str) -> str:
    """
    Procesa una frase para eliminar palabras repetidas y devuelve las palabras únicas ordenadas por longitud.

    Parameters:
        frase (str): La frase ingresada por el usuario, que puede contener palabras repetidas y signos de puntuación.

    Retorna:
        str: Una cadena de caracteres con palabras únicas de la frase, ordenadas por longitud y separadas por espacios.
    """

    sin_signos = re.sub(r'[^\w\s]', '', frase)
    palabras_unicas = set(sin_signos.split())
    return ' '.join(sorted(palabras_unicas, key=len))

frase_usuario = input("Ingrese una frase: ")

print(procesar_frase(frase_usuario))
