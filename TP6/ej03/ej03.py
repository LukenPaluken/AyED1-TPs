import re

def grabar_rango_alturas(archivo: str) -> None:
    """
    Solicita al usuario que ingrese deportes y alturas de atletas para cada deporte,
    y guarda esta información en un archivo de texto.

    Parameters:
        archivo (str): El nombre del archivo donde se guardará la información.
    
    Returns:
        None
    """
    try:
        with open(archivo, 'wt', encoding='utf-8') as file:
            while True:
                deporte = input("Ingrese el nombre del deporte (o 'q' para finalizar carga): ")
                if deporte.lower() == 'q':
                    print("Carga finalizada.")
                    break
                file.write(f"- {deporte.capitalize()}\n")

                while True:
                    altura_input = input("Ingrese altura en cm (o -1 para volver al deporte): ")
                    try:
                        altura = int(altura_input)
                        if altura == -1:
                            break
                        if altura < 0:
                            print("Por favor, ingrese una altura válida en cm o -1 para volver.")
                            continue
                        file.write(f"{altura}cm\n")
                    except ValueError:
                        print("Error: por favor ingrese un número entero para la altura.")

    except FileNotFoundError:
        print(f"Error: el archivo '{archivo}' no ha sido encontrado o no se pudo crear.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")


def grabar_promedio(archivo: str) -> dict:
    """
    Lee los datos de alturas de atletas por deporte desde un archivo de texto, calcula
    el promedio de alturas por disciplina y guarda los resultados en otro archivo de texto.

    Parameters:
        archivo (str): El nombre del archivo que contiene los datos de deportes y alturas de atletas.

    Returns:
        dict: Un diccionario donde las claves son los nombres de los deportes y los valores son listas
        con las alturas de los atletas para ese deporte.

    """
    try:
        with open(archivo, 'rt', encoding='utf-8') as file:
            alturas_por_disciplina = {}
            disciplina = None
            for linea in file:
                linea = linea.strip().replace(" ", "")

                if linea[0] == "-":
                    disciplina = linea[1:]
                    alturas_por_disciplina[disciplina] = []

                elif linea[:-2].isdigit():
                    if alturas_por_disciplina is not None:
                        alturas_por_disciplina[disciplina].append(int(linea[:-2]))

        with open('promedio_de_alturas.txt', 'wt', encoding='utf-8') as file:
            for disciplina, alturas in alturas_por_disciplina.items():
                if alturas:
                    promedio = sum(alturas) / len(alturas)
                    file.write(f"- {disciplina.capitalize()}\n")
                    file.write(f"Promedio de altura: {promedio:.2f}cm\n")

        return alturas_por_disciplina

    except FileNotFoundError:
        print(f"Error. El archivo '{archivo}' no se ha encontrado.")


def mostrar_mas_altos(archivo: str) -> None:
    """
    Esta función lee el archivo de promedios de alturas de disciplinas deportivas, y muestra las disciplinas
    cuyo promedio de altura supera la altura promedio general de todos los atletas.

    Parameters:
        archivo (str): El nombre del archivo que contiene los promedios de altura por disciplina.
        
    Returns:
        None
    """
    try:
        with open(archivo, 'rt', encoding='utf-8') as file:
            disciplinas = []
            alturas = []
            for linea in file:
                alturas.extend(float(num) for num in re.findall(r'\b\d+\.\d+(?=cm\b)?', linea))
                if linea[0] == "-":
                    disciplina = linea[1:].strip()
                    disciplinas.append(disciplina)

            if alturas:
                promedio = sum(alturas) / len(alturas)
                for disciplina, altura in zip(disciplinas, alturas):
                    if altura > promedio:
                        print("DISCIPLINAS DEPORTIVAS CUYOS ATLETAS SUPERAN LA ESTATURA PROMEDIO GENERAL\n")
                        print(f"- {disciplina}")

    except FileNotFoundError:
        print(f"Error. El archivo '{archivo}' no se ha encontrado.")


nombre_archivo = 'alturas.txt'
grabar_rango_alturas(nombre_archivo)
grabar_promedio(nombre_archivo)
mostrar_mas_altos('promedio_de_alturas.txt')
