"""Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía."""

import re

def descomponer_email(correo: str) -> tuple:
    """
    Descompone una dirección de correo electrónico en sus partes utilizando una expresión regular.

    Parameters:
        email (str): Dirección de correo electrónico en formato válido (ejemplo: alguien@uade.edu.ar).

    Retorna:
        tuple: Una tupla con las partes que componen el correo electrónico 
               (usuario, dominio, subdominios). Si el formato es inválido, retorna una tupla vacía.
    """
    patron = r"^([\w\.-]+)@([\w\.-]+)\.([\w\.]+)$"
    match = re.match(patron, correo)

    if match:
        usuario = match.group(1)
        dominio = match.group(2)
        subdominios = match.group(3).split(".")
        return (usuario, dominio, *subdominios)

    return ()

def main():
    """
    Programa principal para ingresar una dirección de correo electrónico, descomponerla
    y mostrar las partes que la componen.

    Retorna:
        None
    """
    email = input("Ingrese una dirección de correo electrónico: ").strip()
    partes = descomponer_email(email)
    
    if partes:
        print(f"Las partes de la dirección son: {partes}")
    else:
        print("La dirección de correo electrónico es inválida.")

main()