try:
    number = int(input("Ingrese un número: "))
except Exception as error:
    print(f"ERROR: No has ingresado un número.\n{error}")
    exit()

print(f"El número ingresado es {number}")