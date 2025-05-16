'''
Solicite nomes ate que o usuario digite ”sair”. Armazene em uma lista e imprima.
'''

lista=[]
nome=''
while nome != 'sair':
    nome=input("digite o texto: ")
    lista.append(nome)
lista.pop()
print(lista)