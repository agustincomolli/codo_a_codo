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


def print_colorfully(message: str, color: str, end: str = "\n") -> None:
    """
    Imprime un mensaje en un color especifico.

    :param message: El mensaje a imprimir.
    :param color: El color en el que se imprimirá el mensaje.
    :param end: El caracter que se imprimirá al final del mensaje. Por defecto es '\n'.
    """

    # Usamos la secuencia de escape del color definido en la clase COLORS.
    print(f"{color}{message}{COLORS.DEFAULT}", end=end)


def input_colorfully(message: str, color_message: str, color_input: str) -> str:
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
    user_input = input(message_colored) + COLORS.DEFAULT

    # Devolvemos la respuesta del usuario con el color por defecto.
    return f"{user_input}"


if __name__ == "__main__":
    print_colorfully("Hola", COLORS.GREEN)
    name = input_colorfully("Type your name: ", COLORS.YELLOW, COLORS.BLUE)
    print_colorfully(name, COLORS.MAGENTA)