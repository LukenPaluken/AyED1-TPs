def ingresar_fecha():
    """
    Solicita al usuario que ingrese una fecha (día, mes, año).

    Utiliza un bucle `while` para solicitar la fecha repetidamente hasta que el usuario
    ingrese números válidos para el día, mes y año. Maneja la excepción `ValueError`
    si el usuario ingresa algo que no sea un número entero.

    Retorna:
        tuple: Una tupla que contiene el día, mes y año ingresados por el usuario.
    """
    while True:
        try:
            dia = int(input("Ingresar día: "))
            mes = int(input("Ingresar mes: "))
            anio = int(input("Ingresar año: "))
            return dia, mes, anio
        except ValueError:
            print("Por favor, ingrese un número válido.")


def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también
    sea divisible por 400.

    Argumentos:
        anio: El año que se quiere verificar.

    Retorna:
        bool: `True` si el año es bisiesto, `False` de lo contrario.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def verificar_fecha(dia, mes, anio):
    """
    Verifica si una fecha es válida teniendo en cuenta el día, mes y año proporcionados por el usuario.

    El día y el mes se verifican contra los valores posibles (e.g., 1-31 para días, 1-12 para meses).
    Febrero se ajusta si el año es bisiesto. Los días y meses se validan con una tabla de días por mes.

    Argumentos:
        dia (int): El día del mes.
        mes (int): El mes del año.
        anio (int): El año a validar.

    Retorna:
        bool: `True` si la fecha es válida, `False` de lo contrario.
    """
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

    if dia <= 0 or mes <= 0 or mes > 12 or anio <= 0:
        return False

    if mes == 2 and es_bisiesto(anio):
        return dia <= 29

    return dia <= dias_por_mes.get(mes, 31)


def app():
    """
    Función principal de la aplicación que gestiona la interacción con el usuario.

    Solicita al usuario que ingrese una fecha, luego verifica si la fecha es válida o no
    utilizando las funciones `ingresar_fecha` y `verificar_fecha`. Informa al usuario si la
    fecha ingresada es válida o inválida.
    """
    dia, mes, anio = ingresar_fecha()
    if verificar_fecha(dia, mes, anio):
        print("Fecha válida.")
    else:
        print("Fecha inválida.")


app()