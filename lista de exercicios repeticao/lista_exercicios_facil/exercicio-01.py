"""
Exercício 1 - Soma dos números inteiros
Faça um programa usando laços que some todos os números inteiros de 1 até n fornecido
pelo usuário.
Exemplo:
Entrada: 5
Saída: 15
"""

contador_limite = float(input('digite o numero: '))
contador = 1
soma = 0
while contador <= contador_limite:
    soma += contador
    contador += 1
print(soma)
