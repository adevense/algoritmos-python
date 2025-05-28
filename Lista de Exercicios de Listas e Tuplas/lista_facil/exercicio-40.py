'''
Implemente uma funcao que conte quantas vezes um valor aparece em uma lista.
'''

def contar_ocorrencias(lista, valor):
    """
    Conta quantas vezes um valor aparece em uma lista.
    :param lista: Lista a ser verificada
    :param valor: Valor a ser contado
    :return: Quantidade de ocorrencias do valor na lista
    """
    
    return lista.count(valor)

# Testando a funcao
lista = [1, 2, 3, 4, 5, 1, 2, 3, 1]
valor = 1
print(f'Lista: {lista}')
print(f'Valor a ser contado: {valor}')
print(f'Quantidade de ocorrencias do valor {valor}: {contar_ocorrencias(lista, valor)}')