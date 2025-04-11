faturamento =  1200 #tipo: int -> numero inteiro
custo = 700.32 #tipo: float -> numero com casa decimal
lucro = faturamento - custo

print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

#  "@"
email_cliente = "adevense@gmail.com"

print(email_cliente.find("@")) # -1 quando não encontrar @ 

# tamanho do texto
print(len(email_cliente))

#pegar caractere

print(email_cliente[2])

print(email_cliente[-2])

#pegar um pedaço do texto

print(email_cliente[:4])

print(email_cliente[4:])

print(email_cliente[1:4])

#trocar um pedaço do texto

email_cliente = email_cliente.replace("gmail.com","hotmail.com")
print(email_cliente)

#pegar o servidor do email

posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)
servidor = email_cliente[posicao_arroba-1:]
print(servidor)