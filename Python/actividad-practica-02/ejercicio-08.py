"""
Eliminar de una lista de palabras que se encuentren en una segunda lista. 
Imprimir la lista original, la lista de palabras a eliminar y la lista 
resultante.

"""

word_list = ["manzana", "papá", "verde", "perro", "automovil", "computadora", "árbol", "agua"]
words_to_delete = ["papá", "verde", "computadora"]
new_word_list = word_list[::]
delete_word = lambda x: new_word_list.remove(x)
list(map(delete_word, words_to_delete))
print(f"Lista original:\n{word_list}")
print(f"\nLista de palabra a eliminar:\n{words_to_delete}")
print(f"\nLista resultante:\n{new_word_list}")