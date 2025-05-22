'''
Crie uma lista de palavras e remova as que tiverem menos de 4 letras.
'''

def remove_palavras_curta(lista):
    """
    Remove palavras com menos de 4 letras de uma lista.
    
    Args:
        lista (list): Lista de palavras.
    
    Returns:
        list: Lista com palavras com 4 ou mais letras.
    """
    return [palavra for palavra in lista if len(palavra) >= 4]
# Testando a funcao
lista = ["cachorro", "gato", "elefante", "rato", "pato"]
print(f'Lista original: {lista}')
print(f'Lista sem palavras curtas: {remove_palavras_curta(lista)}')