'''
Solicite 5 numeros ao usuario e armazene em uma lista. Em seguida, imprima o
maior e o menor numero.
'''
lista=[]
i=0
while i <5:
    lista1=int(input("digite o numero: "))
    lista.append(lista1)
    i+=1
maior_numero = max(lista)
menor_numero = min(lista)
print(f'O menor número é: {menor_numero} e o maior é {maior_numero}')