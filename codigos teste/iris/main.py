import funcoes


while True:
    comando = funcoes.reconhece_fala()
    if comando is not None:
        print(f"Comando recebido: {comando}")
        if 'encerrar' in comando or 'sair' in comando or 'desligar' in comando:
            break
        elif 'horas' in comando or 'hora' in comando or 'que horas são' in comando or 'que horas são agora' in comando:
            funcoes.ver_horas()
        elif 'data' in comando or 'dia' in comando or 'hoje' in comando  or 'hoje é' in comando : 
            funcoes.ver_data()
        elif 'procure por' in comando or 'pesquise por' in comando  or 'pesquisar por' in comando:
            funcoes.pesquisar_wikipedia(comando)
        elif 'tocar' in comando or 'toca' in comando or 'tocar música' in comando or 'toca música' in comando:
            funcoes.musica_youtube(comando)