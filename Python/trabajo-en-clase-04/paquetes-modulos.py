from interface_handler import *

clear_screen()
print_title("Importando módulos propios:", COLORS.YELLOW)
name = input_color("Ingrese su nombre: ", COLORS.CYAN, COLORS.BLUE)
print_color(f"\nHola, {name}. Bienvenido a Python", COLORS.MAGENTA)