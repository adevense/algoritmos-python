from tkinter import *
from tela_inicial import tela_inicial_classe

if __name__ == "__main__":
    # Cria A ÚNICA janela principal da aplicação
    root = Tk()
    root.title("Iris")
    root.geometry("300x200") # largura x altura

    # Instancia a tela inicial_classe, passando a janela 'root' para ela.
    # A tela_inicial_classe será responsável por adicionar seus widgets a esta janela.
    app_inicial = tela_inicial_classe(root)

    
    # Inicia o loop principal da interface gráfica.
    # APENAS UM mainloop() para a janela 'root' principal.
    root.mainloop()