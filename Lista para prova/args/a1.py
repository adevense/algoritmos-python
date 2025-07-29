def somar(*args):
    resultado =  sum(args)
    print(resultado)

valores = []
while True:
    valor = input("Informe os valores a somar:")
    valor = int(valor)
    valores.append(valor)
    continuar  = input("Continuar a adicionar valores(s/n):")
    if continuar == 'n':
        break



somar(*valores)
    