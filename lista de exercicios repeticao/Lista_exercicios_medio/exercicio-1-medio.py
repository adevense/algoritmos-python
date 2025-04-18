"""
Exercício 1: Contagem de Vogais em uma Frase
Crie um programa usando laços que receba uma frase do usuário e retorne quantas vogais
há nessa frase.
"""

def contar_vogais(frase):
  """
  Conta o número de vogais (a, e, i, o, u) em uma frase.

  Args:
    frase: A frase fornecida pelo usuário (string).

  Returns:
    O número total de vogais na frase (inteiro).
  """
  vogais = "aeiouAEIOU"
  contador_vogais = 0
  for letra in frase:
    if letra in vogais:
      contador_vogais += 1
  return contador_vogais

# Solicita a frase ao usuário
frase_usuario = input("Digite uma frase: ")

# Chama a função para contar as vogais
numero_de_vogais = contar_vogais(frase_usuario)

# Exibe o resultado
print(f"A frase '{frase_usuario}' possui {numero_de_vogais} vogais.")

"""
Explicação:

def contar_vogais(frase):: Define uma função chamada contar_vogais que recebe uma frase como argumento.
vogais = "aeiouAEIOU": Cria uma string contendo todas as vogais, tanto minúsculas quanto maiúsculas. Isso facilita a verificação.
contador_vogais = 0: Inicializa uma variável contador_vogais com o valor 0. Esta variável será usada para armazenar o número de vogais encontradas na frase.
for letra in frase:: Este laço for itera sobre cada caractere (letra) na frase fornecida pelo usuário.
if letra in vogais:: Dentro do laço, esta condição verifica se a letra atual está presente na string vogais. O operador in verifica se um elemento pertence a uma sequência.
contador_vogais += 1: Se a letra for uma vogal (ou seja, a condição do if for verdadeira), o contador_vogais é incrementado em 1.
return contador_vogais: Após o laço terminar de percorrer todos os caracteres da frase, a função retorna o valor final de contador_vogais, que representa o número total de vogais encontradas.
frase_usuario = input("Digite uma frase: "): Solicita ao usuário que digite uma frase e armazena essa entrada na variável frase_usuario.
numero_de_vogais = contar_vogais(frase_usuario): Chama a função contar_vogais com a frase fornecida pelo usuário e armazena o resultado (o número de vogais) na variável numero_de_vogais.
print(f"A frase '{frase_usuario}' possui {numero_de_vogais} vogais."): Exibe uma mensagem informando a frase digitada pelo usuário e o número de vogais encontradas.
"""