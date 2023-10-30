# Esto es un comentario en Python
print("¡Hola mundo!")

# Definiendo una función.


def add_two_numbers(number_1, number_2):
    return number_1 + number_2


# Probando funciones y usando las fstrings para mostrar variables.
print(
    f"Probando la función add_two_numbers con 2 + 5 = {add_two_numbers(2, 5)}")

# Operadores de Python
matematical_operators = """
Suma                2 + 3
Resta               5 - 7
Multiplicación      3 * 4
División            12 / 4
Módulo              7 % 5
División entera     9 // 5
Exponenciación      2**3
"""
print(f"\nOperadores matemáticos: {matematical_operators}")

# Operadres lógicos
logicals_operators = """
Y       and
O       or
No      not
"""
print(f"Operadores lógicos: {logicals_operators}")


# Operadores de comparación
comparison_operators = """
mayor que           >
menor que           <
mayor o igual que   >=
menor o igual que   <=
distinto            !=
"""
print(f"Operadores de comparación: {comparison_operators}")

# Pedir datos al usuario.
your_name = input("Ingrese su nombre: ")
print(f"¡Hola {your_name}!")