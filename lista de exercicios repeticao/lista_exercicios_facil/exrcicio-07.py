"""
Exercício 7 - Contar Divisores
Faça um programa que conte quantos divisores inteiros um número inteiro positivo possui
utilizando laços.
"""

valor_divisivel= int(input("Digite o valor: "))
contador = 1
soma=0
while contador <= valor_divisivel:
    if valor_divisivel % contador == 0:
        soma +=1
        #print(contador) para verificar quais os numeros são divisores
    contador+=1
print(soma)