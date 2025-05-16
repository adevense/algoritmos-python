'''
Leia 5 numeros do usuario e verifique se cada um deles e maior que 10.
'''
lista=[]
i=0
for i1 in range(5):
    lista1=int(input('Digite o numero: '))
    lista.append(lista1)

while i<5:
    if lista[i]>10:
        print(f'O número: {lista[i]} é maior que 10')
    elif lista[i]==10:
        print(f'O número: {lista[i]} é igual a 10')
    else:
        print(f'O número: {lista[i]} é menor que 10')
    i+=1