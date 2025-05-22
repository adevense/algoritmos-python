'''
Dada uma lista de strings, crie uma nova lista com o tamanho (n´umero de caracteres)
de cada string
'''

def tamanho_strings(lista):
    lista_tamanhos = []
    for i in lista:
        lista_tamanhos.append(len(i))
    return lista_tamanhos
# Testando a funcao
lista = ['joao', 'maria', 'jose', 'ana']
print(f'Lista original: {lista}')
print(f'Lista com tamanhos: {tamanho_strings(lista)}')