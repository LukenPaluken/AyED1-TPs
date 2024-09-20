def cargar_numeros() -> list[list[int]]:
    """
    Carga una matriz de N x N de números enteros ingresados por el usuario.
    """
    long = int(input("Ingrese la longitud para una matriz N x N: "))

    matriz = []

    for i in range(long):
        fila = []
        for j in range(long):
            numero = int(input(f"Ingrese el {j + 1}° número de la {i + 1}° fila: "))
            fila.append(numero)
        matriz.append(fila)

    return matriz


def ordenar_listas(matriz: list[list[int]]) -> None:
    """
    Ordena cada fila de la matriz en orden ascendente.
    """
    for fila in matriz:
        fila.sort()


def intercambiar_filas(
    matriz: list[list[int]], fila_uno: int, fila_dos: int
) -> list[list[int]]:
    """
    Intercambia dos filas de la matriz.
    """
    if fila_uno not in range(len(matriz)) or fila_dos not in range(len(matriz)):
        print("Ingresar un número de fila válido.")
    else:
        matriz[fila_uno], matriz[fila_dos] = matriz[fila_dos], matriz[fila_uno]

    return matriz


def intercambiar_columnas(
    matriz: list[list[int]], columna_uno: int, columna_dos: int
) -> list[list[int]]:
    """
    Intercambia dos columnas de la matriz.
    """
    if columna_uno not in range(len(matriz[0])) or columna_dos not in range(
        len(matriz[0])
    ):
        print("Ingresar un número de columna válido.")
    else:
        for fila in matriz:
            fila[columna_uno], fila[columna_dos] = fila[columna_dos], fila[columna_uno]

    return matriz


def trasponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    """
    Traspone la matriz sobre sí misma.
    """
    n = len(matriz)

    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

    return matriz


def calcular_promedio(matriz: list[list[int]], fila: int) -> float:
    """
    Calcula el promedio de los elementos de una fila específica de la matriz.
    """
    promedio = sum(matriz[fila]) / len(matriz[fila])
    return promedio


def calcular_porcentaje_impar_columna(matriz: list[list[int]], columna: int) -> float:
    """
    Calcula el porcentaje de elementos impares en una columna específica de la matriz.
    """
    if columna < 0 or columna >= len(matriz[0]):
        print("Número de columna fuera de rango.")
        return 0.0

    total_elementos = len(matriz)
    impares_count = 0

    for fila in matriz:
        if fila[columna] % 2 != 0:
            impares_count += 1

    porcentaje = (impares_count / total_elementos) * 100
    return porcentaje


def es_palindromo(lista: list[int]) -> bool:
    """
    Verifica si una lista de números enteros es un palíndromo.
    """
    return lista == lista[::-1]


def columnas_palindromas(matriz: list[list[int]]) -> list[int]:
    """
    Determina qué columnas de la matriz son palíndromos.
    
    Revisa cada columna de la matriz y devuelve una lista con los índices de las columnas que son palíndromas.
    """
    if not matriz or not matriz[0]:
        return []

    num_columnas = len(matriz[0])
    columnas_palindromas_indices = []

    for j in range(num_columnas):
        columna = [matriz[i][j] for i in range(len(matriz))]
        if es_palindromo(columna):
            columnas_palindromas_indices.append(j)

    return columnas_palindromas_indices


def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Imprime la matriz en un formato legible.
    """
    for fila in matriz:
        print(fila)
    print()


def mostrar_opciones(lista: list[str]) -> None:
    """
    Muestra las opciones del menú.
    """
    for count, items in enumerate(lista, 1):
        print(f"{count} - {items}")


def menu():
    """
    Muestra un menú para interactuar con las funciones de la matriz.
    """
    matriz = cargar_numeros()

    while True:

        mostrar_opciones(opciones)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ordenar_listas(matriz)
            print("Matriz después de ordenar filas:")
            imprimir_matriz(matriz)
        elif opcion == "2":
            fila_uno = int(
                input("Ingrese el número de la primera fila a intercambiar: ")
            )
            fila_dos = int(
                input("Ingrese el número de la segunda fila a intercambiar: ")
            )
            intercambiar_filas(matriz, fila_uno - 1, fila_dos - 1)
            print("Matriz después de intercambiar filas:")
            imprimir_matriz(matriz)
        elif opcion == "3":
            columna_uno = int(
                input("Ingrese el número de la primera columna a intercambiar: ")
            )
            columna_dos = int(
                input("Ingrese el número de la segunda columna a intercambiar: ")
            )
            intercambiar_columnas(matriz, columna_uno - 1, columna_dos - 1)
            print("Matriz después de intercambiar columnas:")
            imprimir_matriz(matriz)
        elif opcion == "4":
            trasponer_matriz(matriz)
            print("Matriz después de trasponer:")
            imprimir_matriz(matriz)
        elif opcion == "5":
            fila = int(
                input("Ingrese el número de la fila para calcular el promedio: ")
            )
            promedio = calcular_promedio(matriz, fila)
            print(f"El promedio de la fila {fila} es: {promedio}")
        elif opcion == "6":
            columna = int(
                input(
                    "Ingrese el número de la columna para calcular el porcentaje de impares: "
                )
            )
            porcentaje = calcular_porcentaje_impar_columna(matriz, columna)
            print(
                f"El porcentaje de impares en la columna {columna} es: {porcentaje:.2f}%"
            )
        elif opcion == "7":
            pass
        elif opcion == "8":
            pass
        elif opcion == "9":
            resultado = columnas_palindromas(matriz)
            print(f"Las columnas palíndromas son: {resultado}")
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


opciones = [
    "Ordenar filas",
    "Intercambiar filas",
    "Intercambiar columnas",
    "Trasponer matriz",
    "Calcular promedio de una fila",
    "Calcular porcentaje de impares en una columna",
    "Salir",
]


menu()
