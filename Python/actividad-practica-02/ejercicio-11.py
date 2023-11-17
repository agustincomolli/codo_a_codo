"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que 
la misma tiene 80 columnas.

"""

from my_console_lib import *

clear_screen()
print_title("Centrar texto en la consola: ", Colors.YELLOW)
line = input_color("\nIngrese un texto: ", color_input=Colors.CYAN)
width, height = get_terminal_size()
print("\n", align_text(line, Align.CENTER, width))