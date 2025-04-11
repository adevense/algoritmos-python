lista_produtos = ["airpod","ipad","iphone","macbook"] #isso é uma lista
precos = [2000,9000, 6000, 11000] #isso tambem

#dic_produtos = {"chave":valor, "chave02":valor02}

dic_produtos = {"airpod":[2000,0], "ipad":9000, "iphone":6000, "macbook":11000} #isso é um dicionario
#pegar um elemento
print(dic_produtos["iphone"])

#editar um elemento
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.3
print(dic_produtos)

#quantidade de itens

print(len(dic_produtos))

#retirar um item do dicionario
dic_produtos.pop("airpod")
print(dic_produtos)

#adicionar um item no dicionario
dic_produtos["apple watch"] = 2500

#verificar se um item existe no dicionario
if "iphone" in dic_produtos:
    print("Existe")
else:
    print("Não existe")

#verificar se um item existe no valores do dicionario
if 9000 in dic_produtos.values():
    print("existe")
else:
    print("Não existe")



nome_produto = input("Nome do produto: ")
preco_produto = input("Preço do produto: ")
nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

produto = "airpod"
novo_preco = dic_produtos[produto] * 1.1
print(novo_preco)

dic_produtos[produto] = novo_preco
print(dic_produtos)

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco

print(dic_produtos)