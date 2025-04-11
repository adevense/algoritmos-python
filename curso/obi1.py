hora = int(input())
minuto = int(input())
segundo = int(input())
acrescimo = int(input())
segundo = segundo + acrescimo 
segundo = segundo + 1 
while segundo > 59 and minuto < 59 and hora < 23:
    if segundo > 59:
        segundo = segundo - 60
        minuto + 1
    if minuto > 59:
        minuto = minuto - 60
        hora + 1
    if hora > 23:
        hora = segundo - 24
print(hora)
print(minuto)
print(segundo - 1)