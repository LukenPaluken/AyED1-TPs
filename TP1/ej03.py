def calcular_gastos(viajes, valor_pasaje):
    """
    Calcula el total gastado en pasajes de subte en un mes, aplicando descuentos según la cantidad de viajes realizados.

    Argumentos:
        viajes (int): La cantidad de viajes realizados en el mes.
        valor_pasaje (float): El valor actual de un boleto.

    Retorna:
        float: El total gastado considerando los descuentos aplicables.
    """
    total_gastado = valor_pasaje * viajes
    if 1 <= viajes <= 20:
        return total_gastado
    elif 21 <= viajes <= 30:
        return total_gastado * 0.8
    elif 31 <= viajes <= 40:
        return total_gastado * 0.7
    else:
        return total_gastado * 0.6


def app():
    """
    Función principal de la aplicación que interactúa con el usuario para calcular el total gastado en pasajes de subte.

    Solicita al usuario la cantidad de viajes realizados y el valor de un boleto,
    luego utiliza la función `calcular_gastos` para determinar el costo total con descuentos aplicables.
    """
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de viajes realizados: "))
            valor_pasaje = int(input("Ingresar el valor actual de un boleto: "))
            total_gastado = calcular_gastos(cantidad, valor_pasaje)
            print(f"El total gastado es de ${total_gastado}")
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
