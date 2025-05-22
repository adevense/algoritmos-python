'''
Separe uma lista de n´umeros em duas: uma com pares e outra com ´ımpares.
'''
def separa_pares_impares(lista):
    lista_pares = []
    lista_impares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    return lista_pares, lista_impares
# Testando a funcao
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Lista original: {lista}')
pares, impares = separa_pares_impares(lista)
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')