# mysql-connector-python --> Librería para conectarse a bases de datos MySQL

# Importando los módulos necesarios
from interface_handler import *
import mysql.connector


def connect_db():
    """
    Esta función se usa para establecer una conexión con la base de datos.

    Returns:
        object: Un objeto que representa la conexión a una base de datos MySQL.
    """
    return mysql.connector.connect(
        host="viaduct.proxy.rlwy.net",
        port=51991,
        user="root",
        password="eggh-22cgFb-gBg4aH6DfFAC14edeFC6",
        database="railway",
    )


def insert_person(name: str, age: int):
    """
    Esta función inserta a una nueva persona en la base de datos.

    Args:
        name (str): El nombre de la persona.
        age (int): La edad de la persona.
    """
    conection = connect_db()  # Conexión del objeto con la base de datos
    try:
        cursor = conection.cursor()
        # Se insertan los datos en la tabla de personas
        sql_insert = f"INSERT INTO railway.persons (name, age) VALUES ('{
            name}', {age});"
        cursor.execute(sql_insert)
        conection.commit()  # se guardan los cambios
    except Exception as error:
        # Imprime cualquier error que ocurra durante el proceso
        print(color_text("ERROR:", COLORS.RED),
              f"No se ha podido insertar el registro.\n{error}")
    finally:
        conection.close()  # Cierra la conexión a la base de datos


def delete_person(id: int):
    """
    Esta función se usa para borrar a una persona de la base de datos.

    Args:
        id (int): ID de la persona a eliminar.
    """
    conection = connect_db()  # Se establece la conexión a la base de datos
    try:
        cursor = conection.cursor()
        # Se borra la persona con el id correspondiente
        sql_delete = f"DELETE FROM railway.persons WHERE id = {id};"
        cursor.execute(sql_delete)
        conection.commit()  # Se guardan los cambios en la base de datos
    except Exception as error:
        # Se imprime cualquier error que ocurra durante el proceso
        print(color_text("ERROR:", COLORS.RED),
              f"No se ha podido borrar el registro.\n{error}")
    finally:
        conection.close()  # Cierra la conexión a la base de datos


def update_person(id: int, name: str, age: int):
    """
    Esta función se usa para actualizar los detalles de una persona en la base de datos.

    Args:
        id (int): ID de la persona a actualizar
        name (str): El nuevo nombre de la persona.
        age (int): La nueva edad de la persona.
    """
    conection = connect_db()  # Se establece la conexión a la base de datos
    try:
        cursor = conection.cursor()
        # Se actualiza el nombre y la edad de la persona con el id correspondiente
        sql_update = f"UPDATE railway.persons SET name = '{
            name}', age = {age} WHERE id = {id};"
        cursor.execute(sql_update)
        conection.commit()  # Se guardan los cambios en la base de datos
    except Exception as error:
        # Se imprime cualquier error que ocurra durante el proceso
        print(color_text("ERROR:", COLORS.RED),
              f"No se ha podido actualizar el registro.\n{error}")
    finally:
        conection.close()  # Cierra la conexión a la base de datos


def read_persons():
    """
    Esta función se usa para leer los datos de todas las personas de la base de datos.

    Returns:
        list: Una lista que contiene los datos de todas las personas.
    """
    conection = connect_db()  # Se establece la conexión a la base de datos
    try:
        cursor = conection.cursor()
        # Se recogen todos los detalles de las personas
        sql_select = "SELECT * FROM railway.persons;"
        cursor.execute(sql_select)
        # Se devuelve una lista que contiene todos los detalles
        return cursor.fetchall()
    except Exception as error:
        # Se imprime cualquier error que ocurra durante el proceso
        print(color_text("ERROR:", COLORS.RED),
              f"No se ha podido leer los registros.\n{error}")
    finally:
        conection.close()  # Cierra la conexión a la base de datos


def create():
    """
    Esta función se usa para obtener los detalles de una nueva persona del 
    usuario y guardarla en la base de datos.
    """
    clear_screen()
    print_title("Agregar nueva persona:")
    name = input_color("\nNombre: ", COLORS.DEFAULT, COLORS.CYAN)
    age = int(input_color("Edad: ", COLORS.DEFAULT, COLORS.CYAN))
    insert_person(name, age)  # almacena los detalles en la base de datos


def update():
    """
    Esta función se utiliza para obtener del usuario los detalles actualizados 
    de una persona y guardarlos en la base de datos.
    """
    clear_screen()
    print_title("Actualizar datos de una persona:")
    id = int(input_color("\nId: ", COLORS.DEFAULT, COLORS.CYAN))
    name = input_color("Nombre: ", COLORS.DEFAULT, COLORS.CYAN)
    age = int(input_color("Edad: ", COLORS.DEFAULT, COLORS.CYAN))
    # Almacena los nuevos detalles en la base de datos
    update_person(id, name, age)


def delete():
    """
    Esta función se utiliza para obtener del usuario el ID de una persona y 
    borrarla de la base de datos.
    """
    clear_screen()
    print_title("Eliminar una persona:")
    id = int(input_color("\nId: ", COLORS.DEFAULT, COLORS.CYAN)
             )  # obtiene el id del usuario
    # borra a la persona con el id correspondiente de la base de datos
    delete_person(id)


def view_all():
    """
    Esta función imprime los detalles de todas las personas de la base de datos.
    """
    clear_screen()
    print_title("Listado de personas")
    print()  # insertar una salto de línea
    persons = read_persons()  # obtiene los detalles de todas las personas
    headers = ["Id.", "Nombre", "Edad"]
    print_table(persons, headers)  # imprime los datos de cada persona
    press_enter_to_continue()  # espera a que el usuario presione enter para continuar


# El bucle infinito se mantiene hasta que el usuario decida salir
menu = 0
while menu != 5:
    clear_screen()  # limpia la pantalla
    print_title("Bases de datos", COLORS.YELLOW)  # imprime el título

    # Opciones del menú que se muestran al usuario
    print("\n\t1 - Insertar un registro")
    print("\t2 - Actualizar un registro")
    print("\t3 - Eliminar un registro")
    print("\t4 - Listar todas las personas")
    print("\t5 - Salir")
    menu = int(input_color("\nIngrese una opción: ",
               COLORS.DEFAULT, COLORS.CYAN))

    # dependiendo de la opción seleccionada por el usuario, se llama a la función correspondiente
    if menu == 1:
        create()
    elif menu == 2:
        update()
    elif menu == 3:
        delete()
    elif menu == 4:
        view_all()
