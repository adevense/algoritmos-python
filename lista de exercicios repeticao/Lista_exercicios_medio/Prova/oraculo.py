eq=0
ins=0

for i in range(8):
    numero=int(input('digite o numero inteiro: '))
    
    if (numero % 2==0 and numero % 5 == 0) or (numero != 0 and numero % 3 ==0):
        print('numero quilibrado')
    else:
        ('numero desequilibrado')
        