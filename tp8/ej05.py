def es_ortogonal(vector_uno: tuple, vector_dos: tuple) -> bool:
    """
    Determina si dos vectores son ortogonales.

    Parameters:
        vector_uno (tuple): Tupla que representa el primer vector (números reales o enteros).
        vector_dos (tuple): Tupla que representa el segundo vector (números reales o enteros).

    Retorna:
        bool: 
            - True si los vectores son ortogonales (el producto escalar es igual a 0), false 
            en caso contrario.
    """
    return not sum(a * b for a, b in zip(vector_uno, vector_dos))

vector1 = (3, 4)
vector2 = (-4, 3)

if es_ortogonal(vector1, vector2):
    print("Es ortogonal.")
else:
    print("No es ortogonal.")
    