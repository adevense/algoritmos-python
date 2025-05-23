energia_total=0
contador_numero=0

while energia_total<100:
    num=int(input('insira o valor: '))
    contador_numero+=1
    
    if num >= 0:
        energia_total +=num
        print('energia aumentada em',num,'Total: ',energia_total)
    else:
        energia_total-= num
        print('energia drenada em',num,'Total: ',energia_total)
print('balança estabilizada')
print(f'Total = {energia_total}')
print(f'Total de numeros digitados = {contador_numero}')