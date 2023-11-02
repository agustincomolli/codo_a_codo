"""
Haz un programa que escriba una pirámide inversa de los números del 1 al 
número que indique el usuario de la siguiente forma (suponiendo que indica 6): 
666666 
55555 
4444 
333 
22 
1
"""

number = int(input("Ingresa un número: "))

for i in range(number, 0, -1):
    print(str(i) * i)