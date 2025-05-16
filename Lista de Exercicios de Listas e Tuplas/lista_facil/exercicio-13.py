'''
Crie uma lista com os numeros de 1 a 10 usando range() e imprima somente os pares.
'''
lista=[]
for i in range(11):
    lista.append(i)
lista.pop(0)
for i1 in range(10):
    if lista[i1] % 2 == 0:
        print(lista[i1])