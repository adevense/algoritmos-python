'''
Crie uma fun¸c˜ao que retorne o segundo maior n´umero de uma lista
'''

def segundo_maior(lista):
    """
    Retorna o segundo maior n´umero de uma lista.
    :param lista: Lista de n´umeros
    :return: Segundo maior n´umero da lista
    """
    if len(lista) < 2:
        return None
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    return lista_unica[1]
# Testando a funcao
lista = [1, 2, 3, 4, 5]
print(f'Lista: {lista}')
print(f'Segundo maior n´umero: {segundo_maior(lista)}')