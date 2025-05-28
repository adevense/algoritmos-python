from tkinter import *
from tkinter import ttk # Importe ttk para usar widgets com estilo, se necessário
from funcoes import * # Certifique-se de que funcoes.py contém a função 'ligar'
from tela_select_mic import tela_selest_mic # Importa a classe da tela de seleção de microfone

class tela_inicial_classe():
    def __init__(self, master):
        self.master = master # Armazena a referência da janela principal

        # Widgets da tela inicial
        self.texto_orientacao = Label(self.master, text="Clique no botão para iniciar a Iris")
        self.texto_orientacao.pack(pady=10)

        self.botao_iniciar = Button(self.master, text="Iniciar Iris", command=lambda: ligar())
        self.botao_iniciar.pack(pady=10)

        # Botão para abrir a tela de seleção de microfone
        self.botao_config_mic = Button(self.master, text="Configurar Microfone", command=self.abrir_tela_mic)
        self.botao_config_mic.pack(pady=5) # Padding menor para diferenciar

    def abrir_tela_mic(self):
        """
        Método para abrir a tela de seleção de microfone como um popup.
        """
        # Instancia a tela_selest_mic, passando a janela principal (self.master) como seu pai.
        # A tela_selest_mic (conforme a correção anterior) se encarregará de criar o Toplevel.
        tela_mic_popup = tela_selest_mic(self.master)
        
        # Nota: Como a tela_selest_mic já tem .grab_set() e .wait_window() em seu __init__,
        # o fluxo do programa aqui vai pausar até que a tela_mic_popup seja fechada.