"""
Contagem regressiva com atraso
Implemente uma funcao recursiva contagem regressiva(n) que imprime uma 
contagem de n ate 0. Ao chegar a 0, deve imprimir "Boom!".
(Opcional: usar time.sleep(1) para simular contagem real.)
"""
import time


def contagem_regresiva(tempo):
    if tempo<=0:
        print("Boom")
        return
    else:
        print ("contagem em:",tempo)
        time.sleep(1)
        contagem_regresiva(tempo -1)
    
    
while  True:
    tempo = input("informe a quantidade de repetições: ")
    tempo= int(tempo)
    if tempo <0:
        print("Valor invalido tente novamente!")
    else:
        contagem_regresiva(tempo)
        break