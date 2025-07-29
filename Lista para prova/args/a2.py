'''
Multiplicacao com *args e verificacao de tipo
Crie uma funcao que multiplica todos os argumentos numericos, ignorando qualquer
argumento que nao seja int ou float.

'''
import math

def multiplicar(*args):
    numeros_validos = []
    for arg in args:
        if isinstance(arg, (int, float)):
            numeros_validos.append(arg)

    if not numeros_validos:
        return 1
    
    produto = math.prod(numeros_validos)
    return produto

valores_para_multiplicar = []

while True:
    valor_str = input("Informe o valor a multiplicar (ou digite 'n' para parar): ")

    if valor_str.lower() == 'n':
        break
    
    try:
        valor = int(valor_str)
        valores_para_multiplicar.append(valor)
    except ValueError:
        try:
            valor = float(valor_str)
            valores_para_multiplicar.append(valor)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número (inteiro ou decimal) ou 'n'.")

resultado_final = multiplicar(*valores_para_multiplicar)

print(f"O produto final de todos os números válidos é: {resultado_final}")
