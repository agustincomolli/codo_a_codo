"""
Escribir una función que reciba como parámetro una tupla conteniendo una fecha 
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada 
en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de Octubre de 
2017”. Escribir también un programa para verificar su comportamiento.

"""

from my_console_lib import *


class DateError(Exception):
    def __init__(self, message="Error en la fecha") -> None:
        """
        Excepción personalizada para manejar errores relacionados con fechas.
        """
        self.message = message
        super().__init__(self.message)


def is_valid_format(user_input: str) -> bool:
    """
    Verifica si la cadena de entrada tiene el formato correcto (dd-mm-yyyy).

    Args:
        user_input (str): La cadena de entrada que representa la fecha.

    Returns:
        bool: True si el formato es válido, False en caso contrario.
    """
    if len(user_input) != 10:
        return False
    elif user_input[2] != "-" or user_input[5] != "-":
        return False
    else:
        return True


def is_valid_data_type(day: str, month: str, year: str) -> bool:
    """
    Verifica si los componentes de la fecha son valores numéricos.

    Args:
        day (str): Día de la fecha.
        month (str): Mes de la fecha.
        year (str): Año de la fecha.

    Returns:
        bool: True si todos los componentes son numéricos, False en caso contrario.
    """
    if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
        return False
    else:
        return True


def is_valid_numbers_range(day, month, year):
    """
    Verifica si los componentes de la fecha están en rangos numéricos válidos.

    Args:
        day (int): Día de la fecha.
        month (int): Mes de la fecha.
        year (int): Año de la fecha.

    Returns:
        bool: True si los valores están en rangos válidos, False en caso contrario.
    """
    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
        return False
    else:
        return True


def is_year_leap(year: int) -> bool:
    """
    Verifica si el año es bisiesto.

    Args:
        year (int): Año a verificar.

    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    if year < 1582:
        return False
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def is_valid_date(day: int, month: int, year: int) -> bool:
    """
    Verifica si la fecha es válida.

    Args:
        day (int): Día de la fecha.
        month (int): Mes de la fecha.
        year (int): Año de la fecha.

    Returns:
        bool: True si la fecha es válida, False en caso contrario.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    elif month in [4, 6, 9, 11] and day <= 30:
        return True
    elif is_year_leap(year) and month == 2 and day <= 29:
        return True
    elif (not is_year_leap(year)) and month == 2 and day <= 28:
        return True
    else:
        return False


def is_valid_input(user_input: str) -> bool:
    """
    Verifica si la entrada del usuario es una fecha válida.

    Args:
        user_input (str): La cadena de entrada que representa la fecha.

    Returns:
        bool: True si la entrada es válida, False en caso contrario.
    """
    if not is_valid_format(user_input):
        return False

    day, month, year = user_input.split("-")
    if not is_valid_data_type(day, month, year):
        return False

    # Convertir las cadenas en números.
    day, month, year = int(day), int(month), int(year)
    if not is_valid_numbers_range(day, month, year):
        return False

    if not is_valid_date(day, month, year):
        return False
    else:
        return True


def get_long_date(day: int, month: int, year: int) -> str:
    """
    Devuelve una cadena con la fecha en formato extendido.

    Args:
        day (int): Día de la fecha.
        month (int): Mes de la fecha.
        year (int): Año de la fecha.

    Returns:
        str: Cadena de caracteres con la fecha en formato extendido.
    """
    month_list = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                  "julio", "agosto", "septiembre", "octubre", "noviembre",
                  "diciembre"]

    return f"{day} de {month_list[month - 1]} de {year}"


def get_user_date() -> tuple:
    """
    Obtiene una fecha válida ingresada por el usuario.

    Returns:
        tuple: Tupla de tres elementos (día, mes, año) que representa la fecha ingresada por el usuario.
    """
    while True:
        try:
            clear_screen()
            user_date = input_color(
                "Ingrese una fecha (dd-mm-yyy): ", color_input=Colors.BLUE)

            # Validar la entrada del usuario.
            if is_valid_input(user_date):
                return tuple(map(int, user_date.split("-")))
            else:
                raise DateError
        except DateError:
            error_message = "No has ingresado una fecha o su formato es erróneo."
            show_error(error_message)
            press_enter_to_continue()


day, month, year = get_user_date()
print(get_long_date(day, month, year))
