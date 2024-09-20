def convertir_a_letras(num: int) -> str:

    if num < 0 or num > 1_000_000_000_000:
        return "Número fuera de rango"

    unidades = [
        "",
        "uno",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho",
        "nueve",
    ]
    decenas = [
        "",
        "diez",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    ]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince"]
    centenas = [
        "",
        "cien",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    ]

    partes_numero = []

    millones = num // 1_000_000
    if millones > 0:
        partes_numero.append(convertir_a_letras(millones) + " millones")
        num %= 1_000_000

    miles = num // 1_000
    if miles > 0:
        partes_numero.append(convertir_a_letras(miles) + " mil")
        num %= 1_000

    if num >= 100:
        partes_numero.append(centenas[num // 100])
        num %= 100

    if num >= 20:
        partes_numero.append(decenas[num // 10])
        num %= 10

    if 10 <= num < 20:
        partes_numero.append(especiales[num - 10])
    elif num > 0:
        partes_numero.append(unidades[num])

    return " ".join(partes_numero).strip()


numero = int(input("Ingresar numero: "))
print(convertir_a_letras(numero))
