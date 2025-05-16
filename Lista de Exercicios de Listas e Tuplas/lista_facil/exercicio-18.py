'''
Verifique se o numero 7 esta presente na lista [3, 6, 9, 12].
'''

lista=[3, 6, 9, 12]

for i in range(4):
    if lista[i] == 7:
        print(f' 7 está presente na posição: {i}, numero: {lista[i]}')
    else:
        print(f' 7 não está presente na posição: {i}, numero: {lista[i]}')