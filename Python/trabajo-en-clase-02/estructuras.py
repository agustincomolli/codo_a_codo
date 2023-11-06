# Estructuras de control.
your_age = int(input("\nIngrese su edad: "))
if your_age >= 18 and your_age < 65:
    print("Eres mayor de edad")
elif your_age >= 65:
    print("Eres un anciano")
else:
    print("Eres un niño")


# Ciclo de repetición while.
counter = 1
print("\nContando hasta 10 con while:")

while counter < 10:
    print(counter, end=", ")
    counter += 1

print(counter)

# Ciclo de repetición for.
print("\nContando hasta 10 con for:")

for counter in range(1, 10):
    print(counter, end=", ")

print(counter)

# Recorriendo una lista.
student_califications = [4, 6, 6, 10, 7, 10, 9]
results = ", "
print("\nCalificaciones del estudiante:")
for calification in student_califications:
    print(str(calification).zfill(2))  #zfill(2) rellena con 0 para que la salida tenga 2 caractres.