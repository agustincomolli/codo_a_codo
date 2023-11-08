from modulo import input_colorfully, print_colorfully, COLORS

name = input_colorfully("Ingrese su nombre: ", COLORS.CYAN, COLORS.BLUE)

print_colorfully(name, COLORS.YELLOW)