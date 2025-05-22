'''
Simule uma pilha usando append e pop. Mostre a pilha a cada opera¸c˜ao.
'''

pilha = []
while True:
    operacao = input("Digite 'adicionar' para adicionar um elemento, 'remover' para remover o elemento do topo ou 'sair' para encerrar: ").strip().lower()
    
    if operacao == 'adicionar':
        elemento = input("Digite o elemento a ser adicionado: ")
        pilha.append(elemento)
        print(f"Pilha após adicionar '{elemento}': {pilha}")
    elif operacao == 'remover':
        if pilha:
            removido = pilha.pop()
            print(f"Elemento removido: '{removido}'")
            print(f"Pilha após remover: {pilha}")
        else:
            print("A pilha está vazia. Não há elementos para remover.")
    elif operacao == 'sair':
        break
    else:
        print("Operação inválida. Tente novamente.")