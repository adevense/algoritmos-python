progs=['Yes','Genesis','Pink Floyd','ELP']
#incluir novo elemento
progs.append('Guns')

print(progs)

#trocar o último elemento

progs[-1]='novo elemento'

#ordenar
progs.sort()

#inverter a lista
progs.reverse()

# remover elemento da lista

#Pesquisar:
#pop pop():
'''
Remove um elemento de uma lista com base no índice do elemento.
Por padrão, se nenhum índice for especificado, pop() remove e retorna o último elemento da lista.
Retorna o valor do elemento removido.
Se o índice especificado estiver fora dos limites da lista, um erro IndexError será levantado.
'''
#remove
'''
Remove a primeira ocorrência de um elemento específico na lista.
Não retorna nenhum valor (retorna None).
Se o elemento não for encontrado na lista, um erro ValueError será levantado.
'''
#enumerate
'''
A função enumerate() adiciona um contador a um iterável e retorna-o como um objeto enumerado.
Em outras palavras, ela retorna tuplas contendo o índice e o valor de cada item no iterável.
É frequentemente usado em loops for quando você precisa tanto do índice quanto do valor dos elementos.
'''
#zip
'''
A função zip() é usada para combinar elementos de duas ou mais iteráveis (listas, tuplas, etc.) em um único iterável de tuplas.
Ela "zipa" os elementos lado a lado, criando tuplas que contêm os elementos correspondentes de cada iterável.
O iterável resultante tem o comprimento do iterável mais curto.
É muito útil para iterar sobre múltiplos iteráveis simultaneamente.
'''


for i,p in enumerate(progs):
    print(f'posição {i} e elemento = {p}')



#dada as seguintes listas [A,B,C] e [D,E,F] como poderiamos junta-las?
listaA=['A','B','C']
listaB=['D','E','F']

listaA += listaB
print(listaA)

'''pensando em listas de 50 alunos, onde serão lidas (random) 4 notas (0 - 100)
Mostre:
    a % de alunos aprovados
    a % de alunos reprovados

    imprima os 5 primeiros alunos com média mais alta 
    imprima os 5 piores alunos
    imprima a nota mais alta
'''

