"""
Una clase es una plantilla o molde para crear objetos en la programación 
orientada a objetos. Define las propiedades y comportamientos que los objetos 
de esa clase tendrán. Las propiedades son variables que almacenan datos, 
mientras que los comportamientos son funciones que pueden realizar acciones o 
manipular esos datos. Los objetos creados a partir de una clase se denominan 
instancias y pueden acceder a las propiedades y comportamientos definidos en 
la clase. Esto permite crear y manipular múltiples objetos con las mismas 
características y funcionalidades.
"""


class Person:
    name = ""
    age = 0

    # Un método constructor es un tipo especial de método en una clase que se
    # utiliza para inicializar los objetos de esa clase.
    def __init__(self, name: str, age: int):
        """
        Inicializa una nueva instancia de la clase con el nombre y la edad proporcionados.

        Args:
            name (str): El nombre de la persona.
            age (int): La edad de la persona.

        Returns:
            None
        """
        self.name = name
        self.age = age

    def greet(self):
        """
        Imprime un saludo personalizado.
        """
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.")

    def __str__(self):
        """
        Devuelve una representación en forma de cadena del objeto.

        Returns:
            str: La representación en forma de cadena del objeto, incluyendo el nombre y la edad.
        """
        return f"Nombre: {self.name}, Edad: {self.age}"


# Los objetos se crean a partir de la clase y se llaman instancias.
cliente = Person("Agustín", 46)

# Muestro una propiedad del objeto.
print(cliente.name)
# Llamo a un método del objeto. 
cliente.greet()
# Muestro la representación en forma de cadena del objeto.
print(cliente)
