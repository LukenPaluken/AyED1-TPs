def eliminar_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena de la cadena original utilizando rebanadas.
    """
    return cadena[:posicion] + cadena[posicion + cantidad :]


def eliminar_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena de la cadena original sin utilizar rebanadas.
    """
    resultado = ""
    resultado = ""
    for i, caracter in enumerate(cadena):
        if i < posicion or i >= posicion + cantidad:
            resultado += caracter
    return resultado


def mostrar_opciones(lista: list[str]) -> None:
    """
    Muestra las opciones del menú.
    """
    for count, items in enumerate(lista, 1):
        print(f"{count} - {items}")


def menu():
    """
    Muestra un menú para interactuar con las funciones.
    """
    while True:

        mostrar_opciones(opciones)
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            cadena = input("\nIntroduce la cadena: ")
            posicion = int(input("Introduce la posición de inicio: "))
            cantidad = int(input("Introduce la cantidad de caracteres a eliminar: "))
            resultado = eliminar_subcadena_rebanadas(cadena, posicion, cantidad)
            print(f"Resultado (con rebanadas): {resultado}")

        elif opcion == "2":
            cadena = input("\nIntroduce la cadena: ")
            posicion = int(input("Introduce la posición de inicio: "))
            cantidad = int(input("Introduce la cantidad de caracteres a eliminar: "))
            resultado = eliminar_subcadena_sin_rebanadas(cadena, posicion, cantidad)
            print(f"Resultado (sin rebanadas): {resultado}")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")


opciones = [
    "Eliminar subcadena (usando rebanadas)",
    "Eliminar subcadena (sin usar rebanadas)",
    "Salir",
]


menu()
