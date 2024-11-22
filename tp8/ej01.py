from datetime import datetime


def anio_bisiesto(anio: int) -> bool:
    """
    Verifica si un año es bisiesto.

    Parameters: anio (int): El año a verificar.
        anio (int): El año a verificar.
        
    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def ingresar_fecha() -> tuple:
    """
    Permite al usuario ingresar una fecha en formato DD/MM/AAAA.

    La fecha ingresada es validada utilizando `datetime.strptime`.
    Si la fecha es válida, se devuelve como una tupla (AAAA, MM, DD).

    Returns:
        tuple: Una tupla que representa la fecha (AAAA, MM, DD), o None si la fecha es inválida.
    """
    try:
        fecha = input("Ingrese la fecha en formato DD/MM/AAAA: ")
        datetime.strptime(fecha, "%d/%m/%Y")
        fecha = tuple(reversed(fecha.split("/")))
        return fecha

    except ValueError:
        print("Fecha invalida.")
        return


def sumar_n_dias(fecha: tuple) -> None:
    """
    Suma un número de días a una fecha dada.

    Dado un número de días, calcula la nueva fecha respetando el número
    de días en cada mes y los años bisiestos.

    Parameters:
        fecha (tuple): La fecha inicial como una tupla (AAAA, MM, DD).

    Returns:
        tuple: La nueva fecha calculada como (AAAA, MM, DD), o None si ocurre un error.
    """
    try:
        sumar_dias = int(input("Ingrese la cantidad de dias que desea sumar: "))
        dia_new = fecha[2] + sumar_dias
        mes_new = fecha[1]
        anio_new = fecha[0]
        dias_del_mes = {
            1: 31,
            2: 29 if anio_bisiesto(anio_new) else 28,
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

        if dia_new > dias_del_mes[mes_new]:
            mes_new += 1

        if mes_new > 12:
            mes_new = 1
            anio_new += 1

        return (anio_new, mes_new, dia_new)

    except TypeError:
        print("Ingresar un numero entero.")


def ingresar_horario() -> tuple[int]:
    """
    Permite al usuario ingresar un horario en formato HH:MM.

    Valida que la hora esté entre 0 y 23, y que los minutos estén entre 0 y 59.

    Returns:
        tuple: Una tupla (hora, minuto) si el horario es válido, o None si no lo es.
    """
    while True:
        try:
            horario = input("Ingrese el horario en formato HH:MM: ").strip()
            hora, minuto = map(int, horario.split(":"))

            if 0 <= hora <= 23 and 0 <= minuto <= 59:
                return hora, minuto
            else:
                print(
                    "Horario inválido. La hora debe estar entre 0 y 23, y los minutos entre 0 y 59."
                )

        except (ValueError, IndexError):
            print("Formato inválido. Intente nuevamente.")


def sumar_n_horas(horario: tuple) -> tuple[int]:
    """
    Calcula la diferencia entre dos horarios dados en formato HH:MM.

    Si el segundo horario es anterior al primero, se asume que corresponde al día siguiente.

    Parameters:
        horario (tuple): Una tupla (hora, minuto) representando el primer horario.

    Returns:
        tuple: Una tupla (horas, minutos) representando la diferencia entre los horarios.
    """
    try:
        segundo_horario = input("Ingrese el segundo horario: ").strip()
        segunda_hora, segundo_minuto = map(int, segundo_horario.split(":"))

        if (
            segunda_hora <= 0
            or segunda_hora > 23
            or segundo_minuto <= 0
            or segundo_minuto > 59
        ):
            print(
                "Horario inválido. La hora debe estar entre 0 y 23, y los minutos entre 0 y 59."
            )

        hora = horario[0]
        minuto = horario[1]
        minutos_totales_uno = hora * 60 + minuto
        minutos_totales_dos = segunda_hora * 60 + segundo_minuto

        if minutos_totales_uno > minutos_totales_dos:
            minutos_totales_dos += 24 * 60

        diferencia_minutos = minutos_totales_dos - minutos_totales_uno
        horas = diferencia_minutos // 60
        minutos = diferencia_minutos % 60

        return horas, minutos

    except TypeError:
        print("Formato inválido. Intente nuevamente.")


def main():
    """
    Función principal que ejecuta el menú interactivo.
    """
    while True:
        print("\nSeleccione una opción:")
        print("1. Ingresar una fecha válida.")
        print("2. Sumar N días a una fecha.")
        print("3. Ingresar un horario válido.")
        print("4. Calcular la diferencia entre dos horarios.")
        print("5. Salir.")

        try:
            opcion = int(input("Ingrese su opción (1-5): "))
        except ValueError:
            print("Opción inválida. Debe ser un número entre 1 y 5.")
            continue

        if opcion == 1:
            fecha = ingresar_fecha()
            if fecha:
                print(f"Fecha ingresada correctamente: {fecha}")

        elif opcion == 2:
            if "fecha" not in locals():
                print("Primero debe ingresar una fecha válida (opción 1).")
            else:
                nueva_fecha = sumar_n_dias(fecha)
                if nueva_fecha:
                    print(f"Nueva fecha: {nueva_fecha}")

        elif opcion == 3:
            horario = ingresar_horario()
            print(f"Horario ingresado correctamente: {horario}")

        elif opcion == 4:
            if "horario" not in locals():
                print("Primero debe ingresar un horario válido (opción 3).")
            else:
                diferencia = sumar_n_horas(horario)
                if diferencia:
                    print(
                        f"Diferencia entre horarios: {diferencia[0]} horas y {diferencia[1]} minutos."
                    )

        elif opcion == 5:
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


main()
