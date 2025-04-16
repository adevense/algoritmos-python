'''
1 - Var de controle
2 - Condição de parada
3 - att da var de controle
'''
'''% é divisão por resto( faz a divisão e retorna só o resto da conta)
i % 2 == 0: isso verifica se o resto da divisão é zero
''' 

# 1 Var de controle
i = 0
# Condição de parada
while i <= 10:
    if i % 2 ==0:
        print(f'i = {i}')
    # 3 atualização da variavel de controle
    i += 1 # incremento
    
# Criar u laço com while que dependa da resposta do usuario para continuar o laço
resposta = 's'    

while resposta == 's' or resposta == 'S':
    print('Ainda repetindo')
    resposta = input('Deseja continuar? s / n: ')
    # resposta = resposta.lower() # deixa todos os caracteres minusculos
    # resposta = resposta.uper() # deixa todos os caracteres maiusculos
    while True: # while com true é um loop infinito até chegar em break
        if resposta == 's' or resposta == 'S' or resposta == 'n' or resposta == 'N':
            break
        else:
            resposta = input(print('resposta invalida, tente novamente: '))
print('final')