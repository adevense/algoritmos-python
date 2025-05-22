'''
Crie uma funcao que recebe uma lista e retorna uma nova lista com apenas os
elementos unicos.
'''
def lista_unicos(lista):    
    lista_unicos = []
    for i in lista:
        if i not in lista_unicos:
            lista_unicos.append(i)
    return lista_unicos
# Testando a funcao
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(f'Lista original: {lista}')
print(f'Lista com elementos unicos: {lista_unicos(lista)}')