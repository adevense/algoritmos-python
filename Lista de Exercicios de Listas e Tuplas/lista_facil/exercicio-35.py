'''
 Crie uma lista de tuplas contendo nomes e idades. Imprima os nomes das pessoas
com mais de 18 anos.
'''
def filtra_maior_de_idade(lista):
    lista_maior_de_idade = []
    for i in lista:
        if i[1] >= 18:
            lista_maior_de_idade.append(i[0])
    return lista_maior_de_idade
# Testando a funcao
lista = [('João', 20), ('Maria', 17), ('José', 19), ('Ana', 16)]
print(f'Lista original: {lista}')
print(f'Lista com nomes de pessoas maiores de idade: {filtra_maior_de_idade(lista)}')