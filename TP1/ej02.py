DIAS_POR_MES = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def ingresar_fecha() -> tuple[int, int, int]:
    """
    Solicita al usuario que ingrese una fecha (día, mes, año).

    Utiliza un bucle `while` para solicitar la fecha repetidamente hasta que el usuario
    ingrese números válidos para el día, mes y año. Maneja la excepción `ValueError`
    si el usuario ingresa algo que no sea un número entero.
    """
    while True:
        try:
            dia = int(input("Ingresar día: "))
            mes = int(input("Ingresar mes: "))
            anio = int(input("Ingresar año: "))
            return dia, mes, anio
        except ValueError:
            print("Por favor, ingrese números enteros válidos para día, mes y año.")


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

    El día y el mes se verifican contra los valores posibles (e.g., 1-31 para días, 1-12 para meses).
    Febrero se ajusta si el año es bisiesto. Los días y meses se validan con una tabla de días por mes.
    """
    if dia <= 0 or mes <= 0 or mes > 12 or anio <= 0:
        return False

    if mes == 2 and es_bisiesto(anio):
        return dia <= 29

    return dia <= DIAS_POR_MES[mes - 1]


def app() -> None:
    """
    Función principal de la aplicación que gestiona la interacción con el usuario.
    """
    dia, mes, anio = ingresar_fecha()
    if not 1 <= dia <= 31:
        print("El día debe ser mayor a 0.")
    elif not 1 <= mes <= 12:
        print("El mes debe estar entre 1 y 12.")
    elif anio <= 0:
        print("El año debe ser un número positivo.")
    elif verificar_fecha(dia, mes, anio):
        print("Fecha válida.")
    else:
        print("Fecha inválida.")
    return None


app()
