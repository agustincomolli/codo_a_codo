"""
Escribir dos funciones separadas para imprimir por pantalla los siguientes 
patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:

**********                          **
**********                          ****
**********                          ******
**********                          ********
**********                          **********

"""


def get_line():
    """
    Devuelve una línea de 10 asteriscos.

    Returns:
    str: una línea de 10 asteriscos.
    """
    return "**********"


def get_stair(row):
    """
    Devuelve una escalera de asteriscos, donde cada peldaño son 2 asteriscos.

    Args:
    row (int): Número de peldaños de la escalera.

    Returns:
    str: una escalera de asteriscos.
    """
    return "**" * row


def draw_patterns(rows: int):
    """I
    mprime dos patrones de asteriscos en paralelo.

    Args:
    rows (int): Número de filas a imprimir para cada patrón.
    """
    for row in range(1, rows + 1):
        print(f"{get_line()}\t\t\t\t{get_stair(row)}")


draw_patterns(5)
