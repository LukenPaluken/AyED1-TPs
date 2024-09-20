import random as rnd


def cargar_sala(filas: int, butacas: int) -> list[list[int]]:
    """
    Carga la sala de cine con valores aleatorios. 0 representa una butaca libre y 1 una butaca ocupada.
    """
    return [[rnd.randint(0, 1) for _ in range(butacas)] for _ in range(filas)]


def mostrar_butacas(sala: list[list[int]]) -> None:
    """
    Muestra por pantalla el estado actual de las butacas de la sala.
    Un 0 indica una butaca libre y un 1 indica una butaca ocupada.
    """
    print("\nEstado actual de la sala de cine (0 = Libre, 1 = Ocupada):")
    for i, fila in enumerate(sala):
        print(f"Fila {i + 1}: {fila}")


def reservar(sala: list[list[int]], fila: int, butaca: int) -> bool:
    """
    Realiza la reserva de una butaca en la sala de cine si está disponible (0). Si la reserva se completa,
    la butaca cambia su estado a 1 (ocupada).
    """
    if sala[fila][butaca] == 0:
        sala[fila][butaca] = 1
        return True
    else:
        return False


def butacas_libres(sala: list[list[int]]) -> int:
    """
    Cuenta cuántas butacas están libres en toda la sala.
    """
    return sum(fila.count(0) for fila in sala)


def butacas_contiguas(sala: list[list[int]]) -> None:
    pass


def mostrar_opciones(lista: list[str]) -> None:
    """
    Muestra las opciones del menú.
    """
    for count, items in enumerate(lista, 1):
        print(f"{count} - {items}")


def main():
    filas = int(input("Ingrese el número de filas: "))
    butacas_por_fila = int(input("Ingrese el número de butacas por fila: "))

    sala = cargar_sala(filas, butacas_por_fila)
    mostrar_butacas(sala)

    while True:

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_butacas(sala)
        elif opcion == "2":
            fila = int(input("Ingrese el número de fila (1 a N): ")) - 1
            butaca = int(input("Ingrese el número de butaca (1 a M): ")) - 1
            if reservar(sala, fila, butaca):
                print(f"Butaca reservada en fila {fila + 1}, butaca {butaca + 1}.")
            else:
                print(
                    f"La butaca en fila {fila + 1}, butaca {butaca + 1} ya está ocupada."
                )
        elif opcion == "3":
            libres = butacas_libres(sala)
            print(f"Hay {libres} butacas libres en la sala.")
        elif opcion == "4":
            pass
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intentar nuevamente.")


opciones = [
    "Mostrar estado de las butacas",
    "Reservar una butaca",
    "Ver cuántas butacas libres hay",
    "Ver secuencia más larga de butacas contiguas libres",
    "Salir",
]


main()
