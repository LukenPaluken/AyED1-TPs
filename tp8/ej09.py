def diccionario_tabla_multi(num) -> dict:
    """
    Genera un diccionario que representa la tabla de multiplicar de un número dado.

    Parameters:
        num (int): El número para el cual se generará la tabla de multiplicar.

    Returns:
        dict: Un diccionario donde las claves son los números del 1 al 12, 
              y los valores son el resultado de multiplicar esas claves por el número dado.
    """
    return {i:num*i for i in range(1,13)}

try:
    numero = int(input("Ingrese un numero: "))
    diccionario = diccionario_tabla_multi(numero)
    for multiplo, resultado in diccionario.items():
        print(f"{multiplo} x {numero} = {resultado}")
except ValueError:
    print("Debe ingresar un numero entero.")
