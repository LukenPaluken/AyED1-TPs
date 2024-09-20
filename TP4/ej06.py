def extraer_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena utilizando rebanadas.
    """
    return cadena[posicion : posicion + cantidad]


def extraer_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena sin utilizar rebanadas.
    """
    subcadena = ""
    for i in range(posicion, posicion + cantidad):
        subcadena += cadena[i]
    return subcadena


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
            cantidad = int(input("Introduce la cantidad de caracteres a extraer: "))
            resultado = extraer_subcadena_rebanadas(cadena, posicion, cantidad)
            print(f"Resultado (con rebanadas): {resultado}")

        elif opcion == "2":
            cadena = input("\nIntroduce la cadena: ")
            posicion = int(input("Introduce la posición de inicio: "))
            cantidad = int(input("Introduce la cantidad de caracteres a extraer: "))
            resultado = extraer_subcadena_sin_rebanadas(cadena, posicion, cantidad)
            print(f"Resultado (sin rebanadas): {resultado}")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")


opciones = [
    "Extraer subcadena (usando rebanadas)",
    "Extraer subcadena (sin usar rebanadas)",
    "Salir",
]


menu()
