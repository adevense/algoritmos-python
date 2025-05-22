'''
Inverta os elementos de uma lista sem usar o m´etodo reverse.
'''

def inverter_lista(lista):  
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida
# Testando a funcao
lista = [1, 2, 3, 4, 5]
print(f'Lista original: {lista}')
print(f'Lista invertida: {inverter_lista(lista)}')
