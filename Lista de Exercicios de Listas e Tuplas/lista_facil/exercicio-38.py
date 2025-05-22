'''
Implemente uma fun¸c˜ao que receba uma lista e retorne os elementos na ordem
inversa.
'''

def lista_inversa(lista):
    """
    Retorna os elementos de uma lista na ordem inversa.
    :param lista: Lista a ser invertida
    :return: Lista com os elementos na ordem inversa
    """
    return lista[::-1]
# Testando a funcao
lista = [1, 2, 3, 4, 5]
print(f'Lista original: {lista}')
print(f'Lista na ordem inversa: {lista_inversa(lista)}')