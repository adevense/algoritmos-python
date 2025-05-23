'''
Dicionarios
-é uma lista de associações compostas por uma chave "unica"
-são mutáveis

sintaxe:
dicionario = {'a': 1, 'b':2,'c':3 }

'''

'''
dic = {'nome':'beto', 'nome2':'ana', 'nome3':'vitor'}

dic['nota'] = 7.80


#usado para debug
print(dic)

#dic = {(1,2,3):'beto'} #pode!

itens = dic.items()
chaves = dic.keys()
valores = dic.values()


print(f'itens: {itens}')
print(f'chaves: {chaves}')
print(f'valores: {valores}')

#get

for i,j in dic.items():
    print(f'i={i} j={j}')
   
'''
    
'''
leia o nome de 5 pessoas e armazene em um dicionario
'''
'''
pessoas = {}
for i in range(5):
    nome = input('digite o nome: ')
    pessoas[i] = nome

print(f'nome: {pessoas}')
'''

'''
crie um programa para gerar um dicionario com 20 números inteiros e mostre a soma de todos os elementos
'''

'''
import random

numeros = {}
soma = 0

# Gera o dicionário com 20 números inteiros
for i in range(20):
    numeros[i] = random.randint(1, 50)
    soma+=numeros.get(i)

print(f'Dicionário: {numeros}')
print(f'Soma de todos os elementos: {soma}')
'''

#comprensão de listas
'''
lista =[i**2 for i in range(5)]# cria uma lista de [0,1,2,3,4]
print(lista)
'''
#pesquisa como trabalhar com comprensão de listas
'''
(compreensão de listas) são uma das características mais poderosas e elegantes do Python, permitindo criar listas de forma concisa e legível. Elas oferecem uma sintaxe mais compacta do que os loops for tradicionais para muitas operações de criação e transformação de listas.

A estrutura básica de uma compreensão de lista é:

Python

[expressao for item in iteravel if condicao]
Onde:

expressao: É a operação que você deseja aplicar a cada item. O resultado desta expressão será adicionado à nova lista.
item: É a variável que representa cada elemento do iteravel.
iteravel: É uma sequência (como uma lista, tupla, string, range, etc.) sobre a qual você deseja iterar.
if condicao (opcional): É uma condição de filtro. Se presente, a expressao só será avaliada e adicionada à nova lista se a condicao for verdadeira.
Vamos explorar com exemplos:

1. Criação Básica de Listas
Exemplo com for tradicional:

Python

quadrados = []
for i in range(1, 6):
    quadrados.append(i * i)
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
Exemplo com List Comprehension:

Python

quadrados = [i * i for i in range(1, 6)]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
Perceba como a compreensão de lista é muito mais compacta e legível.

2. Filtragem de Elementos (usando if)
Exemplo com for tradicional:

Python

pares = []
for numero in range(1, 11):
    if numero % 2 == 0:
        pares.append(numero)
print(pares)  # Saída: [2, 4, 6, 8, 10]
Exemplo com List Comprehension:

Python

pares = [numero for numero in range(1, 11) if numero % 2 == 0]
print(pares)  # Saída: [2, 4, 6, 8, 10]
Aqui, a cláusula if filtra os números, incluindo apenas aqueles que são pares.

3. Aplicação de Função/Transformação
Exemplo com for tradicional:

Python

palavras = ["olá", "mundo", "python", "programação"]
maiusculas = []
for palavra in palavras:
    maiusculas.append(palavra.upper())
print(maiusculas) # Saída: ['OLÁ', 'MUNDO', 'PYTHON', 'PROGRAMAÇÃO']
Exemplo com List Comprehension:

Python

palavras = ["olá", "mundo", "python", "programação"]
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas) # Saída: ['OLÁ', 'MUNDO', 'PYTHON', 'PROGRAMAÇÃO']
4. Condicionais na Expressão (if/else)
Você pode ter uma condicional na parte da expressão para decidir o que colocar na lista com base em uma condição. Neste caso, o if e else vêm antes do for.

Python

numeros = [1, 2, 3, 4, 5, 6]
par_ou_impar = ["par" if n % 2 == 0 else "ímpar" for n in numeros]
print(par_ou_impar) # Saída: ['ímpar', 'par', 'ímpar', 'par', 'ímpar', 'par']
5. List Comprehensions Aninhadas
Você pode aninhar compreensões de lista para trabalhar com estruturas de dados mais complexas, como listas de listas (matrizes).

Exemplo: Criação de uma matriz 3x3

Python

matriz = [[coluna for coluna in range(3)] for linha in range(3)]
print(matriz)
# Saída: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
Exemplo: Achatar uma matriz (flatten)

Python

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_achatada = [numero for linha in matriz for numero in linha]
print(lista_achatada) # Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9]
A ordem dos for loops é importante e segue a lógica dos loops aninhados tradicionais: o for mais à direita é o mais interno.
'''

'''
Ex3 - Crie um programa para ler o nome, a matricula e as 4 notas de 5 alunos e armazene em um dicionario
as notas podem ser geradas aleatoriamente entre 0 e 10
a)mostrar o aluno com a maior média
b) a % de alunos com média maior que 8
c) a % de alunos que estariam reprovados (média < 4)
'''
from random import randint
dicionario = {}
notas = []
for i in range(5):
    nome = input('Digite o nome: ')
    matricula = i
    notas = [(randint(0, 10)) for _ in range(4)]
    dicionario[matricula] = {'nome': nome, 'notas': notas, 'media': sum(notas)/len(notas)}

maior_media = dicionario[0]['media']
aluno_maior_media = dicionario[0]['nome']

for a in range(5):
    if dicionario[a]['media'] > maior_media:
        maior_media = dicionario[a]['media']
        aluno_maior_media = dicionario[a]['nome']

alunos_maior_8 = sum(1 for aluno in dicionario.values() if aluno['media'] > 8)
porcentagem_maior_8 = (alunos_maior_8 / 5) * 100


print(f'Aluno com maior média: {aluno_maior_media} com média {maior_media:.2f}')
print(f'a porcentagem de alunos com a média maior que 8 é: {porcentagem_maior_8:.2f}%')


    