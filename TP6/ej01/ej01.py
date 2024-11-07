def leer_archivo(ruta: str) -> list:
    """
    Lee un archivo de texto y devuelve una lista de nombres y apellidos.

    Parameters:
        ruta (str): Ruta del archivo a leer.

    Returns:
        list: Lista de listas, donde cada sublista contiene [apellido, nombre].
    """
    try:
        with open(ruta, "rt", encoding="utf-8") as file:
            return [linea.strip().split(",") for linea in file]
    except FileNotFoundError:
        print("El archivo que intenta abrir no existe.")
        return []


def escribir_archivos(nombres: list) -> None:
    """
    Escribe nombres y apellidos en archivos de texto según criterios específicos.

    Parameters:
        nombres (list): Lista de listas, donde cada sublista contiene [apellido, nombre].

    Returns:
        None
    """
    try:
        for nombre_apellido in nombres:
            if len(nombre_apellido) != 2:
                raise ValueError(
                    "Cada entrada debe contener exactamente dos elementos: nombre y apellido."
                )

        paises = {
            "ARMENIA.txt": lambda apellido: apellido[-3:].lower() == "ian",
            "ITALIA.txt": lambda apellido: apellido[-3:].lower() == "ini",
            "ESPAÑA.txt": lambda apellido: apellido[-2:].lower() == "ez",
        }

        for pais, condicion in paises.items():
            try:
                with open(pais, "wt", encoding="utf-8") as file:
                    for nombre_apellido in nombres:
                        apellido, nombre = nombre_apellido
                        if condicion(apellido):
                            file.write(f"{apellido},{nombre}\n")
            except IOError:
                print(f"Error en la escritura del archivo {pais}.")
    except ValueError as ve:
        print(f"Error en formato de nombres: {ve}")
    except FileNotFoundError:
        print("El archivo que intenta abrir no existe.")


ruta_archivo = "ej01_nombres.txt"
lista_nombres = leer_archivo(ruta_archivo)
if lista_nombres:
    escribir_archivos(lista_nombres)
