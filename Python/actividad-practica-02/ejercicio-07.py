"""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 
valores de la lista.

"""

square = lambda number: number ** 2

stop_number = int(input("¿Hasta qué número quieres crear la lista? "))
numbers = [i for i in range(1, stop_number + 1)]
print(f"La lista de números es:\n{numbers}")

square_numbers = list(map(square, numbers))
print(f"\nLa lista de números elevada al cuadrado es:\n{square_numbers}")