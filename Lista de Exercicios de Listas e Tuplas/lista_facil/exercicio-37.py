'''
Crie uma lista de palavras e remova as que tiverem menos de 4 letras.
'''

def remove_palavras_curta(lista):

    return [palavra for palavra in lista if len(palavra) >= 4]
# Testando a funcao
lista = ["cachorro", "gato", "elefante", "rato", "pato"]
print(f'Lista original: {lista}')
print(f'Lista sem palavras curtas: {remove_palavras_curta(lista)}')