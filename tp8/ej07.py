def eliminar_numero(conjunto: set) -> None:
    """
    Permite eliminar números de un conjunto interactivamente.

    Parameters:
        conjunto (set): El conjunto del que se eliminarán los números.
    """
    while True:
        if not conjunto:
            print("El conjunto se encuentra vacío.")
            break

        try:
            num = int(input("Ingrese el número que desea eliminar (-1 para salir): "))

            if num == -1:
                print("Saliendo...")
                break

            conjunto.remove(num)
            if conjunto:
                print(conjunto)
        except KeyError:
            print("El número a eliminar no existe en el conjunto.")
        except ValueError:
            print("Ingrese un número válido.")


mi_conjunto = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

eliminar_numero(mi_conjunto)
