'''
Fa¸ca um programa que leia n´umeros do usu´ario at´e digitar -1. Depois, imprima a
m´edia.
'''

def calcula_media():
    lista = []
    while True:
        numero = int(input("Digite um número (-1 para sair): "))
        if numero == -1:
            break
        lista.append(numero)
    if len(lista) == 0:
        print("Nenhum número foi digitado.")
    else:
        media = sum(lista) / len(lista)
        print(f"Média: {media}")
# Testando a função
calcula_media()
# Saindo do programa.