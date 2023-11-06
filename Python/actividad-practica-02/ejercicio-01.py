"""
Desarrollar una función que reciba tres números positivos y devuelva el mayor
de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor
estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y
mostrar el máximo hallado, o un mensaje informativo si éste no existe

"""


def get_max(number_1: int, number_2: int, number_3: int):
    numbers = [number_1, number_2, number_3]
    count = 0
    max_number = max(numbers)

    for number in numbers:
        if number == max_number:
            count += 1

    if count == 1:
        return max_number
    else:
        return -1


number_1 = int(input("Ingrese el número 1: "))
number_2 = int(input("Ingrese el número 2: "))
number_3 = int(input("Ingrese el número 3: "))

max_number = get_max(number_1, number_2, number_3)

if max_number != -1:
    print(f"\nEl número mayor es {max_number}.")
else:
    print("\nNo hay un número mayor estrictamente hablando.")