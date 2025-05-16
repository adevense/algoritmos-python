'''
. Dada uma lista de palavras, junte todas elas em uma string separada por virgulas.
'''

lista = ["maçã", "banana", "laranja", "abacaxi"]
string = ", ".join(lista)
print(string)

'''
O método join() em Python é uma função poderosa e flexível usada para concatenar (juntar) os elementos de um iterável (como uma lista, tupla, conjunto ou qualquer outro objeto que 
possa ser percorrido) em uma única string. A grande sacada do join() é que você especifica qual string será usada como separador entre esses elementos.

Pense nele da seguinte forma: você tem vários itens separados e quer colá-los juntos com algo no meio para separá-los. O join() faz exatamente isso.

A Sintaxe Básica:

separador.join(iteravel)

Onde:
separador: É a string que você deseja inserir entre cada elemento do iterável. Pode ser uma vírgula, um espaço, um traço, uma string vazia (para juntar sem nenhum separador), ou 
qualquer outra string que você quiser.
iteravel: É o objeto iterável (lista, tupla, conjunto, etc.) cujos elementos você quer juntar. É importante notar que todos os elementos dentro deste iterável devem ser strings. 
Se houver outros tipos de dados (como números), você precisará convertê-los para strings antes de usar o join().
'''