def verificar_numeros(num1: int, num2: int) -> bool:
    """
    Verifica si los dos números proporcionados son positivos.
    """
    return num1 > 0 and num2 > 0


def concatenar_numeros(num1: int, num2: int) -> str:
    """
    Concatena dos números enteros y los devuelve como una cadena de caracteres.
    """
    return f"{num1}{num2}"


def app() -> None:
    """
    Función principal que controla el flujo de la aplicación.
    """
    while True:
        try:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            if not verificar_numeros(num1, num2):
                print("Por favor ingresar solo numeros positivos.")
            else:
                print(concatenar_numeros(num1, num2))
                break
        except ValueError:
            print("Valor debe ser un entero")


app()
