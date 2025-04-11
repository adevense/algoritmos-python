x = 9

raiz_x = x ** 2
print(raiz_x)

#ler o valor de 2 lados de um triangulo etangulo e calcular a hipotenusa

lado_01 = float(input('digite o lado 1: '))
lado_02 = float(input('digite o lado 2: '))

print('A hipotenusa é: ', (lado_01**2)+(lado_02**2)/0.5)

# calcular a raiz cubica de x exp. abaixo.
# x = (raiz(y)) + a/3)/raiz(b/2a)
a = float(input('digite a: '))
b = float(input('digite b: '))
y = float(input('digite y: '))
x = ((y**0.5) + a/3) / ((b / (2 * a)**0.5)) 
print('A raiz é:', x )