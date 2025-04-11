"""
Exercício 2 - Tabela de Multiplicação
Faça um programa que exiba a tabuada de multiplicação do número fornecido pelo usuário
(de 1 a 10).
"""
valor_tabuada = int(input("valor da tabuada: "))
contador = 1
while contador <= 10:
    print(valor_tabuada," X ", contador,"= ", valor_tabuada*contador)
    contador += 1