validos=0
tentativas=0

while validos <5:
    num=int(input('insira um valor inteiro e positivo: '))
    tentativas+=1
    
    if num <2 or num % 2 == 0 and num != 2:
        print('rejeitado')
        
    div =2
    eh_primo = True
    while div * div <= num:
        if num % div == 0:
            eh_primo = False
            break
        div+=1
        
    if eh_primo and num % 2 != 0:
        print('valido')
        validos+=1
    else:
        print('Rejeitado')
        
print('Portal liberado')