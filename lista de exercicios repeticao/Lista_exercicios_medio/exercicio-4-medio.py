'''
Exercício 4: Triângulo Numérico Invertido
Faça um programa que, utilizando laços, imprima o seguinte padrão numérico invertido
baseado no número inteiro informado pelo usuário.
Exemplo:
Entrada:
5
Saída:
12345
1234
123
12
1
'''
num = int(input('Insira o valor: '))

while num >= 1:
    linha = ""
    for i in range(1, num + 1):
        linha += str(i)
    print(linha)
    num -= 1