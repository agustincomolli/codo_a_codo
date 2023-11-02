"""
Pide una nota (número). Muestra la calificación según la nota: 
     0-3: Muy deficiente 
     3-5: Insuficiente 
     5-6: Suficiente 
     6-7: Bien 
     7-9: Notable 
     9-10: Sobresaliente

"""

calification = float(input("Ingrese la nota del alumno: "))

if calification < 0 or calification > 10:
    print("ERROR: El valor ingresado debe estar en el rango de 0 a 10")
elif calification >= 0 and calification <= 3:
    print("Muy deficiente")
elif calification >= 3 and calification <= 5:
    print("Insuficiente")
elif calification >= 5 and calification <= 6:
    print("Suficiente")
elif calification >= 6 and calification <= 7:
    print("Bien")
elif calification >= 7 and calification <= 9:
    print("Notable")
elif calification >= 9 and calification <= 10:
    print("Sobresaliente")