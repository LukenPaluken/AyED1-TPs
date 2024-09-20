def convertir_a_romano(num: int) -> str:
    """
    Convierte un número entero entre 1 y 3999 en un número romano.
    """
    if not 0 < num < 4000:
        return "El número debe estar entre 1 y 3999."

    valores = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    resultado = ""
    for valor, simbolo in valores:
        while num >= valor:
            resultado += simbolo
            num -= valor

    return resultado


numero = int(input("Ingrese un numero: "))
romano = convertir_a_romano(numero)
print(f"El número {numero} en romano es {romano}")
