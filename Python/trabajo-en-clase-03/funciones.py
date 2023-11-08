# Funciones en Python.

# Declarando una función.
def greet():
    print("¡Bienvenido a Python!")


# Llamando a una función.
print("Función simple:\n" + "*" * 15)
greet()


# Funciones con parámetros.
def greet_name(name):
    print(f"¡Hola, {name}! Bienvenido a Python.")


print("\nFunciones con parámetros:\n" + "*" * 25)
greet_name("Agustín")


# Funciones con parámetros que tienen valores opcionales.
def greet_optional(name="desconocido"):
    print(f"¡Hola, {name}! Bienvenido a Python.")


print("\nFunciones con parámetros opcionales:\n" + "*" * 36)
greet_optional()


# Devolviendo valores.
def add_two_numbers(number_1, number_2):
    return number_1 + number_2


print("\nDevolviendo valores:\n" + "*" * 20)
print(f"La suma de 34 + 65 es = {add_two_numbers(34, 65)}")


# Funciones lambda.
def square(number): return number ** 2


print("\nUsando funciones lambda:\n" + "*" * 24)
print(f"El cuadrado de 8 es {square(8)}")


# Funciones map.
print("\nFunción map:\n" + "*" * 12)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{list(map(lambda number: number ** 2, numbers))}")
