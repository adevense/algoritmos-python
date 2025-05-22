'''
Dada uma lista de nomes, retorne uma nova lista com os nomes em letras mai´usculas.
'''
def lista_maiusculas(lista):
    lista_maiusculas = []
    for i in lista:
        lista_maiusculas.append(i.upper())
    return lista_maiusculas
# Testando a funcao
lista = ['joao', 'maria', 'jose', 'ana']
print(f'Lista original: {lista}')
print(f'Lista com nomes em maiusculas: {lista_maiusculas(lista)}')
