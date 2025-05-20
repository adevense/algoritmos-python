
'''
#Open 
arquivo = open('nomes.txt','a', encoding='utf-8')  #metodo ''w' para escrita sobrescreve o arquivo o metodo 'a' adiciona
# Write
arquivo.write('Inacio\n') #\n purga quebra de linha  atl esq + 9 + 2 do numpad para gerar a barra a esquerda

arquivo.close() #fecha o arquivo

with open('nomes.txt','r', encoding='utf-8') as arquivo: #comando with fecha o arquivo automaticamente  metodo 'r' para leitura 
    # e metodo 'r+' para leitura e escrita, w+ para escrita e leitura  que cria o arquivo se ele nao existir
    
   # nomes = arquivo.read() #leitura do arquivo
    #print(nomes) #imprime o conteudo do arquivo
    nomes1 = arquivo.readlines(1) #leitura do arquivo linha a linha
    print(nomes1) #imprime o conteudo do arquivo
'''

#Exemplo 1: Lendo o arquivo inteiro de uma vez (.read()):
'''
# Criando um arquivo de exemplo para leitura
with open("exemplo_leitura.txt", "w") as f:
    f.write("Esta é a primeira linha.\n")
    f.write("Esta é a segunda linha.\n")
    f.write("E a última linha.\n")

# Lendo o arquivo
try:
    with open("exemplo_leitura.txt", "r") as arquivo:
        conteudo = arquivo.read()  # Lê todo o conteúdo como uma única string
        print("Conteúdo completo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo 'exemplo_leitura.txt' não foi encontrado.")
'''
 
'''
#Exemplo 2: Lendo o arquivo linha por linha (.readline() ou iterando):

# Criando um arquivo de exemplo
with open("linhas.txt", "w") as f:
    f.write("Item A\n")
    f.write("Item B\n")
    f.write("Item C\n")

# Lendo linha por linha
print("\nLendo linha por linha:")
with open("linhas.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip()) # .strip() remove espaços em branco (incluindo quebras de linha)

# Usando .readline() (menos comum para iterar o arquivo inteiro)
print("\nLendo com .readline():")
with open("linhas.txt", "r") as arquivo:
    primeira_linha = arquivo.readline()
    print(primeira_linha.strip())
    segunda_linha = arquivo.readline()
    print(segunda_linha.strip())
'''

print("\nEscrevendo em 'saida.txt' (sobrescrevendo):")
with open("saida.txt", "w", encoding='utf-8') as arquivo_saida:
    arquivo_saida.write("Este texto sobrescreverá qualquer conteúdo anterior.\n")
    arquivo_saida.write("Esta é a segunda linha escrita.\n")
    arquivo_saida.write("Número: " + str(123) + "\n") # Converter números para string
    