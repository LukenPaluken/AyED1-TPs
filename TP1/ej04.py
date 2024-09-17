def verificar_entradas(total: int, recibido: int) -> bool:
    """
    Verifica que los valores ingresados para el total de la compra y el dinero recibido sean válidos.
    """
    return total > 0 and recibido > 0


def ingresar_total() -> tuple[int, int]:
    """
    Solicita al usuario que ingrese el total de la compra y el dinero recibido,
    asegurándose de que sean valores enteros positivos.
    """
    while True:
        try:
            total = int(input("Ingrese el total de la compra: "))
            recibido = int(input("Ingrese el dinero recibido: "))
            if total > 0 and recibido > 0:
                return total, recibido
            else:
                print("Por favor ingresar números mayores a 0.")
        except ValueError:
            print("Por favor ingrese un número válido.")


def calcular_vuelto(total_compra: int, dinero_recibido: int) -> dict[int, int]:
    """
    Calcula el vuelto que debe entregarse al cliente minimizando la cantidad de billetes utilizados.
    """
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    cambio = dinero_recibido - total_compra
    vuelto = {}

    if cambio < 0:
        return -1

    for billete in billetes:
        if cambio >= billete:
            cantidad_billetes = cambio // billete
            vuelto[billete] = cantidad_billetes
            cambio -= cantidad_billetes * billete

    if cambio != 0:
        return -2

    return vuelto


def app() -> None:
    """
    Controla el flujo principal del programa para calcular y mostrar el vuelto a entregar al cliente.
    """
    total, recibido = ingresar_total()

    if not verificar_entradas(total, recibido):
        print("Por favor ingresar números mayores a 0.")
        return

    status = calcular_vuelto(total, recibido)

    if status == -1:
        print("El dinero recibido es insuficiente.")
    elif status == -2:
        print("No se puede entregar el cambio exacto con las denominaciones disponibles.")
    else:
        print("\nVUELTO\n")
        for billete, cantidad in status.items():
            print(f"{cantidad} billete(s) de ${billete}")


app()
