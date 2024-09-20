import random as rnd


def generar_clave_maestra() -> str:
    string = ""
    for _ in range(rnd.randint(10, 20)):
        string += str(rnd.randint(0, 9))

    return string


def obtener_claves(clave_maestra: str) -> None:
    clave_par = ""
    clave_impar = ""
    long = len(clave_maestra)

    for i in range(long):
        if i % 2 == 0:
            clave_par += clave_maestra[i]
        else:
            clave_impar += clave_maestra[i]

    return clave_par, clave_impar


clave = generar_clave_maestra()
string_par, string_impar = obtener_claves(clave)
print(clave)
print(string_par)
print(string_impar)
