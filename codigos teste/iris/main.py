from tkinter import *
from tela_inicial import tela_inicial_classe
from tela_select_mic import tela_selest_mic # Mantenha este import se for usar, mas a lógica de abertura deve ser tratada dentro de uma classe

if __name__ == "__main__":
    # Cria A ÚNICA janela principal da aplicação
    root = Tk()
    root.title("Iris")
    root.geometry("300x200") # largura x altura

    # Instancia a tela inicial_classe, passando a janela 'root' para ela.
    # A tela_inicial_classe será responsável por adicionar seus widgets a esta janela.
    app_inicial = tela_inicial_classe(root)

    # Nota sobre tela_selest_mic:
    # Se tela_selest_mic for uma janela secundária (como um pop-up de configuração),
    # ela deveria ser instanciada e exibida por um método dentro de tela_inicial_classe
    # (por exemplo, ao clicar em um botão "Configurar Microfone").
    # Não a instancie diretamente aqui, a menos que ela seja uma janela principal independente
    # e você esteja ciente das complexidades de múltiplos mainloops ou Toplevels.

    # Inicia o loop principal da interface gráfica.
    # APENAS UM mainloop() para a janela 'root' principal.
    root.mainloop()