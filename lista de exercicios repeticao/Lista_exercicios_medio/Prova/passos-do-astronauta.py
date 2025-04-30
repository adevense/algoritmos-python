passos = int(input("Quantos passos o astronauta deu: "))
pedras= 0
buraco = 0
 
for i in range(1, passos +1):
    
    obs = input(f'Passo {i}: Pedra (P) ou Buraco(B): ').upper()
    
    if obs == 'P':
        pedras+=1
    elif obs == 'B':
        buraco+=1
    else:
        print('entrada invalida')

print(f'Total de pedras encontradas: {pedras}')
print(f'Total de buracos encontradas: {buraco}')

if buraco>pedras:
    print('Cuidado! Mais buracos que pedras')
