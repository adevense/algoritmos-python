'''
Crie um menu interativo que permita adicionar, remover, listar ou sair de um programa que manipula listas.
'''

def exibir_menu():
    print("Menu:")
    print("1. Adicionar elemento")
    print("2. Remover elemento")
    print("3. Listar elementos")
    print("4. Sair")
def adicionar_elemento(lista):
    elemento = input("Digite o elemento a ser adicionado: ")
    lista.append(elemento)
    print(f"Elemento '{elemento}' adicionado com sucesso!")
def remover_elemento(lista):
    if lista:
        elemento = input("Digite o elemento a ser removido: ")
        if elemento in lista:
            lista.remove(elemento)
            print(f"Elemento '{elemento}' removido com sucesso!")
        else:
            print(f"Elemento '{elemento}' não encontrado na lista.")
    else:
        print("A lista está vazia. Não há elementos para remover.")
def listar_elementos(lista):
    if lista:
        print("Elementos na lista:")
        for elemento in lista:
            print(f"- {elemento}")
    else:
        print("A lista está vazia.")
def main():
    lista = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ")
        if opcao == '1':
            adicionar_elemento(lista)
        elif opcao == '2':
            remover_elemento(lista)
        elif opcao == '3':
            listar_elementos(lista)
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()
# Testando o programa
# main()
# Saindo do programa.