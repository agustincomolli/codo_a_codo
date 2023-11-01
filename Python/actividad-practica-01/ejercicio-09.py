"""
Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay 
que decir todos por los que es divisible).

"""

number = int(input("Ingrese un número: "))
if number % 2 == 0:
    print(f"\t{number} es divisible por 2")
if number % 3 == 0:
    print(f"\t{number} es divisible por 3")
if number % 5 == 0:
    print(f"\t{number} es divisible por 5")
if number % 7 == 0:
    print(f"\t{number} es divisible por 7")