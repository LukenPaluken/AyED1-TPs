def ultimos_caracteres(cadena: str, n: int) -> str:
    return cadena[-n:]


string = "Esto es un string super duper largo que sirve para testear"
num = int(input("N (imprimir ultimos N caracteres): "))
string_ultimos = ultimos_caracteres(string, num)
print(string_ultimos)
