import random as rnd

def cargar_matriz() -> list[list[int]]:
    """
    Carga una matriz de N x N de números enteros ingresados por el usuario.
    """
    n = int(input("Ingrese la longitud para una matriz N x N: "))

    numeros_unicos = list(range(0, n**2))
    rnd.shuffle(numeros_unicos)

    matriz = []
    for i in range(n):
        fila =  numeros_unicos[i * n:(i + 1) * n]
        matriz.append(fila)

    return matriz


def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Imprime la matriz en formato legible.
    """
    for fila in matriz:
        print(fila)


matrizz = cargar_matriz()
imprimir_matriz(matrizz)
