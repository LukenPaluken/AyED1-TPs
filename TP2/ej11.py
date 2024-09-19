def ingresar_datos() -> list[tuple[int, int]]:
    pacientes = []
    while True:
        try:
            numero_afiliado = int(
                input("Ingrese su número de afiliado (4 dígitos) o -1 para finalizar: ")
            )

            if numero_afiliado == -1:
                print("Fin del ingreso de pacientes.")
                break

            if len(str(numero_afiliado)) != 4:
                print("El número de afiliado debe tener 4 dígitos.")
                continue

            condicion = int(input("Ingrese 0 para urgencia o 1 con turno: "))
            if condicion not in (0, 1):
                print("Opción inválida. Ingrese 0 para urgencia o 1 con turno.")
                continue

            tipo_atencion = "urgencia" if condicion == 0 else "turno"
            print(
                f"Paciente con número de afiliado {numero_afiliado} viene por {tipo_atencion}."
            )

            pacientes.append((numero_afiliado, condicion))

        except ValueError:
            print("Error: Ingrese un número válido.")

    return pacientes


def mostrar_listados(lista: list[tuple[int, int]]) -> None:
    por_urgencia = []
    por_turno = []

    for item in lista:
        if item[1] == 0:
            por_urgencia.append(item)
        else:
            por_turno.append(item)

    print("\nListado de pacientes atendidos por urgencia:")
    for count, paciente in enumerate(por_urgencia, 1):
        print(f"{count} - Número de afiliado: {paciente[0]}")

    print("\nListado de pacientes atendidos con turno:")
    for count, paciente in enumerate(por_turno, 1):
        print(f"{count} - Número de afiliado: {paciente[0]}")


def buscar_afiliado(lista: list[tuple[int, int]]) -> None:
    while True:
        try:
            numero_afiliado = int(
                input("Ingrese el número de afiliado a buscar o -1 para finalizar: ")
            )

            if numero_afiliado == -1:
                print("Fin de la búsqueda.")
                break

            contador_urgencia = 0
            contador_turno = 0

            for paciente in lista:
                if paciente[0] == numero_afiliado:
                    if paciente[1] == 0:
                        contador_urgencia += 1
                    else:
                        contador_turno += 1

            if contador_urgencia == 0 and contador_turno == 0:
                print(f"El afiliado {numero_afiliado} no fue encontrado.")
            else:
                print(
                    f"Afiliado {numero_afiliado}: {contador_urgencia} por urgencia y {contador_turno} por turno."
                )

        except ValueError:
            print("Error: Ingrese un número válido.")


def mostrar_opciones(lista: list[str]) -> None:
    """
    Muestra las opciones del menú.
    """
    for count, items in enumerate(lista, 1):
        print(f"{count} - {items}")


def menu():
    pacientes = []

    while True:
        mostrar_opciones(opciones)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pacientes = ingresar_datos()
        elif opcion == "2":
            if pacientes:
                mostrar_listados(pacientes)
            else:
                print("No hay pacientes ingresados.")
        elif opcion == "3":
            if pacientes:
                buscar_afiliado(pacientes)
            else:
                print("No hay pacientes ingresados.")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


opciones = [
    "Ingresar datos de pacientes.",
    "Mostrar listados de pacientes atendidos.",
    "Buscar un número de afiliado.",
    "Salir.",
]

menu()
