import os


class COLORS:
    """
    Clase para mantener las secuencias de escape de los colores ANSI.
    """

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    # Sequencia de escape por defecto para restablecer el color.
    DEFAULT = "\033[0m"


def color_text(text: str, color: str) -> str:
    return f"{color}{text}{COLORS.DEFAULT}"


def print_color(message: str, color: str, end: str = "\n") -> None:
    """
    Imprime un mensaje en un color especifico.

    :param message: El mensaje a imprimir.
    :param color: El color en el que se imprimirá el mensaje.
    :param end: El caracter que se imprimirá al final del mensaje. Por defecto es '\n'.
    """

    # Usamos la secuencia de escape del color definido en la clase COLORS.
    print(color_text(message, color), end=end)


def print_title(text: str, color: str, underline_char: str = "*"):
    """
    Imprime un título con una línea subrayada.

    Parameters:
    text (str): El texto del título.
    underline_char (str): El carácter utilizado para subrayar el título.
    """
    print(f"{color_text(text, color)}\n{color_text(
        underline_char, color) * (len(text) + 1)}")


def input_color(message: str, color_message: str, color_input: str) -> str:
    """
    Solicita un input al usuario mostrando el mensaje en un color y la respuesta en otro color.

    :param message: El mensaje a mostrar al usuario.
    :param color_message: El color en el que se mostrará el mensaje.
    :param color_input: El color en el que se mostrará la respuesta del usuario.

    :return: La respuesta del usuario.
    """

    # Coloreamos el mensaje.
    message_colored = f"{color_message}{message}{color_input}"

    # Solicitamos el input al usuario.
    user_input = input(message_colored)
    print(COLORS.DEFAULT, end="")

    # Devolvemos la respuesta del usuario con el color por defecto.
    return f"{user_input}"


def clear_screen():
    """
    Esta función borra el contenido actual en la consola/terminal.

    Este método funciona en diferentes sistemas operativos (Windows y Unix/Linux/MacOS), 
    y utiliza comandos del sistema específicos para cada uno de ellos para borrar la pantalla.

    Ejemplo de uso:
    >>> clear_screen()
    # Borra el contenido de la consola
    """

    # `os.name` es `'nt'` si el sistema operativo es Windows
    # Entonces, si estamos en Windows, usamos el comando `'cls'` para borrar la pantalla
    # De lo contrario, suponemos que estamos en un sistema tipo Unix (Linux/MacOS), 
    # por lo que usamos el comando `'clear'` para borrar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    print_title("Funciones de consola", COLORS.RED)
    name = input_color("Escriba su nombre: ", COLORS.YELLOW, COLORS.BLUE)
    print_color(f"Hola, {name}", COLORS.MAGENTA)
