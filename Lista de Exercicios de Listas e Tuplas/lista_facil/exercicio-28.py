'''
Crie uma fun¸c˜ao que receba uma lista e retorne a soma de todos os elementos
num´ericos.
'''

def soma_lista(lista):
    soma = 0
    for i in lista:
        if isinstance(i, (int, float)):
            soma += i
    return soma
# Testando a funcao
lista = [1, 2, 3, 4, 5]
print(f'Lista original: {lista}')
print(f'Soma dos elementos numericos: {soma_lista(lista)}')