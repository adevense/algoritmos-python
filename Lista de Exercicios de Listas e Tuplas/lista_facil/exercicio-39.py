'''
Faca a uniao de duas listas sem usar o operador +
'''

def uniao_listas(lista1, lista2):

    lista_uniao = []
    for elemento in lista1:
        if elemento not in lista_uniao:
            lista_uniao.append(elemento)
    for elemento in lista2:
        if elemento not in lista_uniao:
            lista_uniao.append(elemento)
    return lista_uniao
# Testando a funcao
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Uniao das listas: {uniao_listas(lista1, lista2)}')
