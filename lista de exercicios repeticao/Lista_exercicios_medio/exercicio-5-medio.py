'''
Exercício 5: MDC de dois números (Euclides simplificado)
Crie um programa usando apenas laços que calcule o MDC (Máximo Divisor Comum)
entre dois números inteiros fornecidos pelo usuário.
Exemplo:
Entrada:
12
18
Saída:
6
'''

n1=int(input('insira o valor: '))
n2=int(input('insira o valor: '))

while n2 !=0:
    resto =n2 %n1
    n1 = n2
    n2 =resto

print(n1)