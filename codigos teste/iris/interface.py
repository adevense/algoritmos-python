import tkinter as tk
from tkinter import ttk
import speech_recognition as sr

class EscolhaMicrofoneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escolher Microfone")

        self.microfones_disponiveis = sr.Microphone.list_microphone_names()
        self.microfone_selecionado_index = tk.IntVar()
        self.microfone_selecionado_index.set(0)  # Selecionar o primeiro por padrão

        self.label = ttk.Label(root, text="Selecione o microfone:")
        self.label.pack(pady=10)

        self.lista_microfones = ttk.Combobox(root,
                                            values=self.microfones_disponiveis,
                                            textvariable=self.microfone_selecionado_index,
                                            state="readonly")
        self.lista_microfones.pack(padx=20, pady=10)
        self.lista_microfones.bind("<<ComboboxSelected>>", self.selecionar_microfone)

        self.btn_usar = ttk.Button(root, text="Usar Microfone Selecionado", command=self.usar_microfone)
        self.btn_usar.pack(pady=20)

        self.microfone_index_escolhido = None

    def selecionar_microfone(self, event):
        """Atualiza o índice do microfone selecionado."""
        self.microfone_index_escolhido = self.lista_microfones.current()
        print(f"Microfone selecionado (índice): {self.microfone_index_escolhido}")

    def usar_microfone(self):
        """Usa o microfone selecionado para reconhecimento de fala."""
        if self.microfone_index_escolhido is not None:
            try:
                with sr.Microphone(device_index=self.microfone_index_escolhido) as mic:
                    rec = sr.Recognizer()
                    print(f"Ouvindo no microfone: {self.microfones_disponiveis[self.microfone_index_escolhido]}")
                    rec.adjust_for_ambient_noise(mic)
                    audio = rec.listen(mic)
                    texto = rec.recognize_google(audio, language="pt-BR")
                    print(f"Você disse: {texto}")
                self.root.destroy()  # Fecha a janela após o uso (opcional)
            except sr.WaitTimeoutError:
                print("Nenhum áudio detectado.")
            except sr.UnknownValueError:
                print("Não foi possível entender o áudio.")
            except sr.RequestError as e:
                print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")
        else:
            print("Por favor, selecione um microfone.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EscolhaMicrofoneApp(root)
    root.mainloop()