saldo = int(input("Digite o valor do saldo:"))

if  saldo >=  0 and saldo <201:
    print("Nenhum crédito")
elif saldo>200 and saldo<=400:
    print("20% do valor do saldo médio.")
elif saldo>400 and saldo<=600:
    print("30% do valor do saldo médio.")   
elif saldo>601:
    print("40% do valor do saldo médio.")   
else:
    print("Saldo negativo ou invalido.")


print("Acabou o prgrama")