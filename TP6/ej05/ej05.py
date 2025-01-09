"""Se dispone de tres formatos diferentes de archivos de texto en los que se almacenan datos de empleados, detallados más abajo. Desarrollar un programa para cada 
uno de los formatos suministrados, que permitan leer cada uno de los archivos y 
grabar los datos obtenidos en otro archivo de texto con formato CSV.
Archivo 1: Los campos tienen longitud fija con un espacio de separación 
entre ellos.
(Regla) 1 2 3 4 5 6 
012345678901234567890123456789012345678901234567890123456789012
Pérez Juan 20080211 Corrientes 348 
González Ana M 20080115 Juan de Garay 1111 3er piso dto A
Archivo 2: Todos los campos de este archivo están precedidos por un 
número de dos dígitos que indica la longitud del campo a leer.
10Pérez Juan082008021114Corrientes 348
14González Ana M082008011533Juan de Garay 1111 3er piso dto A
NOTAS:
· Los espacios que se encuentren al final de las cadenas en el formato 1 deberán 
ser eliminados.
· El formato 2 debe generalizarse para que soporte registros con cualquier cantidad de campos.
"""


def cargar_archivo_uno(arch: str) -> None:
    longitudes = {1: 15, 2: 8, 3: 36}
    nombre_completo = input("Ingrese nombre y apellido: ")
    if not nombre_completo.replace(" ", "").isalpha():
        raise ValueError("El nombre completo solo debe contener letras y espacios.")
    codigo = input("Ingrese código de empleado (8 dígitos): ")
    if not (codigo.isdigit() and len(codigo) == 8):
        raise ValueError("El código de empleado debe ser un número de 8 dígitos.")
    domicilio = input("Ingrese domicilio: ")

    if len(nombre_completo) <= longitudes[1]:
        nombre_formateado = nombre_completo.ljust(longitudes[1])
    else:
        first_name = nombre_completo.split()[0:-1]
        initial = (
            nombre_completo.split()[-1][0] if len(nombre_completo.split()) > 1 else ""
        )
        nombre_formateado = f"{first_name} {initial}".ljust(longitudes[1])

    try:
        with open(arch, "wt", encoding="utf-8") as file:
            file.write(f"{nombre_formateado} {codigo} {domicilio}")
    except FileExistsError:
        print(f"Error: archivo '{arch}' no ha sido encontrado.")


def cargar_csv_uno(arch: str) -> None:
    try:
        with open(arch, "rt", encoding="utf-8") as file:
            with open("archivo_uno.csv", "wt", encoding="utf-8") as out_file:
                for linea in file:
                    print(linea)
                    out_file.write(f"{linea[:16]},{linea[16:24]},{linea[24:]}")
    except FileExistsError:
        print("Error: archivo 'archivo_uno_csv.csv' no ha sido encontrado.")


def cargar_archivo_dos(arch: str) -> None:
    """
    Carga datos en un archivo con campos precedidos por su longitud en dos dígitos.

    Recibe el nombre y apellido, código de empleado y domicilio, y graba estos datos
    en el archivo especificado en el formato con longitudes precedidas por los dos primeros dígitos.

    Parameters:
    arch (str): Ruta del archivo de salida donde se grabarán los datos.
    """
    try:
        nombre_completo = input("Ingrese nombre y apellido: ")
        if not nombre_completo.replace(" ", "").isalpha():
            raise ValueError("El nombre completo solo debe contener letras y espacios.")

        codigo = input("Ingrese código de empleado (8 dígitos): ")
        if not (codigo.isdigit() and len(codigo) == 8):
            raise ValueError("El código de empleado debe ser un número de 8 dígitos.")

        domicilio = input("Ingrese domicilio: ")

        nombre_completo_formateado = nombre_completo.ljust(10)
        codigo_formateado = codigo.ljust(8)
        domicilio_formateado = domicilio.ljust(14)

        data = [
            f"{len(nombre_completo_formateado):02}{nombre_completo_formateado}",
            f"{len(codigo_formateado):02}{codigo_formateado}",
            f"{len(domicilio_formateado):02}{domicilio_formateado}",
        ]

        with open(arch, "wt", encoding="utf-8") as file:
            file.write("".join(data))
        print(f"Archivo '{arch}' creado y datos guardados correctamente.")

    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def cargar_csv_dos(ruta: str) -> None:
    """
    Procesa un archivo donde los campos están precedidos por los dos primeros dígitos
    que indican la longitud de cada campo. Los campos procesados se escriben en otro archivo,
    separados por comas.

    Parámetros:
    ruta (str): Ruta del archivo de entrada que contiene los datos a procesar.
    ruta_salida (str): Ruta del archivo de salida donde se guardarán los resultados.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            with open("archivo_dos.csv", "w", encoding="utf-8") as out_file:
                data = file.readlines()

                for line in data:
                    line = line.strip()
                    valor_inicial = 0
                    campos = []

                    while valor_inicial < len(line):
                        largo = int(line[valor_inicial : valor_inicial + 2])
                        valor_inicial += 2

                        campo = line[valor_inicial : valor_inicial + largo]
                        campos.append(campo)

                        valor_inicial += largo

                    out_file.write(f"{','.join(campos)}\n")

        print("Archivo de salida actualizado correctamente.")

    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


archivo_uno = "archivo_uno.txt"
archivo_dos = "archivo_dos.txt"

cargar_archivo_uno(archivo_uno)
cargar_csv_uno(archivo_uno)
cargar_archivo_uno(archivo_dos)
cargar_csv_dos(archivo_dos)
