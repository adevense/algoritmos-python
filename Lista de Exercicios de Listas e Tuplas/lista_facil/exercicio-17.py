'''
Crie uma lista com 5 numeros e calcule a media usando laco for.
'''
lista = [10, 20, 30, 40, 50]
soma = 0

for numero in lista:
    soma += numero

if len(lista) > 0:
    media = soma / len(lista)
    print(f"A lista de números é: {lista}")
    print(f"A soma dos números é: {soma}")
    print(f"A média dos números é: {media}")
else:
    print("A lista está vazia, não é possível calcular a média.")
    
#não entendi o porque de calcular a media por meio de um for sendo que se pode calcular apenas com um /len