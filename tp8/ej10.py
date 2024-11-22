def eliminarclaves(diccionario: dict, claves: list) -> tuple[dict, int]:
    """
    Elimina del diccionario las claves especificadas en una lista.

    Parameters:
        diccionario (dict): El diccionario del que se eliminarán las claves.
        claves (list): Lista de claves a eliminar del diccionario.

    Returns:
        tuple[dict, int]: Una tupla que contiene:
            - El diccionario modificado.
            - Un número entero que indica la cantidad de claves eliminadas.
    """
    eliminadas = 0
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            eliminadas += 1
    return diccionario, eliminadas

def main():
    """
    Programa principal para probar el comportamiento de la función eliminar_claves.
    """
    diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
    claves_a_eliminar = ["a", "c", "e"]

    print(f"Diccionario inicial: {diccionario}")
    print(f"Claves a eliminar: {claves_a_eliminar}")

    diccionario_modificado, cantidad_eliminada = eliminarclaves(
        diccionario, claves_a_eliminar
    )

    print(f"Diccionario modificado: {diccionario_modificado}")
    print(f"Cantidad de claves eliminadas: {cantidad_eliminada}")

main()
