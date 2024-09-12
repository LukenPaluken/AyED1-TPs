    try:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            if not verificar_numeros(num1, num2):
                print("Por favor ingresar numeros positivos.")
        except ValueError:
            print("Valores deben ser enteros.")