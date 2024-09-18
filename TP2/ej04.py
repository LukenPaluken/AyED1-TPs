import random as rnd

rnd.seed(1)


def borrar_repetidos(lista_original: list, lista_segunda: list) -> None:
    """
    Elimina los elementos de la lista_original que se encuentran en la lista_segunda.

    Modifica la lista_original en lugar de crear una nueva lista modificada.
    """
    for num in lista_segunda:
        if num in lista_original:
            cant = lista_original.count(num)
            for _ in range(cant):
                lista_original.remove(num)


def mostrar_menu() -> None:
    """
    Muestra el menú interactivo con las opciones disponibles para el usuario.
    """
    print("\n--- Menú ---")
    print("1. Generar listas de números aleatorios")
    print("2. Eliminar números repetidos")
    print("3. Mostrar las listas")
    print("4. Salir")


lista_a = []
lista_b = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")
    if opcion == "1":
        lista_a = [rnd.randint(1, 20) for _ in range(20)]
        lista_b = [rnd.randint(1, 20) for _ in range(20)]
        print("\nListas generadas exitosamente.")
    elif opcion == "2":
        if lista_a and lista_b:
            print("\nEliminando números de la lista A que están en la lista B...")
            borrar_repetidos(lista_a, lista_b)
            print("Eliminación completada.")
        else:
            print("\nPor favor, genera las listas primero (opción 1).")
    elif opcion == "3":
        print("\nLista A (original o modificada):", lista_a)
        print("Lista B (números a eliminar):", lista_b)
    elif opcion == "4":
        print("\nSaliendo del programa. ¡Adiós!")
        break
    else:
        print("\nOpción no válida. Inténtalo de nuevo.")
