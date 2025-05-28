'''
Crie uma fun¸c˜ao que verifique se uma lista est´a ordenada.
'''

def lista_ordenada(lista):
    return lista == sorted(lista)
# Testando a funcao
lista = [1, 2, 3, 4, 5]
print(f'Lista: {lista}')
print(f'Lista est´a ordenada: {lista_ordenada(lista)}')