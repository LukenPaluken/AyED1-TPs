def calcular_gastos(viajes: int, valor_pasaje: float) -> float:
    """
    Calcula el total gastado en pasajes de subte en un mes, aplicando descuentos según la cantidad de
    viajes realizados.
    """
    if 1 <= viajes <= 20:
        total_gastado = valor_pasaje * viajes
    elif 21 <= viajes <= 30:
        total_gastado = valor_pasaje * 0.8 * viajes
    elif 31 <= viajes <= 40:
        total_gastado = valor_pasaje * 0.7 * viajes
    else:
        total_gastado = valor_pasaje * 0.6 * viajes

    return round(total_gastado, 2)


def app() -> None:
    """
    Función principal de la aplicación que interactúa con el usuario para calcular el total gastado
    en pasajes de subte.
    """
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
            valor_pasaje = float(input("Ingrese el valor actual de un boleto (en pesos): "))

            if cantidad < 1:
                print("La cantidad de viajes debe ser mayor a 0.")
                continue

            total_gastado = calcular_gastos(cantidad, valor_pasaje)
            print(f"El total gastado es de ${total_gastado:.2f}")
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return None

app()
