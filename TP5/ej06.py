def cargar_lista() -> list[int]:
    """
    Carga una lista de números enteros ingresados por el usuario.
    
    Returns:
        list[int]: Lista de números enteros ingresados, excluyendo -1.
    """
    lista_numeros = []
    while True:
        try:
            numero = int(input("Ingrese un número para agregar a la lista (-1 para terminar): "))
            if numero == -1:
                break
            lista_numeros.append(numero)
        except ValueError:
            print("Se debe ingresar un número.")
    return lista_numeros


def visualizar_posicion_numeros() -> None:
    """
    Permite al usuario buscar la posición de elementos dentro de una lista.

    Returns:
        None
    """
    lista_numeros = cargar_lista()
    if not lista_numeros:
        print("No hay elementos en la lista.")
        return

    contador = 0
    while contador < 3:
        try:
            numero_buscado = int(input("Ingrese el número que desea encontrar: "))
            indice_numero = lista_numeros.index(numero_buscado)
            print(f"El número {numero_buscado} está en el índice {indice_numero}.")
        except ValueError:
            print("Número no encontrado en la lista.")
            contador += 1
            if contador == 3:
                print("Proceso abortado: Se han alcanzado tres errores consecutivos.")


visualizar_posicion_numeros()
