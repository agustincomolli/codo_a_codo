# Esto es un comentario en Python.

# Con print mostramos un mensaje en la consola.
print("¡Hola mundo!")


def add_two_numbers(number_1, number_2):  # Definiendo una función
    return number_1 + number_2


# Probando funciones y usando las fstrings para mostrar variables.
print(
    f"Probando la función add_two_numbers con 2 + 5 = {add_two_numbers(2, 5)}")

# Tipos de datos
data_types = """
Enteros         int         3
Reales          float       14.7
cadenas         string      "hola"
lógicos         bool        true
lista           list        [1, "dos", 3.5]
tupla           tuple       (1,2)
diccionario     dict        {"nombre": "Agustín"}
"""
print(f"\nTipos de datos:{data_types}")

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
print(f"Operadores matemáticos: {matematical_operators}")

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

# Con input pedimos datos al usuario.
your_name = input("Ingrese su nombre: ")
print(f"¡Hola {your_name}!")


# Estructuras de control.
your_age = int(input("\nIngrese su edad: "))
if your_age >= 18 and your_age < 65:
    print("Eres mayor de edad")
elif your_age >= 65:
    print("Eres un anciano")
else:
    print("Eres un niño")


# Ciclo de repetición while.
counter = 1
print("\nContando hasta 10 con while:")

while counter < 10:
    print(counter, end=", ")
    counter += 1

print(counter)

# Ciclo de repetición for.
print("\nContando hasta 10 con for:")

for counter in range(1, 10):
    print(counter, end=", ")

print(counter)

# Recorriendo una lista.
student_califications = [4, 6, 6, 10, 7, 10, 9]
results = ", "
print("\nCalificaciones del estudiante:")
for calification in student_califications:
    print(str(calification).zfill(2))  #zfill(2) rellena con 0 para que la salida tenga 2 caractres.