def es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también
    sea divisible por 400.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def verificar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si una fecha es válida teniendo en cuenta el día, mes y año proporcionados por el usuario.

    Febrero se ajusta si el año es bisiesto.
    """
    if dia <= 0 or mes <= 0 or mes > 12 or anio <= 0:
        return False

    if mes == 2 and es_bisiesto(anio):
        return dia <= 29

    return dia <= dias_por_mes[mes]


def dia_siguiente(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    """
    Calcula el día siguiente a una fecha dada.
    """
    if not verificar_fecha(dia, mes, anio):
        print("Fecha no válida. Inténtalo nuevamente.")
        return False

    if dia < dias_por_mes[mes]:
        return dia + 1, mes, anio
    else:
        if mes == 12:
            return 1, 1, anio + 1
        else:
            return 1, mes + 1, anio


def sumar_n_dias(dia: int, mes: int, anio: int, n: int) -> tuple[int, int, int]:
    """
    Suma N días a una fecha dada.
    """
    for _ in range(n):
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    return dia, mes, anio


def dias_entre_fechas(dia1: int, mes1: int, anio1: int, dia2: int, mes2: int, anio2: int) -> int:
    """
    Calcula la cantidad de días entre dos fechas.
    """
    dias = 0
    while (dia1, mes1, anio1) != (dia2, mes2, anio2):
        dia1, mes1, anio1 = dia_siguiente(dia1, mes1, anio1)
        dias += 1
    return dias


def mostrar_opciones() -> None:
    """
    Muestra las opciones del menú al usuario.
    """
    for count, items in enumerate(opciones, 1):
        print(f"{count} - {items}")


def menu() -> None:
    """
    Presenta un menú interactivo para sumar días a una fecha o calcular los días entre dos fechas.
    """
    while True:
        mostrar_opciones()
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            dia = int(input("Introduce el día: "))
            mes = int(input("Introduce el mes: "))
            anio = int(input("Introduce el año: "))
            n = int(input("Introduce el número de días a sumar: "))
            nuevo_dia, nuevo_mes, nuevo_anio = sumar_n_dias(dia, mes, anio, n)
            print(
                f"Fecha luego de sumar {n} días: {nuevo_dia}/{nuevo_mes}/{nuevo_anio}"
            )

        elif opcion == "2":
            dia1 = int(input("Introduce el primer día: "))
            mes1 = int(input("Introduce el primer mes: "))
            anio1 = int(input("Introduce el primer año: "))
            dia2 = int(input("Introduce el segundo día: "))
            mes2 = int(input("Introduce el segundo mes: "))
            anio2 = int(input("Introduce el segundo año: "))
            total_dias = dias_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2)
            print(f"Cantidad de días entre las dos fechas: {total_dias}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


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
    12: 31,
}


opciones = [
    "Sumar N días a una fecha",
    "Calcular la cantidad de días entre dos fechas",
    "Salir",
]


menu()
