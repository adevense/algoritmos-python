#tipos de variaveis
idade = 10
pi = 3.14
nome = 'inacio.azevedo'
status = True

#ler 4 notas e fazer media
nota_01 = float(input('digite a nota 1: '))
nota_02 = float(input('digite a nota 2: '))
nota_03 = float(input('digite a nota 3: '))
nota_04 = float(input('digite a nota 4: '))

print('A média é: ',(nota_01 + nota_02 + nota_03 + nota_04)/4)
#ler 4 notas e fazer media ponderada
print('A média ponderada é: ',(nota_01*0.2 + nota_02*0.1 + nota_03*0.4 + nota_04*0.3))
print(f'nota 1: {nota_01*0.2} nota 2: {nota_02*0.1} nota 3: {nota_03*0.4} nota 4: {nota_04*0.3}')