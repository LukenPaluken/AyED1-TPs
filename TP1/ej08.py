def diadelasemana(dia: int, mes: int, anio: int) -> int:
    """
    Calcula el día de la semana para una fecha dada.
    """
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem


def verificar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si una fecha es válida teniendo en cuenta el día, mes y año proporcionados.
    """
    if mes <= 0 or mes > 12:
        return False

    if es_bisiesto(anio) and mes == 2:
        max_dias = 29
    else:
        max_dias = dias_por_mes[mes]

    if dia <= 0 or dia > max_dias:
        return False

    return True


def es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también
    sea divisible por 400.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def imprimir_calendario(mes: int, anio: int) -> None:
    """
    Imprime el calendario de un mes específico.
    """
    if es_bisiesto(anio):
        dias_por_mes[2] = 29
    else:
        dias_por_mes[2] = 28

    print(f"\nCalendario para {mes}/{anio}")
    print("Do  Lu  Ma  Mi  Ju  Vi  Sa")

    primer_dia = diadelasemana(1, mes, anio)

    for _ in range(primer_dia):
        print("    ", end="")

    for dia in range(1, dias_por_mes[mes] + 1):
        print(f"{dia:2}  ", end="")

        if (primer_dia + dia) % 7 == 0:
            print()

    print()


def app() -> None:
    """
    Ejecuta la aplicación para imprimir un calendario mensual.
    Solicita el mes y año al usuario y valida si es una fecha válida antes de imprimir el calendario.
    """
    mes_input = int(input("Introduce el mes (1-12): "))
    anio_input = int(input("Introduce el año: "))

    if verificar_fecha(1, mes_input, anio_input):
        imprimir_calendario(mes_input, anio_input)
    else:
        print("Fecha inválida. Por favor, introduce un mes y año válidos.")


dias_por_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


app()
