"""
Exercício 4 - Números Pares até N
Crie um programa que imprima todos os números pares até o número fornecido pelo
usuário usando laços.
"""
valor_limite = int(input("Insira o valor limite: "))
contador = 1

while contador <= valor_limite:
    if contador % 2 == 0: # se o contador dividido por 2 o resto for diferente de zero print contador
      print(contador)
    contador+= 1