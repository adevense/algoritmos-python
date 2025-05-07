'''pensando em listas de 50 alunos, onde serão lidas (random) 4 notas (0 - 100)
Mostre:
    a % de alunos aprovados
    a % de alunos reprovados

    imprima os 5 primeiros alunos com média mais alta 
    imprima os 5 piores alunos
    imprima a nota mais alta
'''

import random #ctrl + clique em random

numero_de_alunos = 50
numero_de_notas = 4
lista_de_alunos = []

for i in range(numero_de_alunos):
    notas_do_aluno = [random.randint(0, 100) for i in range(numero_de_notas)]
    lista_de_alunos.append(notas_do_aluno)


print(lista_de_alunos[0]) 

for indice in range(numero_de_alunos):
    lista_de_alunos[indice]

