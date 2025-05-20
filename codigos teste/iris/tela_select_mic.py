import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import json
import os

class tela_selest_mic():
    # O construtor agora aceita 'parent_window' que será a janela principal (root)
    def __init__(self, parent_window):
        self.parent_window = parent_window # Armazena a referência da janela pai

        # Cria uma nova janela Toplevel, vinculada à janela pai
        self.toplevel_window = tk.Toplevel(self.parent_window) 
        self.toplevel_window.title("Escolher Microfone")
        self.toplevel_window.geometry("400x400")

        self.microfones_disponiveis = sr.Microphone.list_microphone_names()
        self.microfone_selecionado_index = tk.IntVar()
        self.microfone_selecionado_index.set(0) # Selecionar o primeiro por padrão

        # Todos os widgets agora são filhos de self.toplevel_window
        self.label = ttk.Label(self.toplevel_window, text="Selecione o microfone:")
        self.label.pack(pady=10)

        self.lista_microfones = ttk.Combobox(self.toplevel_window,
                                             values=self.microfones_disponiveis,
                                             textvariable=self.microfone_selecionado_index,
                                             state="readonly",
                                             width=35)
        self.lista_microfones.pack(padx=20, pady=10)
        self.lista_microfones.bind("<<ComboboxSelected>>", self.selecionar_microfone)
        
        self.btn_usar = ttk.Button(self.toplevel_window, text="Selecionar microfone", command=self.definir_microfone)
        self.btn_usar.pack(pady=20)

        self.microfone_index_escolhido = None
        if self.microfones_disponiveis:
            self.microfone_index_escolhido = 0
            self.lista_microfones.set(self.microfones_disponiveis[0])

        # Opcional: Torna a janela Toplevel modal
        # Isso significa que o usuário não pode interagir com a janela principal
        # enquanto esta janela de seleção de microfone estiver aberta.
        self.toplevel_window.transient(self.parent_window)
        self.toplevel_window.grab_set()
        # Espera até que a janela Toplevel seja fechada antes de continuar o código.
        self.parent_window.wait_window(self.toplevel_window)

    def selecionar_microfone(self, event):
        """Atualiza o índice do microfone selecionado."""
        self.microfone_index_escolhido = self.lista_microfones.current()
        print(f"Microfone selecionado (índice): {self.microfone_index_escolhido}")

    def definir_microfone(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_config = os.path.join(diretorio_atual, 'config.json')

        try:
            with open(caminho_config, 'r', encoding='utf-8') as arquivo_json:
                dados = json.load(arquivo_json)
        except FileNotFoundError:
            # Se o arquivo config.json não existir, cria uma estrutura básica
            dados = {"configuracao": {"microfone": None}}
        
        dados['configuracao']['microfone'] = self.microfone_index_escolhido
    
        with open(caminho_config, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
        
        # Fecha a janela Toplevel após salvar
        self.toplevel_window.destroy()