"""
Escribir una función que reciba una lista como parámetro y devuelva True si la 
lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. 
Desarrollar además un programa para verificar el comportamiento de la función.

"""

def is_sorted(a_list:list) -> bool:
    copy_list = a_list[::]
    copy_list.sort()
    return a_list == copy_list
    

print(is_sorted([1,2,3]))
print(is_sorted(["b", "a"]))