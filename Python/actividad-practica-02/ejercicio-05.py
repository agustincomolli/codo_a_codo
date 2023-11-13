"""
Crear una función lambda que devuelva el cuadrado de un valor recibido cómo 
parámetro. Desarrollar además un programa para verificar el comportamiento de 
la función.

"""


square = lambda number: number ** 2
print("Función LAMBDA")
my_number = int(input("Ingrese un número: "))
print(f"El número {my_number} elevado al cuadrado es {square(my_number)}")