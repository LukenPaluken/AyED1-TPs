import random as rnd

rnd.seed(5)


def cargar_datos() -> list[list[list[int]]]:
    """
    Genera los datos de producción de bicicletas para varias fábricas. Cada fábrica
    tiene un registro de la cantidad de bicicletas producidas durante 7 días. La
    cantidad de fábricas es un número aleatorio entre 1 y 5.
    """
    fabricas = []
    n = rnd.randint(1, 5)

    for i in range(n):
        ventas_fabrica = []
        for j in range(7):
            ventas = [j + 1, rnd.randint(0, 150)]
            ventas_fabrica.append(ventas)
        fabricas.append(ventas_fabrica)
        print(f"Fabrica {i + 1}:\n{ventas_fabrica}")

    return fabricas


def total_por_fabrica(fabricas: list[list[list[int]]]) -> None:
    """
    Muestra la cantidad total de bicicletas producidas por cada fábrica.
    """
    for i, fabrica in enumerate(fabricas):
        total_bicicletas = sum(ventas[1] for ventas in fabrica)
        print(f"Fábrica {i + 1} fabricó un total de {total_bicicletas} bicicletas.")


def fabrica_mayor_produccion(fabricas: list[list[list[int]]]) -> None:
    """
    Determina la fábrica que produjo la mayor cantidad de bicicletas en un solo día,
    mostrando el día y la fábrica.
    """
    max_produccion = 0
    dia_max = 0
    fabrica_max = 0

    for i, fabrica in enumerate(fabricas):
        for ventas in fabrica:
            dia, produccion = ventas
            if produccion > max_produccion:
                max_produccion = produccion
                dia_max = dia
                fabrica_max = i + 1

    print(
        f"La fábrica {fabrica_max} produjo la mayor cantidad en un solo día: {max_produccion} bicicletas el día {dia_max}."
    )


def dia_mas_productivo(fabricas: list[list[list[int]]]) -> None:
    """
    Determina el día más productivo en general (considerando todas las fábricas
    combinadas) y muestra la cantidad de bicicletas producidas ese día.
    """
    total_por_dia = [0] * 7

    for fabrica in fabricas:
        for ventas in fabrica:
            dia, produccion = ventas
            total_por_dia[dia - 1] += produccion

    dia_max = total_por_dia.index(max(total_por_dia)) + 1
    print(
        f"El día más productivo fue el día {dia_max}, con {max(total_por_dia)} bicicletas producidas en total."
    )


def menor_fabricacion_por_fabrica(fabricas: list[list[list[int]]]) -> list[int]:
    """
    Genera una lista que contiene la menor cantidad de bicicletas fabricadas
    por cada fábrica en un solo día.
    """
    return [min(ventas[1] for ventas in fabrica) for fabrica in fabricas]


def main():
    """
    Programa que utiliza todas las funciones.
    """

    print("Generando datos de producción de bicicletas:\n")
    fabricas = cargar_datos()
    print()
    total_por_fabrica(fabricas)
    print()
    fabrica_mayor_produccion(fabricas)
    print()
    dia_mas_productivo(fabricas)

    print("\nMenor cantidad de bicicletas fabricadas en un día por cada fábrica:")
    menores = menor_fabricacion_por_fabrica(fabricas)
    for i, menor in enumerate(menores):
        print(f"Fábrica {i + 1}: {menor} bicicletas")


main()
