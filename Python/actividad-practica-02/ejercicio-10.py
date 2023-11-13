"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, 
sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que 
permita verificar su funcionamiento.

"""

def is_palindrome(word:str) -> bool:
    for i in range(len(word)//2):
        if word[i] != word[-i -1]:
            return False
    return True


print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("level"))
print(is_palindrome("capicua"))