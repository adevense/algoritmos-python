contador_quantidade = float(input("digite a quantidades de números a serem inseridos: "))
lista_numeros = []
contador = 1
while contador <= contador_quantidade:
    num = float(input("insira o valor dos números: "))
    posicao_0 = len(lista_numeros)
    print(posicao_0)
    if num == 0:
        lista_numeros.pop(posicao_0 - 1)
    else:
        lista_numeros.append(num)
    contador = contador + 1
print(sum(lista_numeros))