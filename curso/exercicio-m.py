def media_impares(numeros):
    
    impares = [num for num in numeros if num % 2 != 0]
   
    if impares:
        return sum(impares) / len(impares)
    else:
        return None  


numeros = []
print("Digite cinco números:")
for i in range(5):
    numero = float(input(f"Número {i+1}: "))
    numeros.append(numero)

resultado = media_impares(numeros)

if resultado is not None:
    print(f"A média dos números ímpares é: {resultado:.2f}")
else:
    print("Não há números ímpares entre os valores fornecidos.")
