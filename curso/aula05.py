lista_vendas =[1000, 500, 800, 2000, 2300]
meta = 1200
percentual_bonus = 0.1

for venda in lista_vendas:
    if venda >= meta:
        bonus = percentual_bonus * venda
    else:
        bonus = 0
    print(bonus)

#   indice  
#for item in lista_vendas:
#    print(item)
#    print("proximo item")

#fora do for