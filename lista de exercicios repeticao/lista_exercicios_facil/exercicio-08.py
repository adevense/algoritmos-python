"""
Exercício 8 - Série Incremental
Faça um programa que imprima a seguinte série incremental, com base num valor n:
"""
valor_maximo = int(input("Digite o valor do incremento: "))
contador = 1
valor_incremento = ""
while contador <= valor_maximo:
    valor_incremento =valor_incremento + str(contador)
    contador+=1
    print(valor_incremento)
