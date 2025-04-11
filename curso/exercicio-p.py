def verificar_triangulo(a, b, c):

    lados = sorted([a, b, c])

    menor, medio, maior = lados[0], lados[1], lados[2]


    if maior**2 == menor**2 + medio**2:
        return "Triângulo Retângulo"
    elif maior**2 < menor**2 + medio**2:
        return "Triângulo Acutângulo"
    else:
        return "Triângulo Obtusângulo"


lado1 = float(input("Digite a medida do lado 1: "))
lado2 = float(input("Digite a medida do lado 2: "))
lado3 = float(input("Digite a medida do lado 3: "))

resultado = verificar_triangulo(lado1, lado2, lado3)
print(f"O triângulo é: {resultado}")
