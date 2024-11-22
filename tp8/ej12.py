def incrementar_precio(diccionario: dict, producto: str, porcentaje: float) -> dict:
    """
    Incrementa el precio de un producto en un diccionario según un porcentaje.

    Parameters:
        diccionario (dict): El diccionario con los productos y sus precios.
        producto (str): El producto cuyo precio se incrementará.
        porcentaje (float): El porcentaje en el que se incrementará el precio.

    Returns:
        dict: El diccionario actualizado con el nuevo precio del producto.
    """
    if producto in diccionario:
        diccionario[producto] *= 1 + porcentaje / 100
    return diccionario


def obtener_item_mas_costoso(diccionario: dict) -> str:
    """
    Encuentra el ítem más costoso en el diccionario de precios.

    Parameters:
        diccionario (dict): El diccionario con los productos y sus precios.

    Returns:
        str: El nombre del ítem más costoso.
    """
    max_producto = max(diccionario, key=diccionario.get)
    return max_producto


def imprimir_lista_precios(diccionario: dict) -> None:
    """
    Imprime el listado de productos y sus precios.

    Parameters:
        diccionario (dict): El diccionario con los productos y sus precios.
    """
    print("Listado de precios:")
    for producto, precio in diccionario.items():
        print(f"{producto}: ${precio:.2f}")


def main():
    """
    Programa principal que gestiona los precios, incrementa el precio de los cuadernos,
    imprime la lista de precios y muestra el producto más costoso.
    """
    precios = {
        "cuaderno": 50.0,
        "lapiz": 15.0,
        "borrador": 10.0,
        "regla": 30.0,
        "lapicera": 20.0,
    }

    precios = incrementar_precio(precios, "cuaderno", 15)

    imprimir_lista_precios(precios)

    producto_mas_costoso = obtener_item_mas_costoso(precios)
    print(
        f"\nEl ítem más costoso es: {producto_mas_costoso} con un precio de ${precios[producto_mas_costoso]:.2f}"
    )


main()
