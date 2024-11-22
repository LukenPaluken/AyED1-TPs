def buscarclave(diccionario: dict, valor: int) -> list:
    """
    Busca todas las claves en un diccionario que tienen un valor asociado específico.

    Parameters:
    diccionario (dict): El diccionario donde se buscarán las claves.
    valor (int): El valor que se busca en el diccionario.

    Retorna:
    list: Una lista con las claves que tienen el valor especificado.
    """
    claves = []

    for clave, v in diccionario.items():
        if v == valor:
            claves.append(clave)

    return claves


diccionario_valores = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}

valor_buscado = 10
claves_post = buscarclave(diccionario_valores, valor_buscado)

print(f"Las claves que mapean al valor {valor_buscado} son: {claves_post}")
