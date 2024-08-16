def ingresar_numeros():
    """
    Solicita al usuario que ingrese tres números positivos y los almacena en una lista.
    
    El usuario tiene que ingresar un número válido (entero). Si el usuario ingresa un 
    valor no entero, se le pedirá que lo intente de nuevo hasta que ingrese un número válido.
    
    Retorna:
        numeros: Una lista de tres números enteros ingresados por el usuario.
    """
    numeros = []
    for _ in range(3):
        while True:
            try:
                num = int(input("Ingrese un número positivo: "))
                numeros.append(num)
                break
            except ValueError:
                print("Por favor ingrese un número válido.")
    return numeros


def verificar_numero_positivo(lista):
    """
    Verifica si todos los números en la lista son positivos.
    
    Argumentos:
        lista: Lista de números enteros.
    
    Retorna:
        bool: True si todos los números en la lista son positivos, False en caso contrario.
    """
    for item in lista:
        if item < 0:
            return False
    return True


def mayor_estricto(lista):
    """
    Determina el mayor número de la lista, si este es único.
    
    Si el mayor número en la lista aparece más de una vez, se devuelve -1 para indicar que 
    no hay un mayor estricto.
    
    Argumentos:
        lista: Lista de números enteros.
    
    Retorna:
        int: El mayor número si es único, -1 si es repetido.
    """
    mayor = max(lista)
    if lista.count(mayor) > 1:
        return -1
    return mayor


def app():
    """
    Ejecuta la aplicación principal que solicita números al usuario, verifica que sean positivos,
    y determina si hay un número mayor estricto.
    
    Si todos los números ingresados son positivos, se verifica si existe un mayor estricto. 
    Dependiendo de los resultados, se imprimirá un mensaje adecuado.
    """
    numeros = ingresar_numeros()
    MAYOR = mayor_estricto(numeros)
    if verificar_numero_positivo(numeros):
        if MAYOR == -1:
            print("No hay un mayor estricto.")
        else:
            print(f"El número mayor es {MAYOR}.")
    else:
        print("Por favor, solo ingrese números positivos.")


app()