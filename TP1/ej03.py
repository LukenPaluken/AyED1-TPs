def calcular_gastos(viajes, valor_pasaje):
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
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de viajes realizados: "))
            valor_pasaje = int(input("Ingresar el valor actual de un boleto: "))
            total_gastado = calcular_gastos(cantidad, valor_pasaje)
            print(f"El total gastado es de ${total_gastado}")
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")