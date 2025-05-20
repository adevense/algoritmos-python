from tkinter import *
from funcoes import *

janela = Tk()
 
janela.title("Iris") #titulo da janela
janela.geometry("300x200") #largura x altura


texto_orientacao  = Label(janela, text="Clique no botão para iniciar a Iris") #texto na janela
texto_orientacao.pack() #coloca o texto na janela
botao = Button(janela, text="Iniciar Iris", command=lambda: ligar()) #botão que inicia a Iris
botao.pack() #coloca o botão na janela



janela.mainloop()