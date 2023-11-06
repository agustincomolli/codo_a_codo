"""
Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver True o False según
la fecha sea correcta o no. Realizar también un programa para verificar el
comportamiento de la función.

"""


def check_is_date(day:int, month:int, year:int):
    if year >= 1:
        if month >= 1 and month <= 12:
            if month == 2 and day >= 1 and day <= 29:
                return True
            elif month in [1, 3, 5, 7, 8, 10, 12] and day >= 1 and day <= 31:
                return True
            elif month != 2 and day >= 1 and day <= 30:
                return True
    
    return False


date = input("Ingrese una fecha cuyos números estén separados por un guión '-': ")
day, month, year = date.split("-")
day = int(day)
month = int(month)
year = int(year)
if check_is_date(day, month, year):
    print("Es una fecha válida")
else:
    print("No has ingresado una fecha válida.")