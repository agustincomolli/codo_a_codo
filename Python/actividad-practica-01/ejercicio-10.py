"""
Escribir un programa que escriba en pantalla los divisores de un número dado.

"""

number = int(input("Ingrese un número: "))
for i in range(1,number):
    if number % i == 0:
        print(f"{i}", end=", ")
print(number)