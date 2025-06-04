import speech_recognition as sr

# Inicializa o reconhecedor
rec = sr.Recognizer()

# Use o microfone com o índice especificado (substitua 1 pelo índice correto)
try:
   
    with sr.Microphone(4) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Diga algo:")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)
        texto = texto.lower()
        
        if texto == "bom dia":
            print("Olá, bem vindo")
            
except sr.UnknownValueError:
    print("Não foi possível entender o que você disse.")
except sr.RequestError as e:
    print(f"Erro ao acessar o serviço de reconhecimento de voz: {e}")
except OSError as e:
    print(f"Erro ao acessar o microfone com índice 1: {e}")