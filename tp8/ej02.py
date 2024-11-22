from datetime import datetime


def convertir_a_fecha_extendida(fecha: tuple, corte: int) -> str:
    """
    Convierte una fecha en formato (día, mes, año) a una representación extendida.

    Parameters:
        fecha (tuple[int, int, int]): Tupla que contiene el día, mes y año de la fecha.
        corte (int): Año de corte para determinar el siglo al interpretar años con dos dígitos.

    Retorna:
        str: Cadena de texto que representa la fecha en formato extendido.
    """
    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]
    dia, mes, anio = fecha

    if anio < 100:
        anio += 2000 if anio <= corte else anio + 1900

    return f"{dia} de {meses[mes - 1]} de {anio}"


def main():
    """
    Programa principal para ingresar una fecha, procesarla y mostrarla en formato extendido.
    """
    try:
        fecha_input = input(
            "Ingrese una fecha en formato DD/MM/AA o DD/MM/AAAA: "
        ).strip()
        dia, mes, anio = map(int, fecha_input.split("/"))

        datetime(anio if anio >= 100 else 2000, mes, dia)

        fecha_texto = convertir_a_fecha_extendida((dia, mes, anio), ANIO_CORTE)
        print(f"Fecha en formato extendido: {fecha_texto}")

    except ValueError:
        print(
            "Fecha inválida. Asegúrese de ingresarla en el formato correcto y que sea válida."
        )


ANIO_CORTE = 50
main()
