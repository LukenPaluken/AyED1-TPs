def ingresar_socios() -> list[int]:
    """
    Permite ingresar números de socios (de 5 dígitos) y los almacena en una lista.
    """
    socios = []
    while True:
        try:
            numero_socio = int(
                input("Ingrese el número de socio (5 dígitos, 0 para finalizar): ")
            )

            if numero_socio == 0:
                print("Fin del ingreso de socios.")
                break

            if len(str(numero_socio)) != 5:
                print("El número de socio debe tener 5 dígitos.")
                continue

            socios.append(numero_socio)
            print(f"Socio {numero_socio} registrado exitosamente.")

        except ValueError:
            print("Error: Ingrese un número válido.")

    return socios


def contar_cantidad_ingresos(lista_socios: list[int]) -> dict[int, int]:
    """
    Cuenta cuántas veces cada socio ha ingresado.
    """
    ingresos_por_socio = {}

    for socio in lista_socios:
        if socio in ingresos_por_socio:
            ingresos_por_socio[socio] += 1
        else:
            ingresos_por_socio[socio] = 1

    for socio, cantidad in ingresos_por_socio.items():
        print(f"Socio {socio} ingresó {cantidad} veces.")

    return ingresos_por_socio


def eliminar_socio(dict_socio: dict[int, int]) -> None:
    """
    Elimina todos los ingresos de un socio específico y muestra los registros antes 
    y después de la eliminación.
    """
    print("\nRegistros de entrada antes de eliminar:")
    for socio, cantidad in dict_socio.items():
        print(f"Socio {socio} ingresó {cantidad} veces.")

    try:
        socio_a_eliminar = int(
            input("\nIngrese el número de socio que desea eliminar: ")
        )

        ingresos_eliminados = dict_socio.pop(socio_a_eliminar, None)

        if ingresos_eliminados is not None:
            print(
                f"\nSe eliminaron {ingresos_eliminados} ingresos del socio {socio_a_eliminar}."
            )
        else:
            print(f"\nEl socio {socio_a_eliminar} no existe en los registros.")
            return

        print("\nRegistros de entrada después de eliminar:")
        for socio, cantidad in dict_socio.items():
            print(f"Socio {socio} ingresó {cantidad} veces.")

    except ValueError:
        print("Error: Ingrese un número válido.")


def mostrar_opciones(lista: list[str]) -> None:
    """
    Muestra las opciones del menú.
    """
    for count, items in enumerate(lista, 1):
        print(f"{count} - {items}")


def menu():
    """
    Muestra el menú principal y gestiona las operaciones de registro, conteo y eliminación de socios.
    """
    lista_socios = []
    ingresos_por_socio = {}

    while True:
        mostrar_opciones(opciones)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista_socios = ingresar_socios()
        elif opcion == "2":
            ingresos_por_socio = contar_cantidad_ingresos(lista_socios)
        elif opcion == "3":
            if ingresos_por_socio:
                eliminar_socio(ingresos_por_socio)
            else:
                print("Primero debe contar los ingresos de los socios.")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")


opciones = [
    "Ingresar socios",
    "Contar cantidad de ingresos",
    "Eliminar socio",
    "Salir",
]

menu()
