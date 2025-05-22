'''
Crie uma fun¸c˜ao que verifique se uma lista est´a ordenada.
'''

def lista_ordenada(lista):
    """
    Verifica se uma lista est´a ordenada em ordem crescente.
    :param lista: Lista a ser verificada
    :return: True se a lista est´a ordenada, False caso contr´ario
    """
    return lista == sorted(lista)
# Testando a funcao
lista = [1, 2, 3, 4, 5]
print(f'Lista: {lista}')
print(f'Lista est´a ordenada: {lista_ordenada(lista)}')