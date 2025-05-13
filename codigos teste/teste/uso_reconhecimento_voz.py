import speech_recognition  as sr

#print(sr.Microphone.list_microphone_names())

rec = sr.Recognizer()
with sr.Microphone(4) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Diga algo:")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print("Você disse:", texto)
    texto = texto.lower()
    if texto == "bom dia":
        print("Olá, bem vindo")