"""
Exercício 5 - Somatório dos Ímpares
Faça um programa que some apenas os números ímpares até um número inteiro positivo
informado pelo usuário usando laços.
"""

valor_limite = int(input("Insira o valor limite: "))
soma_impares = 0
contador = 1

while contador <= valor_limite:
    if contador % 2 != 0:  # Verifica se o número é ímpar (resto da divisão por 2 não é zero)
        soma_impares += contador
    contador += 1

print(f"A soma dos números ímpares até {valor_limite} é: {soma_impares}")