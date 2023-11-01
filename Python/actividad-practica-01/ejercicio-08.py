"""
Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 
7 (sólo hay que comprobar si lo es por uno de los cuatro)

"""

number = int(input("Ingrese un número: "))
if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    print(f"El número {number} es divisible por alguno de estos números: 2, 3, 5 0 7")