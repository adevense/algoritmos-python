import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import pywhatkit
import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_config = os.path.join(diretorio_atual, 'config.json')

rec = sr.Recognizer() # É bom inicializar o Recognizer fora da função para não recriá-lo a cada chamada
engine = pyttsx3.init()


def reconhece_fala():
    comando = None   # Inicializa 'comando' com um valor padrão (None)
    try:
        with open(caminho_config, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            microfone_index_escolhido = dados['configuracao']['microfone']
        with sr.Microphone(device_index=microfone_index_escolhido) as mic: 
            print("ouvindo...")
            rec.adjust_for_ambient_noise(mic) # Ajusta o ruído ambiente para melhor reconhecimento
            audio = rec.listen(mic)
            comando = rec.recognize_google(audio, language="pt-BR")
            comando = comando.lower()
            print(f"Comando reconhecido: {comando}")
            if 'íris' in comando or 'iris' in comando:
                comando = comando.replace('iris', '').replace('íris', '').strip() # Remove ambas as variações e espaços
            else:
                comando = ''
               
    except:
        print("não ouvi nada")
        return None
    return comando


def ligar(comando):
    engine.say('Olá, eu sou a Iris. Como posso ajudar?')
    engine.runAndWait()
    while True:
        comando = reconhece_fala()
        if comando is not None:
            print(f"Comando recebido: {comando}")
            if 'encerrar' in comando or 'sair' in comando or 'desligar' in comando:
                break
            elif 'horas' in comando or 'hora' in comando or 'que horas são' in comando or 'que horas são agora' in comando:
                ver_horas()
            elif 'data' in comando or 'dia' in comando or 'hoje' in comando  or 'hoje é' in comando : 
                ver_data()
            elif 'procure por' in comando or 'pesquise por' in comando  or 'pesquisar por' in comando:
                pesquisar_wikipedia(comando)
            elif 'tocar' in comando or 'toca' in comando or 'tocar música' in comando or 'toca música' in comando or 'toque música' in comando or 'toque' in comando:
                musica_youtube(comando)       
       
       
def ver_horas():
    horas = datetime.datetime.now().strftime('%H:%M')
    engine.say(f'Agora são {horas}')
    engine.runAndWait()


def  ver_data():
    data = datetime.datetime.now().strftime('%d/%m/%Y')
    engine.say(f'Hoje é {data}')
    engine.runAndWait()

def pesquisar_wikipedia(comando):
    if 'procure por' in comando or 'pesquise por' in comando  or 'pesquisar por' in comando:
        comando = comando.replace('procure por', '').replace('pesquise por', '').replace('pesquisar por', '').strip()
        engine.say(f'Pesquisando por {comando} na Wikipedia')
        engine.runAndWait()
        wikipedia.set_lang('pt')
        # Limita a pesquisa a duas linhas
        resultado = wikipedia.summary(comando,2)
        engine.say(resultado)
        engine.runAndWait()
        
def musica_youtube(comando):
    if 'tocar' in comando or 'toca' in comando or 'tocar música' in comando or 'toca música' in comando  or 'toque música' in comando or 'toque' in comando:
        comando = comando.replace('tocar', '').replace('toca', '').replace('tocar música', '').replace('toca música', '').replace('toque música','').replace('toque','').strip()
        engine.say(f'Tocando {comando} no YouTube')
        engine.runAndWait()
        pywhatkit.playonyt(comando)