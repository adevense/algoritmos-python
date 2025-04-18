'''
Exercício 3: Soma da Série Especial
Crie um programa que calcule o valor da seguinte série até o n-ésimo termo informado
pelo usuário, usando apenas laços:
S=1/1+2/3+3/5+4/7+⋯+n/2n−1

'''
num=int(input('Insia o valor: '))
valor =0
valor_final=0
i=1
while i<=num:
    valor= i/(2*i-1)
    valor_final=valor_final + valor
    i+=1
print(valor_final)