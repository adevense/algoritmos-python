'''
Solicite ao usuario 10 numeros, armazene em uma lista e remova todos os numeros
pares usando remove.
'''
numeros = []
for i in range(10):
    n = int(input(f'Digite o {i+1}° numero: '))
    numeros.append(n)   
print(f'Lista original: {numeros}')
for i in numeros[:]:
    if i % 2 == 0:
        numeros.remove(i)
print(f'Lista sem os numeros pares: {numeros}')

