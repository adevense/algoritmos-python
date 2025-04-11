
vendas = float(input("Digite o valor das vendas:"))
meta = 1300

# == igual
# != diferente


    # if condição / comparação:
#tudo o que acontece se a condição for verdadeira
#else:
#tudo o que acontece se a condição for falsa

meta1 = 1500

if vendas >= meta1:
    print("Vendedor ganha bônus")
    bonus = 0.2 * vendas
    print("Bonus do vendedor: ", bonus)
elif vendas>= meta:
    print("Vendedor ganha bônus")
    bonus = 0.1 * vendas
    print("Bonus do vendedor: ", bonus)
else:
    print("Vendedor não bateu a meta de vendas")

print("Acabou o prgrama")