'''
Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a
ordem.
'''
def lista_unicos(lista):
    lista_unicos = []
    for i in lista:
        if i not in lista_unicos:
            lista_unicos.append(i)
    return lista_unicos
# Testando a funcao 
lista = ['joao', 'maria', 'joao', 'jose', 'maria', 'ana']
print(f'Lista original: {lista}')
print(f'Lista com elementos unicos: {lista_unicos(lista)}')
