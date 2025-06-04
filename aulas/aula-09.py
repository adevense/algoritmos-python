'''
lambda function/ função anônima

sintaxe: lambda argumentos: expressão
'''

dobro = lambda x: x * 2

print(f'O dobro de 5 é {dobro(5)}')

soma = lambda x,y: x+y

print(f'O resultado da soma é {soma(5,3)}')


hipotenusa = lambda  a, b: (a**2 + b**2)**0.5

print(f'O valor da hipotenusa é {hipotenusa(5,3)}')

#filter, map

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = list(filter(lambda x: x % 2 == 0,numeros))

print(f'O resultado da filtragem é {pares}')

'''
gere 100n radomicos(20,60) e filtre na facha de 60 acima
gere 100n radomicos(20,60) e filtre os acima da media
gere 100n radomicos(20,60) e filtre na facha de 25 abaixo
'''

from random import randint
nums = [(randint(20, 100)) for _ in range(100)]

acima = list(filter(lambda y: y >= 60,nums))
print(f'O resultado da filtragem é {acima}')

abaixo = list(filter(lambda z:z <= 25,nums))
print(f'O resultado da filtragem é {abaixo}')


media = list(filter(lambda b:b >= sum(nums)/len(nums),nums ))
print(f'O resultado da filtragem é {media}')

#map

quadrado = list(map(lambda x: x **2,numeros))
print(quadrado)

#sorted
pessoas = [('ana',19),('joao',30),('maria',20)]

pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
print(pessoas_ordenadas)

