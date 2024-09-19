import random as rnd

rnd.seed(1)


def intercalar_elementos() -> None:
    index = 1
    for item in lista_dos:
        lista_uno[index:index] = [item]
        index += 2


lista_uno = [rnd.randint(0, 9) for _ in range(rnd.randint(3, 5))]
lista_dos = [rnd.randint(0, 9) for _ in range(rnd.randint(3, 5))]

print(lista_uno)
print(lista_dos)
intercalar_elementos()
print(lista_uno)
