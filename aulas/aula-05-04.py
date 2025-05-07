# Tuplas -> são semelhantes as listas, porém são imutaveis: não podemos acresentar ou apagar ou até mesmo fazer novas atribuições

tupla = (1,2,3,4)

t1 = (1,)

print(tupla[0])

for i in tupla:
    print(tupla)

lista = list(tupla)

lista_tupla = ([1,2,3], [2,3],['beto','vitor','rafael'])

# Pesquisa
#set
'''
Um "set" (conjunto) em Python é uma coleção desordenada de itens únicos. Isso significa que:

Desordenado: Os itens em um conjunto não têm uma ordem específica.
Único: Cada item em um conjunto deve ser único; não pode haver duplicatas.
Características principais:

Criação: Você pode criar um conjunto usando chaves {} ou a função set().
'''
#frozenset
'''
Um frozenset é uma variação de um set (conjunto) em Python, com uma diferença crucial: um frozenset é imutável. Isso significa que, uma vez criado, você não pode adicionar, remover ou modificar seus elementos.

Características principais:

Imutabilidade: A principal característica do frozenset é sua imutabilidade. Isso significa que, após a criação, você não pode alterar o conteúdo do conjunto.

Criação: Você cria um frozenset usando a função frozenset(), passando um iterável (como uma lista, tupla ou outro conjunto) como argumento.
'''

#união,interseção e diferença

#o que é range?