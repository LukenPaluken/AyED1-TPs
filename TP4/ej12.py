def crear_baraja():
    numeros = list(range(1, 13))
    palos = ["Oros", "Copas", "Bastos", "Espadas"]

    baraja = [f"{numero} {palo}" for palo in palos for numero in numeros]

    return baraja


baraja_final = crear_baraja()
print(baraja_final)
