# Listas (List).
my_list = [1, 2, 3, 76, 45, 99]
names = ["Agustín", "Lorena", "Adrián", "Carlitos"]
other = ["Agustín", 46, True, ["Python", "JavaScript"]]

print("Listas:\n" + "*"*7)
# Recorriendo la lista.
for item in other:
    print(item)

# Accediendo a un item de la lista.
print(f"{my_list[2]} es el segundo elemento de la lista: {my_list}")


# Tuplas (Tuples). Estas son inmutables.
my_tuple = ("Agustín", "Comolli")
# Desempaquetando tuplas.
first_name, last_name = my_tuple
print("\nTuplas:\n" + "*"*7)
print(my_tuple)
print(f"Nombre: {first_name}\nApellido: {last_name}")


# Diccionarios (Dict).
contact = {
    "name": "Agustín",
    "age": 46,
    "email": "agustincomolli@yahoo.com.ar",
    "is_male": True,
    "skills": ["HTML", "CSS", "JavaScript", "Python"]
}

print("\nDiccionarios:\n" + "*"*13)
# Recorriendo un diccionario por clave y valor.
for key, value in contact.items():
    print(f"{key}: {value}")


# Funciones de listas (max, min, sum)
print("\nFunciones de listas:\n" + "*"*20)
numbers = [1, 23, 54, 4, 7, 99]
print(f"La lista: {numbers}")
print(f"El valor más grande de la lista es: {max(numbers)}")
print(f"El valor más chico de la lista es: {min(numbers)}")
print(f"El total de la suma de los números es: {sum(numbers)}")


# Agregar elementos a una lista.
print("\nAgregando elementos:\n" + "*"*20)
skills = ["HTML", "CSS"]
print(f"Mis habilidades son: {skills}")
# Agregando al final de la lista.
skills.append("Python")
print(f"Mis habilidades son: {skills}")
# Agregando en una posición determinada.
skills.insert(2, "JavaScript")
print(f"Mis habilidades son: {skills}")


# Eliminando elementos de una lista.
print("\nEliminando elementos:\n" + "*"*20)
print(f"Mis habilidades son: {skills}")
# Eliminando el último elemento.
skills.pop()
print(f"Mis habilidades son: {skills}")
# Eliminando en una posición determinada.
skills.pop(0)
print(f"Mis habilidades son: {skills}")
# Eliminando un valor determinada.
skills.remove("CSS")
print(f"Mis habilidades son: {skills}")