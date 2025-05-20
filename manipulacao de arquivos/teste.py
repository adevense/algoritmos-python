import os

def reescrever_linha(nome_arquivo, chave_para_modificar, novo_valor):
    """
    Lê o arquivo, modifica a linha com a chave especificada e reescreve o arquivo.

    Args:
        nome_arquivo (str): O nome do arquivo a ser modificado.
        chave_para_modificar (str): A chave (ex: 'DEBUG') da linha a ser alterada.
        novo_valor (str): O novo valor a ser atribuído à chave.
    """
    linhas = []
    modificado = False

    # 1. Ler o conteúdo existente do arquivo
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                # Verificar se a linha contém a chave que queremos modificar
                if linha.strip().startswith(chave_para_modificar + '='):
                    linhas.append(f"{chave_para_modificar}={novo_valor}\n")
                    modificado = True
                else:
                    linhas.append(linha) # Mantém as outras linhas como estão
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    if not modificado:
        print(f"A chave '{chave_para_modificar}' não foi encontrada no arquivo. Adicionando-a.")
        linhas.append(f"{chave_para_modificar}={novo_valor}\n")


    # 2. Escrever todo o conteúdo modificado de volta no arquivo
    # Abrir o arquivo no modo 'w' (escrita) apaga o conteúdo antigo
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.writelines(linhas) # Escreve todas as linhas de uma vez

    print(f"Arquivo '{nome_arquivo}' modificado com sucesso para {chave_para_modificar}={novo_valor}")


# --- Exemplo de Uso ---

# Crie um arquivo de exemplo para testar
nome_do_arquivo = "config.txt"
with open(nome_do_arquivo, "w", encoding='utf-8') as f:
    f.write("VERSAO=1.0\n")
    f.write("DEBUG=False\n")
    f.write("PORTA=8080\n")
    f.write("NOME_APP=MinhaAplicacao\n")

print("Conteúdo original de config.txt:")
with open(nome_do_arquivo, 'r', encoding='utf-8') as f:
    print(f.read())

# Modificar a linha 'DEBUG'
reescrever_linha(nome_do_arquivo, "DEBUG", "True")

print("\nConteúdo de config.txt após a modificação de DEBUG:")
with open(nome_do_arquivo, 'r', encoding='utf-8') as f:
    print(f.read())

# Modificar uma linha que não existe (será adicionada)
reescrever_linha(nome_do_arquivo, "TIMEOUT", "600")

print("\nConteúdo de config.txt após adicionar TIMEOUT:")
with open(nome_do_arquivo, 'r', encoding='utf-8') as f:
    print(f.read())