"""
Exercício 6 - Fatorial Simples
Faça um programa que calcule o fatorial de um número inteiro positivo usando apenas
laços.
"""

fatorial = int(input("Fatorial de: ") )
resultado=1
contador=1

while contador <= fatorial:
    resultado *= contador
    contador += 1
print(resultado)