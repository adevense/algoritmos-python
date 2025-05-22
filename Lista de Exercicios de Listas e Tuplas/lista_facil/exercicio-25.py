'''
Solicite uma frase ao usu´ario e retorne uma lista com todas as palavras (use split).
'''

frase = input("Digite uma frase: ")
palavras = frase.split()
print(f'Lista de palavras: {palavras}')
# Testando a funcao
frase = "Aprendendo Python com OpenAI"
palavras = frase.split()
print(f'Lista de palavras: {palavras}')
