"""
Exercício 3 - Contagem Regressiva
Crie um programa que faça uma contagem regressiva, do número fornecido até 0, utilizando
laços de repetição.    
"""

valor_contagem = int(input("Insira o valor da contagem regressiva: "))
contador = 0

while contador <= valor_contagem:
    print(valor_contagem)
    valor_contagem -= 1