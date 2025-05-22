'''
Crie uma lista com n´umeros de 1 a 100 e filtre os m´ultiplos de 3.
'''

def filtra_multiplos_de_tres(lista):
    lista_multiplos_de_tres = []
    for i in lista:
        if i % 3 == 0:
            lista_multiplos_de_tres.append(i)
    return lista_multiplos_de_tres
# Testando a funcao
lista = list(range(1, 101))
print(f'Lista original: {lista}')
print(f'Lista com multiplos de 3: {filtra_multiplos_de_tres(lista)}')