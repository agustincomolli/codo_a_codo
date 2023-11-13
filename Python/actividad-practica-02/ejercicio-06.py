"""
Crear una función lambda para comprobar si un número es par o impar. 
Desarrollar además un programa para verificar el comportamiento de la función.

"""

is_pair = lambda number: (number % 2 == 0)

print("Función LAMBDA")
my_number = int(input("Ingrese un número: "))
if is_pair(my_number):
    print(f"El número {my_number} es par")
else:
    print(f"El número {my_number} es impar")