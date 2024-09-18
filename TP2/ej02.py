import random as rnd


def generar_lista() -> list:
    """Genera una lista de números aleatorios entre 1 y 100."""
    n = int(input("Ingrese un número (cantidad de elementos de la lista): "))
    lista = [rnd.randint(1, 100) for _ in range(n)]
    print(f"Lista generada: {lista}")
    return lista


def elemento_repetido(lista: list) -> bool:
    """Devuelve True si la lista contiene elementos repetidos, False si no."""
    return len(lista) != len(set(lista))


def lista_unica(lista: list) -> list:
    """Devuelve una nueva lista con los elementos únicos de la lista original."""
    return list(set(lista))


def mostrar_opciones() -> None:
    """Muestra las opciones del menú."""
    print("\nOpciones:")
    print("1 - Generar una lista de números aleatorios")
    print("2 - Verificar si la lista contiene elementos repetidos")
    print("3 - Obtener una lista con elementos únicos")
    print("4 - Salir")


def menu() -> None:
    """Menú principal para interactuar con las funciones."""
    lista = []
    while True:
        mostrar_opciones()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            lista = generar_lista()
        elif opcion == "2":
            if not lista:
                print("No hay ninguna lista generada.")
            else:
                if elemento_repetido(lista):
                    print("La lista contiene elementos repetidos.")
                else:
                    print("La lista no contiene elementos repetidos.")
        elif opcion == "3":
            if not lista:
                print("No se ha generado ninguna lista. Primero, genere una lista.")
            else:
                unica = lista_unica(lista)
                print(f"Lista con elementos únicos: {unica}")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")



if __name__ == "__main__":
    menu()
