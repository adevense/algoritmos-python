import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class HistoricoPontuacao:
    def __init__(self, nome_ponto, valor_ponto):
        self.nome_ponto = nome_ponto
        self.valor_ponto = valor_ponto

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao_total = 0.0
        self.historico = []

    def adicionar_ponto(self, nome_ponto, valor_ponto):
        self.pontuacao_total += valor_ponto
        novo_registro = HistoricoPontuacao(nome_ponto, valor_ponto)
        self.historico.append(novo_registro)

    def remover_ponto(self, indice):
        if 0 <= indice < len(self.historico):
            ponto_removido = self.historico.pop(indice)
            self.pontuacao_total -= ponto_removido.valor_ponto
            return True
        return False

    def modificar_ponto(self, indice, novo_valor):
        if 0 <= indice < len(self.historico):
            ponto = self.historico[indice]
            self.pontuacao_total -= ponto.valor_ponto
            ponto.valor_ponto = novo_valor
            self.pontuacao_total += novo_valor
            return True
        return False

class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Pontuação e Pódio")
        self.geometry("900x500")
        self.protocol("WM_DELETE_WINDOW", self.ao_fechar)

        self.pessoas = {}
        self.pessoa_selecionada = None
        self.caminho_arquivo = "dados_pontuacao.json"

        self.criar_widgets()
        self.carregar_dados()

    def criar_widgets(self):
        main_frame = tk.Frame(self, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        top_frame = tk.Frame(main_frame)
        top_frame.pack(fill=tk.X)

        save_button = tk.Button(top_frame, text="Salvar Dados", command=self.salvar_dados)
        save_button.pack(side=tk.RIGHT, padx=5)

        person_frame = tk.LabelFrame(top_frame, text="Gerenciar Pessoas", padx=5, pady=5)
        person_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=5)

        tk.Label(person_frame, text="Nome:").pack(side=tk.LEFT)
        self.nome_pessoa_entry = tk.Entry(person_frame)
        self.nome_pessoa_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        add_person_button = tk.Button(person_frame, text="Adicionar", command=self.adicionar_nova_pessoa)
        add_person_button.pack(side=tk.LEFT, padx=(0, 5))
        
        remove_person_button = tk.Button(person_frame, text="Remover", command=self.remover_pessoa)
        remove_person_button.pack(side=tk.LEFT)

        points_frame = tk.LabelFrame(main_frame, text="Gerenciar Pontos", padx=5, pady=5)
        points_frame.pack(fill=tk.X, pady=5)

        tk.Label(points_frame, text="Ponto:").pack(side=tk.LEFT)
        self.nome_ponto_entry = tk.Entry(points_frame)
        self.nome_ponto_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        tk.Label(points_frame, text="Valor:").pack(side=tk.LEFT, padx=(10, 0))
        self.valor_ponto_entry = tk.Entry(points_frame, width=8)
        self.valor_ponto_entry.pack(side=tk.LEFT)

        add_point_button = tk.Button(points_frame, text="Adicionar Ponto", command=self.adicionar_ponto_a_pessoa)
        add_point_button.pack(side=tk.LEFT, padx=5)

        display_frame = tk.Frame(main_frame)
        display_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        left_frame = tk.Frame(display_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        center_frame = tk.Frame(display_frame)
        center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        right_frame = tk.Frame(display_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(left_frame, text="Pessoas:").pack(anchor=tk.W)
        self.lista_pessoas = tk.Listbox(left_frame)
        self.lista_pessoas.pack(fill=tk.BOTH, expand=True)
        self.lista_pessoas.bind("<<ListboxSelect>>", self.selecionar_pessoa)

        historico_label = tk.Label(center_frame, text="Histórico de Pontuação:")
        historico_label.pack(anchor=tk.W)
        self.historico_listbox = tk.Listbox(center_frame)
        self.historico_listbox.pack(fill=tk.BOTH, expand=True)
        # Associa a seleção da listbox do histórico a um método
        self.historico_listbox.bind("<<ListboxSelect>>", self.ativar_botoes_edicao_ponto)

        historico_buttons_frame = tk.Frame(center_frame)
        historico_buttons_frame.pack(fill=tk.X, pady=5)

        self.btn_remover_ponto = tk.Button(historico_buttons_frame, text="Remover Ponto Selecionado", command=self.remover_ponto_selecionado, state=tk.DISABLED)
        self.btn_remover_ponto.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.btn_modificar_ponto = tk.Button(historico_buttons_frame, text="Modificar Ponto Selecionado", command=self.modificar_ponto_selecionado, state=tk.DISABLED)
        self.btn_modificar_ponto.pack(side=tk.LEFT, expand=True, fill=tk.X)

        tk.Label(right_frame, text="Pódio (Top 3):", font=("Arial", 12, "bold")).pack(anchor=tk.W)
        self.podio_text = tk.Text(right_frame, wrap=tk.WORD, state=tk.DISABLED, height=5)
        self.podio_text.pack(fill=tk.BOTH, expand=True)

    def salvar_dados(self):
        dados_para_salvar = {}
        for nome_pessoa, obj_pessoa in self.pessoas.items():
            historico_dict = [
                {"nome_ponto": ponto.nome_ponto, "valor_ponto": ponto.valor_ponto}
                for ponto in obj_pessoa.historico
            ]
            dados_para_salvar[nome_pessoa] = {
                "pontuacao_total": obj_pessoa.pontuacao_total,
                "historico": historico_dict
            }
        try:
            with open(self.caminho_arquivo, "w") as f:
                json.dump(dados_para_salvar, f, indent=4)
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        except IOError:
            messagebox.showerror("Erro", "Não foi possível salvar o arquivo.")

    def carregar_dados(self):
        if os.path.exists(self.caminho_arquivo):
            try:
                with open(self.caminho_arquivo, "r") as f:
                    dados_carregados = json.load(f)
                
                self.pessoas = {}
                for nome_pessoa, dados in dados_carregados.items():
                    nova_pessoa = Pessoa(nome_pessoa)
                    nova_pessoa.pontuacao_total = dados["pontuacao_total"]
                    nova_pessoa.historico = [
                        HistoricoPontuacao(ponto["nome_ponto"], ponto["valor_ponto"])
                        for ponto in dados["historico"]
                    ]
                    self.pessoas[nome_pessoa] = nova_pessoa
                
                self.atualizar_lista_pessoas()
                self.atualizar_podio()
                messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
            except (IOError, json.JSONDecodeError):
                messagebox.showerror("Erro", "Não foi possível carregar o arquivo de dados.")
    
    def ao_fechar(self):
        if messagebox.askyesno("Sair", "Deseja salvar os dados antes de sair?"):
            self.salvar_dados()
        self.destroy()

    def atualizar_lista_pessoas(self):
        self.lista_pessoas.delete(0, tk.END)
        for nome in sorted(self.pessoas.keys()):
            self.lista_pessoas.insert(tk.END, nome)
        self.atualizar_podio()

    def adicionar_nova_pessoa(self):
        nome = self.nome_pessoa_entry.get().strip()
        if nome and nome not in self.pessoas:
            nova_pessoa = Pessoa(nome)
            self.pessoas[nome] = nova_pessoa
            self.nome_pessoa_entry.delete(0, tk.END)
            self.atualizar_lista_pessoas()
            messagebox.showinfo("Sucesso", f"Pessoa '{nome}' adicionada.")
        elif nome in self.pessoas:
            messagebox.showwarning("Aviso", f"A pessoa '{nome}' já existe!")
    
    def remover_pessoa(self):
        try:
            indice = self.lista_pessoas.curselection()[0]
            nome_selecionado = self.lista_pessoas.get(indice)
            confirmar = messagebox.askyesno("Confirmar Remoção", f"Tem certeza que deseja remover {nome_selecionado}?")
            if confirmar:
                del self.pessoas[nome_selecionado]
                self.pessoa_selecionada = None
                self.atualizar_lista_pessoas()
                self.atualizar_historico_na_tela()
                messagebox.showinfo("Sucesso", f"Pessoa '{nome_selecionado}' removida.")
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma pessoa para remover.")

    def selecionar_pessoa(self, event=None):
        try:
            indice = self.lista_pessoas.curselection()[0]
            nome_selecionado = self.lista_pessoas.get(indice)
            self.pessoa_selecionada = self.pessoas.get(nome_selecionado)
            self.historico_listbox.selection_clear(0, tk.END) # Limpa a seleção do histórico
            self.atualizar_historico_na_tela()
        except IndexError:
            pass # Mantém a seleção anterior

    def adicionar_ponto_a_pessoa(self):
        if self.pessoa_selecionada:
            nome_ponto = self.nome_ponto_entry.get().strip()
            valor_ponto_str = self.valor_ponto_entry.get().strip()
            
            if not nome_ponto or not valor_ponto_str:
                messagebox.showerror("Erro", "Preencha o nome e o valor do ponto.")
                return

            try:
                valor_ponto = float(valor_ponto_str)
            except ValueError:
                messagebox.showerror("Erro", "O valor do ponto deve ser um número real.")
                return

            self.pessoa_selecionada.adicionar_ponto(nome_ponto, valor_ponto)
            self.atualizar_historico_na_tela()
            self.nome_ponto_entry.delete(0, tk.END)
            self.valor_ponto_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Selecione uma pessoa na lista.")

    def remover_ponto_selecionado(self):
        if self.pessoa_selecionada:
            try:
                indice = self.historico_listbox.curselection()[0]
                self.pessoa_selecionada.remover_ponto(indice)
                self.atualizar_historico_na_tela()
            except IndexError:
                messagebox.showwarning("Aviso", "Selecione um ponto para remover.")
        else:
            messagebox.showwarning("Aviso", "Selecione uma pessoa na lista.")

    def modificar_ponto_selecionado(self):
        if self.pessoa_selecionada:
            try:
                indice = self.historico_listbox.curselection()[0]
                ponto_selecionado = self.pessoa_selecionada.historico[indice]
                
                novo_valor_str = simpledialog.askstring("Modificar Ponto", f"Digite o novo valor para '{ponto_selecionado.nome_ponto}':", parent=self)
                
                if novo_valor_str is not None:
                    try:
                        novo_valor = float(novo_valor_str)
                        self.pessoa_selecionada.modificar_ponto(indice, novo_valor)
                        self.atualizar_historico_na_tela()
                    except ValueError:
                        messagebox.showerror("Erro", "O valor deve ser um número real.")
            except IndexError:
                messagebox.showwarning("Aviso", "Selecione um ponto para modificar.")
        else:
            messagebox.showwarning("Aviso", "Selecione uma pessoa na lista.")

    def atualizar_historico_na_tela(self):
        self.historico_listbox.delete(0, tk.END)
        if self.pessoa_selecionada:
            for registro in self.pessoa_selecionada.historico:
                self.historico_listbox.insert(tk.END, f"{registro.nome_ponto}: {registro.valor_ponto:.2f} pontos")
            self.historico_listbox.insert(tk.END, "--------------------------")
            self.historico_listbox.insert(tk.END, f"Pontuação Total: {self.pessoa_selecionada.pontuacao_total:.2f}")
        else:
            self.historico_listbox.insert(tk.END, "Nenhuma pessoa selecionada.")
        
        self.ativar_botoes_edicao_ponto()
        self.atualizar_podio()

    def ativar_botoes_edicao_ponto(self, event=None):
        if self.pessoa_selecionada:
            # Verifica se há algo selecionado na Listbox e se não é o separador ou a pontuação total
            try:
                indice_selecionado = self.historico_listbox.curselection()[0]
                if indice_selecionado < len(self.pessoa_selecionada.historico):
                    self.btn_remover_ponto.config(state=tk.NORMAL)
                    self.btn_modificar_ponto.config(state=tk.NORMAL)
                else:
                    self.btn_remover_ponto.config(state=tk.DISABLED)
                    self.btn_modificar_ponto.config(state=tk.DISABLED)
            except IndexError:
                self.btn_remover_ponto.config(state=tk.DISABLED)
                self.btn_modificar_ponto.config(state=tk.DISABLED)
        else:
            self.btn_remover_ponto.config(state=tk.DISABLED)
            self.btn_modificar_ponto.config(state=tk.DISABLED)

    def atualizar_podio(self):
        self.podio_text.config(state=tk.NORMAL)
        self.podio_text.delete(1.0, tk.END)

        if not self.pessoas:
            self.podio_text.insert(tk.END, "Nenhuma pessoa cadastrada.")
            self.podio_text.config(state=tk.DISABLED)
            return

        ranking = sorted(self.pessoas.values(), key=lambda p: p.pontuacao_total, reverse=True)
        
        self.podio_text.insert(tk.END, "Pódio:\n\n")
        
        if len(ranking) >= 1:
            self.podio_text.insert(tk.END, f"  1º - {ranking[0].nome}: {ranking[0].pontuacao_total:.2f} pontos\n\n")
        if len(ranking) >= 2:
            self.podio_text.insert(tk.END, f"  2º - {ranking[1].nome}: {ranking[1].pontuacao_total:.2f} pontos\n\n")
        if len(ranking) >= 3:
            self.podio_text.insert(tk.END, f"  3º - {ranking[2].nome}: {ranking[2].pontuacao_total:.2f} pontos\n\n")

        self.podio_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()