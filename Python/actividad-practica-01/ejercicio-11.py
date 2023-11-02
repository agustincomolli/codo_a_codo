"""
Escribir un programa que nos diga si un número dado es primo (no es divisible 
por ninguno otro número que no sea él mismo o la unidad)

"""

number = int(input("Ingrese un número: "))
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break


if is_prime:
    print(f"El número {number} es un número primo")
else:
    print(f"El número {number} NO es un número primo")