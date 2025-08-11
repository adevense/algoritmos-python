import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame
import os
import threading
import time
import json
from mutagen.mp3 import MP3
from ttkthemes import ThemedTk

class RPGMusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("RPG OST Player para Mestre")
        master.geometry("800x600")

        # Usando um tema base neutro e configurando as cores manualmente
        master.set_theme("clam")
        master.configure(bg="#f0f0f0")
        
        pygame.mixer.init()

        self.music_files = {
            "Batalha": [],
            "Ambiente": [],
            "Tensão": [],
            "Amigáveis": []
        }
        
        self.load_music_files()
        
        self.current_playlist = None
        self.current_index = 0
        self.paused = False
        self.loop_enabled = False
        self.playback_thread = None
        self.stop_thread = threading.Event()
        
        self.total_length = 0
        self.is_playing = False
        self.current_music_file = None
        
        self.drag_data = {"item": None, "original_index": None}
        self.is_seeking = False
        self.playback_start_pos = 0

        self.create_widgets()
        
        self.update_progress_bar_loop()
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        # Configurações de estilo para o tema branco básico
        style = ttk.Style()
        style.theme_use("clam")
        
        style.configure("TFrame", background="#f0f0f0")
        
        # Estilo do Notebook
        style.configure("TNotebook", background="#f0f0f0", borderwidth=0, tabposition="nw")
        style.configure("TNotebook.Tab", background="#e0e0e0", foreground="#000000", borderwidth=0, padding=[5, 2])
        style.map("TNotebook.Tab", background=[("selected", "#ffffff")], foreground=[("selected", "#000000")])
        
        style.configure("TLabel", background="#f0f0f0", foreground="#000000")
        
        # Estilo do botão
        style.configure("Light.TButton", font=("Arial", 10, "bold"), background="#e0e0e0", foreground="#000000", borderwidth=1, relief="raised")
        style.map("Light.TButton", background=[("active", "#d9d9d9"), ("pressed", "#cccccc")])

        # Estilo do Scale
        style.configure("TScale", background="#f0f0f0", troughcolor="#e0e0e0")
        style.configure("TScale", sliderrelief="flat")
        style.map("TScale", background=[("active", "#cccccc")])

        # Estilo da barra de rolagem
        style.configure("Vertical.TScrollbar", troughcolor="#e0e0e0", background="#cccccc", bordercolor="#d9d9d9", arrowcolor="#333333")
        style.map("Vertical.TScrollbar", background=[("active", "#bbbbbb")])
        
        # Frame principal para a lista de reprodução
        playlist_frame = ttk.Frame(self.master, padding="15", style="TFrame")
        playlist_frame.pack(fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(playlist_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        self.tabs = {}
        for category in self.music_files:
            frame = ttk.Frame(self.notebook, padding="10", style="TFrame")
            self.notebook.add(frame, text=category)
            self.tabs[category] = frame
            
            listbox_frame = ttk.Frame(frame, style="TFrame")
            listbox_frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, style="Vertical.TScrollbar")
            listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE, 
                                 bg="#ffffff", fg="#000000", selectbackground="#d9d9d9", selectforeground="#000000", 
                                 borderwidth=0, highlightthickness=0, font=("Arial", 10))
            listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.config(command=listbox.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            listbox.bind("<Double-Button-1>", lambda event, cat=category: self.play_selected_music(event, cat))
            listbox.bind("<ButtonPress-1>", lambda event, cat=category: self.on_drag_start(event, cat))
            listbox.bind("<B1-Motion>", lambda event, cat=category: self.on_drag_motion(event, cat))
            listbox.bind("<ButtonRelease-1>", lambda event, cat=category: self.on_drag_release(event, cat))
            
            self.tabs[category].listbox = listbox
            
            add_button = ttk.Button(frame, text=f"Adicionar músicas de {category}", command=lambda cat=category: self.add_music_files(cat), style="Light.TButton")
            add_button.pack(pady=(10, 0), fill=tk.X)
            
            for file_path in self.music_files[category]:
                listbox.insert(tk.END, os.path.basename(file_path))
        
        self.on_tab_change()
            
        controls_frame = ttk.Frame(self.master, padding="10", style="TFrame", relief="raised")
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.current_song_label = ttk.Label(controls_frame, text="Nenhuma música em reprodução", font=("Arial", 12, "bold"))
        self.current_song_label.pack(pady=(5, 5))
        
        button_frame = ttk.Frame(controls_frame, style="TFrame")
        button_frame.pack(pady=5)

        self.prev_button = ttk.Button(button_frame, text="⏪", command=self.prev_music, style="Light.TButton")
        self.play_button = ttk.Button(button_frame, text="▶️", command=self.play_music, style="Light.TButton")
        self.pause_button = ttk.Button(button_frame, text="⏸️", command=self.pause_music, style="Light.TButton")
        self.stop_button = ttk.Button(button_frame, text="⏹️", command=self.stop_music, style="Light.TButton")
        self.next_button = ttk.Button(button_frame, text="⏭️", command=self.next_music, style="Light.TButton")
        self.loop_button = ttk.Button(button_frame, text="🔁", command=self.toggle_loop, style="Light.TButton")
        
        self.prev_button.pack(side=tk.LEFT, padx=5)
        self.play_button.pack(side=tk.LEFT, padx=5)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.next_button.pack(side=tk.LEFT, padx=5)
        self.loop_button.pack(side=tk.LEFT, padx=20)
        
        progress_frame = ttk.Frame(controls_frame, style="TFrame")
        progress_frame.pack(pady=5, fill=tk.X)
        
        self.current_time_label = ttk.Label(progress_frame, text="00:00", foreground="#333333")
        self.current_time_label.pack(side=tk.LEFT, padx=5)

        self.progress_scale = ttk.Scale(progress_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.progress_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.progress_scale.bind("<ButtonPress-1>", self.on_seek_start)
        self.progress_scale.bind("<ButtonRelease-1>", self.on_seek_release)

        self.total_time_label = ttk.Label(progress_frame, text="00:00", foreground="#333333")
        self.total_time_label.pack(side=tk.LEFT, padx=5)

        volume_frame = ttk.Frame(controls_frame, style="TFrame")
        volume_frame.pack(pady=5, fill=tk.X)
        ttk.Label(volume_frame, text="Volume:", foreground="#000000").pack(side=tk.LEFT, padx=(5, 0))
        self.volume_scale = ttk.Scale(volume_frame, from_=0.0, to=1.0, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def on_tab_change(self, event=None):
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")
        self.current_playlist = self.music_files[tab_name]

    def add_music_files(self, category):
        files = filedialog.askopenfilenames(
            defaultextension=".mp3",
            filetypes=[("Arquivos de Áudio", "*.mp3 *.wav")]
        )
        if files:
            for file_path in files:
                file_name = os.path.basename(file_path)
                self.music_files[category].append(file_path)
                self.tabs[category].listbox.insert(tk.END, file_name)
            self.save_music_files()

    def play_selected_music(self, event, category):
        # Captura o índice da seleção atual
        selection = self.tabs[category].listbox.curselection()
        if selection:
            # Atualiza o índice e a playlist com base na seleção atual
            self.current_index = selection[0]
            self.current_playlist = self.music_files[category]
            self.play_music()
            
            # Limpa a seleção para que a próxima escolha seja independente
            self.tabs[category].listbox.selection_clear(0, tk.END)


    def play_music(self, start_pos=0):
        if not self.current_playlist or self.current_index >= len(self.current_playlist):
            self.current_song_label.config(text="Nenhuma música em reprodução")
            return

        self.current_music_file = self.current_playlist[self.current_index]

        try:
            audio = MP3(self.current_music_file)
            self.total_length = int(audio.info.length)
        except Exception:
            self.total_length = 0
        
        self.total_time_label.config(text=self.format_time(self.total_length))
        self.progress_scale.config(to=self.total_length)
        self.progress_scale.set(start_pos)
        self.current_song_label.config(text=os.path.basename(self.current_music_file))

        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.current_music_file)
        pygame.mixer.music.play(start=start_pos)
        self.paused = False
        
        self.playback_start_pos = start_pos
        self.set_volume(self.volume_scale.get())

        self.is_playing = True
        
        if self.playback_thread and self.playback_thread.is_alive():
            self.stop_thread.set()
            self.playback_thread.join()
        
        self.stop_thread.clear()
        self.playback_thread = threading.Thread(target=self.check_playback_status)
        self.playback_thread.daemon = True
        self.playback_thread.start()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused = True
            self.is_playing = False
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.is_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused = False
        self.is_playing = False
        self.progress_scale.set(0)
        self.current_time_label.config(text="00:00")
        self.current_song_label.config(text="Nenhuma música em reprodução")
        
    def next_music(self):
        if self.current_playlist:
            self.current_index = (self.current_index + 1) % len(self.current_playlist)
            self.play_music()

    def prev_music(self):
        if self.current_playlist:
            self.current_index = (self.current_index - 1 + len(self.current_playlist)) % len(self.current_playlist)
            self.play_music()

    def toggle_loop(self):
        self.loop_enabled = not self.loop_enabled
        self.loop_button.configure(style="Loop.TButton" if self.loop_enabled else "Light.TButton")
        style = ttk.Style()
        style.configure("Loop.TButton", background="#0078d7", foreground="#ffffff")
        style.map("Loop.TButton", background=[("active", "#0088e7")])

    def on_seek_start(self, event):
        self.is_seeking = True

    def on_seek_release(self, event):
        if self.current_music_file:
            new_pos = float(self.progress_scale.get())
            self.play_music(start_pos=new_pos)
        self.is_seeking = False

    def set_volume(self, value):
        pygame.mixer.music.set_volume(float(value))

    def on_drag_start(self, event, category):
        listbox = self.tabs[category].listbox
        selection = listbox.curselection()
        if not selection:
            return

        index = selection[0]
        self.drag_data["item"] = listbox.get(index)
        self.drag_data["original_index"] = index
        self.drag_data["category"] = category

    def on_drag_motion(self, event, category):
        if not self.drag_data["item"] or self.drag_data["category"] != category:
            return

        listbox = self.tabs[category].listbox
        y = event.y
        new_index = listbox.nearest(y)

        if new_index != self.drag_data["original_index"]:
            listbox.delete(self.drag_data["original_index"])
            listbox.insert(new_index, self.drag_data["item"])
            listbox.selection_set(new_index)
            self.drag_data["original_index"] = new_index

    def on_drag_release(self, event, category):
        if not self.drag_data["item"] or self.drag_data["category"] != category:
            return

        listbox = self.tabs[category].listbox
        try:
            new_index = listbox.nearest(event.y)
            file_path_to_move = self.music_files[category].pop(self.drag_data["original_index"])
            self.music_files[category].insert(new_index, file_path_to_move)

            if self.current_playlist == self.music_files[category]:
                if self.current_index == self.drag_data["original_index"]:
                    self.current_index = new_index
                elif self.current_index > self.drag_data["original_index"] and self.current_index <= new_index:
                    self.current_index -= 1
                elif self.current_index < self.drag_data["original_index"] and self.current_index >= new_index:
                    self.current_index += 1
            
        except IndexError:
            pass

        self.drag_data = {"item": None, "original_index": None}
        self.save_music_files()

    def update_progress_bar_loop(self):
        if self.is_playing and not self.paused and not self.is_seeking:
            time_since_play = pygame.mixer.music.get_pos() / 1000
            current_time = time_since_play + self.playback_start_pos
            
            if current_time <= self.total_length:
                self.progress_scale.set(current_time)
                self.current_time_label.config(text=self.format_time(current_time))
            
        self.master.after(100, self.update_progress_bar_loop)

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"

    def check_playback_status(self):
        while not self.stop_thread.is_set():
            if not pygame.mixer.music.get_busy() and self.is_playing:
                if self.loop_enabled:
                    self.play_music()
                else:
                    self.is_playing = False
                    self.next_music()
            time.sleep(0.5)

    def save_music_files(self):
        try:
            with open("music_files.json", "w", encoding="utf-8") as f:
                json.dump(self.music_files, f)
        except Exception as e:
            print(f"Erro ao salvar os arquivos: {e}")

    def load_music_files(self):
        try:
            with open("music_files.json", "r", encoding="utf-8") as f:
                self.music_files = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhum arquivo salvo encontrado ou o arquivo está corrompido.")

    def on_closing(self):
        self.save_music_files()
        self.stop_thread.set()
        pygame.mixer.music.stop()
        self.master.destroy()

if __name__ == "__main__":
    root = ThemedTk(theme="clam")
    app = RPGMusicPlayer(root)
    root.mainloop()