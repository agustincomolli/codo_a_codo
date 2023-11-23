"""
Ingresar una frase desde el teclado y usar un conjunto para eliminar las 
palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar 
las palabras ordenadas según su longitud.

"""

phrase = input("Ingrese una frase: ")
print(phrase)
words_set = set(phrase.split())
print(words_set)
words_list = sorted(words_set, key= lambda word: len(word))
print(words_list)