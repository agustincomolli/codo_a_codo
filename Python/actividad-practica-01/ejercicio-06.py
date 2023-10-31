"""
Escribe un programa que pida 3 números y escriba en la pantalla el mayor de 
los tres.

"""

number_1 = int(input("Número 1: "))
number_2 = int(input("Número 2: "))
number_3 = int(input("Número 3: "))

greater = number_1

if number_2 > greater:
    greater = number_2

if number_3 > greater:
    greater = number_3

print(greater, "es el número más grande.")
