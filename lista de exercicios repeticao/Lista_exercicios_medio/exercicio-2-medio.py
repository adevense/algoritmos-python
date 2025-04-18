'''
Exercício 2: Número Perfeito
Faça um programa usando apenas laços que determine se um número informado pelo
usuário é um número perfeito. Um número é perfeito quando é igual à soma dos seus
divisores próprios (exceto ele mesmo).
Exemplo:
Entrada:
6
Saída:
Número Perfeito
'''
numero_perfeito=0
i=1
num=int(input("insira o valor: "))

while i <num:
    if num % i==0:
        numero_perfeito +=i
        print(i,numero_perfeito)
    i+=1
if numero_perfeito == num:
    print(f'O número {num} é perfeito')
else:
    print(f'O número {num} não é perfeito')