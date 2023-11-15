"""
1 - Cargar datos de alumnos
2 - Listar los alumnos cargados
3 - Mostrar la lista de alumnos con notas mayores a 7
4 - Salir del programa

"""


class Student:
    name = ""
    grade = 0

    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade

    def __str__(self) -> str:
        return f"Alumno: {self.name}, Nota: {self.grade}"


def new_student():
    print()
    name = input("Nombre: ")
    grade = int(input("Nota: "))
    return Student(name, grade)


def view_all(students: list):
    print()
    for student in students:
        print("- ", student)

    input("\nPresione ENTER para continuar...\n")


def view_approved(students: list):
    print()
    for student in students:
        if student.grade >= 7:
            print(f"- {student}")

    input("\nPresione ENTER para continuar...\n")


menu = 0
menu_options = ["Cargar datos de alumnos",
                "Listar todos los alumnos",
                "Listar alumnos con notas mayores a 7",
                "Salir"]
students = []

while menu != 4:
    print("Alumnos:\n")
    for index, value in enumerate(menu_options):
        print(f"{index + 1} - {value}")
    print()
    menu = int(input("Ingrese una opción: "))

    if menu == 1:
        students.append(new_student())
    elif menu == 2:
        view_all(students)
    elif menu == 3:
        view_approved(students)
