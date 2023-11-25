"""
Desarrollar una función eliminar_claves() que reciba como parámetros un 
diccionario y una lista de claves. La función debe eliminar del diccionario todas 
las claves contenidas en la lista, devolviendo el diccionario modificado y un 
valor de verdad que indique si la operación fue exitosa. Desarrollar también un 
programa para verificar su comportamiento.

"""


def delete_keys(dictionary: dict, keys: list) -> dict:
    my_dictionary = dictionary.copy()
    for key in keys:
        if key in my_dictionary.keys():
            my_dictionary.pop(key)
    return my_dictionary


def show_dictionary(dictionary: dict) -> None:
    for key, value in dictionary.items():
        print(f"{key}: {value}")


user_data = {
    "name": "Agustín",
    "last_name": "Comolli",
    "age": 46,
    "email": "agustincomolli@yahoo.com.ar",
    "address": "Rivadavia 340",
    "city": "Cañuelas",
    "province": "Buenos Aires",
}

keys_to_delete = ["age", "address", "city", "province"]

new_user_data = delete_keys(user_data, keys_to_delete)

print("Diccionario original: ")
show_dictionary(user_data)
print("\nNuevo diccionario: ")
show_dictionary(new_user_data)
