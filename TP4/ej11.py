def contar_subcadena(cadena: str, subcadena: str) -> int:
    cadena = cadena.lower()
    subcadena = subcadena.lower()

    count = 0
    start = 0

    while start < len(cadena):
        temp_sub = subcadena
        for i in range(start, len(cadena)):
            if cadena[i] == temp_sub[0]:
                temp_sub = temp_sub[1:]
                if not temp_sub:
                    count += 1
                    start = i + 1
                    break
        else:
            break

    return count

cadena = """
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
"""

subcadena = "UADE"
cantidad = contar_subcadena(cadena, subcadena)
print(f"Cantidad encontrada: {cantidad}")
