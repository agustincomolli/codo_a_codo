"""
Escribe un programa que pida dos números y escriba en la pantalla cual es el 
mayor.
"""

number_1 = int(input("Número 1: "))
number_2 = int(input("Número 2: "))

if number_1 > number_2:
    print(number_1, "es mayor que", number_2)
else:
    print(number_2, "es mayor que", number_1)

