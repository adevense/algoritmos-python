'''
Lista/Tuplas/dicionario

Listas -> coleções heterogeneas de objetos, podem ser de qualquer tipo, inclusive outras listas
[0, 1, 10, "Beto",[2,5]]

listas são mutaveis

lista01=[1,2,3,4,5,6,7,8,9,10]

lista02=[3.14,'beto',True,[]]
'''

lista=[1,2,3,4,5,6,7,8,9,10]

print(lista)

nome = "Beto"

print(nome[0])

#len -> é uma função que retorna o tamanho de uma coleção
print(len(nome))

progs=['Yes','Genesis','Pink Floyd','ELP']

progs[3]='Metalica'
#progs[5]='Mew'

print(progs[0])
print(progs[1])

for i in range(len(progs)):
    print(progs[i])
    
for progs in progs:
    print(progs)    