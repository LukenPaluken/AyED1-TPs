es_oblongo = lambda x: any(n * (n + 1) == x for n in range(1, int(x**0.5) + 1))

es_triangular = lambda x: any(n * (n + 1) // 2 == x for n in range(1, int((2 * x)**0.5) + 1))

def app() -> None:
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            if es_oblongo(numero):
                print(f"{numero} es oblongo.")
            else:
                print(f"{numero} no es oblongo.")

            if es_triangular(numero):
                print(f"{numero} es triangular.")
            else:
                print(f"{numero} no es triangular.")
        except ValueError:
            print("Por favor ingresar un entero.")

app()
