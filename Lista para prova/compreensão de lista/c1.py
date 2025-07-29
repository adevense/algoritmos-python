def filtrar_palavras_longas(lista_palavras):
    return [palavra for palavra in lista_palavras if len(palavra) > 5]

# Exemplo de uso:
palavras = ["banana", "uva", "morango", "kiwi", "abacaxi", "manga"]
palavras_filtradas = filtrar_palavras_longas(palavras)
print(f"Palavras originais: {palavras}")
print(f"Palavras com mais de 5 letras: {palavras_filtradas}") # Saída: ['banana', 'morango', 'abacaxi']