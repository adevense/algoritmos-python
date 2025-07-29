import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo(titulo):
    print("\n" + "=" * 60)
    print(f"{titulo.center(60)}")
    print("=" * 60 + "\n")

def exibir_menu(opcoes, colunas=1):
    if colunas == 1:
        for i, opcao in enumerate(opcoes):
            print(f"[{i + 1}] {opcao}")
    else:
        # Divide as opções em duas colunas
        metade = (len(opcoes) + 1) // 2
        coluna1 = opcoes[:metade]
        coluna2 = opcoes[metade:]

        # Adiciona um espaçamento mínimo para a primeira coluna
        max_len1 = 0
        if coluna1:
            max_len1 = max(len(f"[{i+1}] {opcao}") for i, opcao in enumerate(coluna1))
        
        for i in range(metade):
            item1 = f"[{i + 1}] {coluna1[i]}"
            item1_padded = item1.ljust(max_len1 + 5) # Adiciona um espaçamento entre colunas
            
            if i < len(coluna2):
                item2 = f"[{i + metade + 1}] {coluna2[i]}"
                print(f"{item1_padded}{item2}")
            else:
                print(item1_padded)
    print("-" * 60)

def obter_escolha(prompt, max_opcao):
    while True:
        try:
            escolha = int(input(prompt))
            if 1 <= escolha <= max_opcao:
                return escolha
            else:
                print("Opção inválida. Por favor, escolha um número dentro do intervalo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def gerar_ficha_ordem_paranormal_v6():
    """
    Gera uma ficha de personagem aleatória para Ordem Paranormal com interface interativa e regras oficiais.
    """

    # --- Dados Oficiais e Expandidos ---
    # Nomes e Sobrenomes (Mantidos como V5 para variedade, pois o prompt não pediu alteração aqui)
    nomes_masculinos = {
        "brasileiro": ["Arthur", "Carlos", "Eduardo", "Gabriel", "Igor", "Lucas", "Nicolas", "Pedro", "Rafael", "Thiago", "Victor", "João", "Marcelo", "Miguel", "Bruno", "Daniel", "Felipe", "Gustavo", "Leonardo", "Rodrigo"],
        "japones": ["Kenji", "Hiroshi", "Akira", "Ren", "Sora", "Takashi", "Yuki", "Daiki", "Haruto", "Kaito", "Kazuki", "Ryo", "Satoshi", "Shota", "Yuuto"],
        "americano": ["Alex", "Brian", "Chris", "Daniel", "Ethan", "Frank", "George", "Henry", "Isaac", "Jacob", "Kevin", "Liam", "Mason", "Noah", "Oliver"],
        "alemao": ["Franz", "Hans", "Karl", "Max", "Oskar", "Paul", "Rolf", "Walter", "Wolfgang", "Ludwig", "Andreas", "Felix", "Jonas", "Leon", "Moritz"],
        "russo": ["Ivan", "Dmitri", "Nikolai", "Sergei", "Vladimir", "Alexei", "Boris", "Grigori", "Leonid", "Pavel", "Andrei", "Fyodor", "Mikhail", "Roman", "Yuri"],
        "europeu_ocidental": ["Louis", "Jean", "Pierre", "Antoine", "Marc", "Hugo", "Oscar", "Felix", "Leo", "Gaspard", "Alessandro", "Giovanni", "Marco", "Giuseppe", "Francesco", "Pablo", "Javier", "Diego", "Miguel", "Antonio"],
        "europeu_oriental": ["Jan", "Piotr", "Tomasz", "Filip", "Adam", "Matej", "Milan", "Jakub", "Luka", "Denis"]
    }

    nomes_femininos = {
        "brasileiro": ["Beatriz", "Diana", "Fernanda", "Helena", "Juliana", "Mariana", "Olivia", "Sophia", "Ursula", "Yasmin", "Alice", "Bruna", "Isabela", "Laura", "Natália", "Ana", "Gabriela", "Larissa", "Manuela", "Vitória"],
        "japones": ["Akari", "Hana", "Koharu", "Mio", "Rina", "Sakura", "Yui", "Aoi", "Ichika", "Mei", "Nanami", "Saki", "Yuna", "Miku", "Haruka"],
        "americano": ["Ashley", "Brittany", "Chloe", "Danielle", "Emily", "Grace", "Hannah", "Isabelle", "Jessica", "Kimberly", "Madison", "Olivia", "Sophia", "Ava", "Mia"],
        "alemao": ["Anja", "Greta", "Heidi", "Lena", "Maria", "Sophie", "Ute", "Hannah", "Julia", "Katharina", "Amelie", "Charlotte", "Frieda", "Ida", "Lina"],
        "russo": ["Anastasia", "Elena", "Irina", "Katerina", "Natalia", "Olga", "Svetlana", "Tatiana", "Viktoria", "Sofia", "Anna", "Daria", "Ekaterina", "Maria", "Polina"],
        "europeu_ocidental": ["Camille", "Manon", "Léa", "Chloé", "Emma", "Louise", "Lucie", "Clara", "Margaux", "Sophie", "Chiara", "Giulia", "Sofia", "Aurora", "Francesca", "Isabella", "Marta", "Nuria", "Paula", "Sara"],
        "europeu_oriental": ["Zofia", "Ewa", "Anna", "Magdalena", "Martyna", "Tereza", "Katarina", "Elena", "Petra", "Monika"]
    }

    nomes_composto_segundo = {
        "M": ["Luiz", "Felipe", "Augusto", "Henrique", "José", "Paulo", "Pedro"],
        "F": ["Maria", "Clara", "Vitória", "Gabriela", "Carolina", "Beatriz", "Joana"]
    }

    sobrenomes = [
        "Silva", "Santos", "Oliveira", "Souza", "Lima", "Ferreira", "Almeida", "Pereira",
        "Rodrigues", "Costa", "Martins", "Carvalho", "Ribeiro", "Gomes", "Dias", "Mendes",
        "Nascimento", "Rocha", "Machado", "Freitas", "Barbosa", "Reis", "Gonçalves", "Fernandes",
        "Vasconcelos", "Moraes", "Castro", "Pinheiro", "Monteiro", "Cavalcanti", "Mesquita",
        "Santana", "Aragão", "Camargo", "Rezende", "Padilha", "Guimarães", "Miranda", "Bittencourt",
        "Andrade", "Dantas", "Pires", "Sales", "Guerra", "Bueno", "Franco", "Tavares", "Correia",
        "Cardoso", "Ramos", "Figueiredo", "Duarte", "Cunha", "Brandão", "Brito", "Pacheco",
        "Schmidt", "Müller", "Schneider", "Fischer", "Weber", "Becker", "Meyer", "Wagner",
        "Garcia", "Rodriguez", "Hernandez", "Lopez", "Martinez", "Gonzalez", "Perez", "Sanchez",
        "Rossi", "Ferrari", "Russo", "Bianchi", "Romano", "Gallo", "Costa", "Fontana",
        "Dubois", "Lefebvre", "Leroy", "Moreau", "Simon", "Laurent", "Michel", "Richard",
        "Smirnov", "Ivanov", "Kuznetsov", "Sokolov", "Vasilev", "Popov", "Novikov", "Mikhailov",
        "Tanaka", "Suzuki", "Sato", "Watanabe", "Takahashi", "Yamamoto", "Nakamura", "Kobayashi"
    ]

    origens = [
        "Acadêmico", "Agente de Saúde", "Amnésico", "Artista", "Atleta", "Cientista", "Criminoso",
        "Cultista Arrependido", "Engenheiro", "Jornalista", "Lutador", "Militar", "Músico",
        "Operário", "Policial", "Religioso", "Servidor Público", "T.I.", "Teórico da Conspiração",
        "Trabalhador Rural", "Universitário", "Veterano", "Chef", "Desgarrado", "Entregador",
        "Garçom", "Herdeiro", "Influenciador", "Morador de Rua", "Professor", "Segurança", "Tradutor"
    ]

    patentes = {
        5: "Recruta", 10: "Recruta", 15: "Recruta",
        20: "Operador", 25: "Operador", 30: "Operador",
        35: "Agente de Campo", 40: "Agente de Campo", 45: "Agente de Campo",
        50: "Agente Especial", 55: "Agente Especial", 60: "Agente Especial",
        65: "Elite", 70: "Elite", 75: "Elite",
        80: "Elite", 85: "Elite", 90: "Elite",
        95: "Elite", 99: "Elite"
    }
    
    elementos_afinidade = ["Morte", "Conhecimento", "Sangue", "Energia", "Medo"]

    # Descrições (Mantidos como V5 para variedade)
    descricoes_fisicas_m = [
        "Um homem de estatura mediana e constituição atlética. Seus cabelos curtos e castanhos combinam com seus olhos penetrantes e expressivos. Geralmente veste roupas práticas.",
        "Um indivíduo robusto, com ombros largos e uma barba bem cuidada. Seus olhos claros contrastam com sua pele bronzeada pelo sol. Tem uma cicatriz discreta na sobrancelha.",
        "Um sujeito magro e alto, com uma postura ligeiramente curvada e um olhar pensativo por trás dos óculos. Seus cabelos são escuros e desalinhados. Quase sempre carrega um caderno.",
        "Um homem jovem com um ar descontraído, sardas no rosto e um sorriso fácil. Seus cabelos loiros caem sobre a testa e seus olhos são curiosos. Parece estar sempre de bom humor.",
        "Uma figura imponente, com feições marcantes e um semblante sério. Seus cabelos grisalhos e curtos denunciam uma vida de experiências. Seus movimentos são precisos e calculados."
    ]

    descricoes_fisicas_f = [
        "Uma mulher de estatura média e porte elegante. Possui cabelos longos e lisos, de cor escura, e olhos amendoados que expressam calma. Veste-se de forma discreta, mas com bom gosto.",
        "Uma jovem de aparência delicada, mas com um brilho determinado nos olhos. Seus cabelos ruivos são cacheados e emolduram um rosto com poucas sardas. Tem uma pequena tatuagem no pulso.",
        "Uma figura atlética e forte, com cabelos curtos e práticos. Seu olhar é direto e confiante, e ela se move com agilidade. Costuma usar roupas confortáveis para se movimentar.",
        "Uma mulher de semblante expressivo, com um sorriso acolhedor e olhos vibrantes. Seus cabelos castanhos são volumosos e cheios de vida. Sua voz é suave, mas firme.",
        "Alguém com um ar misterioso, vestindo roupas que não chamam a atenção. Seus olhos escuros parecem observar tudo ao redor com atenção. Quase nunca revela suas emoções."
    ]

    descricoes_personalidade = [
        "Pragmático e lógico, prefere agir com base em fatos e dados. Pode parecer um pouco frio(a) à primeira vista, mas é extremamente leal aos que confia. Tem dificuldade em expressar sentimentos.",
        "Extremamente curioso(a) e com uma sede insaciável por conhecimento. Gosta de investigar e desvendar mistérios, mas pode se perder em seus próprios pensamentos. É um(a) pouco distraído(a).",
        "Impulsivo(a) e corajoso(a), sempre pronto(a) para a ação. Tende a resolver problemas com força e determinação, mas às vezes age sem pensar nas consequências. É muito protetor(a).",
        "Calmo(a) e observador(a), com uma paciência notável. Prefere planejar antes de agir e raramente se desespera, sendo um pilar de estabilidade para o grupo. Tem um senso de humor sutil.",
        "Um(a) líder nato(a), com carisma e capacidade de inspirar outros. Protege seus aliados com ferocidade e tem um forte senso de justiça. Pode ser um(a) tanto teimoso(a).",
        "Um tanto cético(a) e desconfiado(a), especialmente em relação ao paranormal. Precisa de provas concretas para acreditar, o que o(a) torna um(a) bom(boa) investigador(a). É reservado(a).",
        "Excêntrico(a) e com um humor peculiar, às vezes difícil de entender. Possui uma mente brilhante, mas que funciona de maneiras não convencionais. Adora quebra-cabeças.",
        "Sensível e empático(a), com grande capacidade de compreender os sentimentos alheios. Pode ser facilmente afetado(a) pelas emoções de outras pessoas. É muito intuitivo(a)."
    ]

    historias_breves = [
        "Um(a) ex-universitário(a) que se deparou com o Outro Lado após uma pesquisa acadêmica mal sucedida. Agora busca respostas e vingança.",
        "Era um(a) profissional comum até que um evento paranormal em sua vida o(a) forçou a ver a realidade por trás do véu. Luta para proteger os inocentes.",
        "Um(a) agente da Ordem desde cedo, treinado(a) para lidar com o paranormal. Conhece os perigos, mas também o preço da verdade.",
        "Um(a) sobrevivente de um culto, que conseguiu escapar e agora usa seu conhecimento sombrio contra as forças que antes servia.",
        "Um(a) artista que passou a canalizar o medo em suas obras após um encontro bizarro. Seus talentos agora são usados para o combate.",
        "Um(a) ex-militar com traumas de guerra que encontrou no paranormal um novo tipo de conflito para lutar. Busca redenção em cada missão."
    ]

    # Itens (Expandidos e mais focados em Ordem Paranormal)
    armas_brancas_leves = [
        "Faca de Caça", "Cassetete Extensível", "Soqueira Reforçada", "Machadinha", "Faca de Arremesso (x3)",
        "Adaga", "Pé de Cabra", "Bastão Retrátil"
    ]
    armas_brancas_pesadas = [
        "Katana", "Espada Larga", "Martelo de Guerra", "Foice", "Marreta",
        "Alabarda", "Gadanha", "Montante"
    ]
    armas_de_fogo_leves = [
        "Pistola (Cal. .38)", "Revólver (Cal. .357)", "SMG (Submetralhadora .45)", "Pistola de Bolso (Cal. .22)",
        "Pistola (9mm)", "Revólver (.38)"
    ]
    armas_de_fogo_pesadas = [
        "Escopeta de Combate (Cal. 12)", "Fuzil de Assalto (5.56mm)", "Rifle de Precisão (.308)",
        "Lançador de Granadas (não-letal)", "Escopeta de Caça (Cal. 20)", "Fuzil de Caça (.30-06)"
    ]
    protecoes = [
        "Colete Balístico (Leve)", "Colete Balístico (Pesado)", "Capuz de Furtividade", "Máscara de Gás",
        "Capacete Tático", "Armadura Leve (Reforçada)", "Armadura Pesada (Reforçada)"
    ]
    equipamentos_gerais = [
        "Kit de Primeiros Socorros", "Kit de Perícia (simples)", "Lanterna Tática", "Binóculos Militares",
        "Rádio Comunicador (Portátil)", "Algemas de Polímero", "Ganzuas de Titânio", "Corda (20m)",
        "Mochila de Expedição", "Óculos de Visão Noturna (básico)", "Drone de Reconhecimento (Pequeno)",
        "Bateria Extra (Universal)", "Kit de Ferramentas", "PDA Tático", "GPS de Mão", "Fita Adesiva Reforçada",
        "Câmera Digital", "Gravador de Voz", "Kit de Limpeza de Arma"
    ]
    componentes_rituais = [
        "Sangue Coagulado (Frasco)", "Vela de Sebo Consagrada", "Tinta de Ossos Triturados", "Giz de Sacrifício",
        "Olho de Corvo mumificado", "Pó de Morte", "Fio de Cabelo (Comum)", "Amuleto Quebrado", "Ervas Secas Estranhas",
        "Sal Negro", "Essência de Medo (Frasco Pequeno)"
    ]

    # --- Habilidades de Trilha OFICIAIS (Conforme o livro base de Ordem Paranormal) ---
    # CORREÇÃO: Envolva as habilidades em uma chave 'habilidades'
    classes_trilhas_habilidades = {
        "Combatente": {
            "trilhas": {
                "Aniquilador": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Ataque Pesado", "descricao": "Uma vez por rodada, você pode gastar 1 PE para aumentar o dano do seu próximo ataque em +1d8."},
                        40: {"nome": "Golpe de Sorte", "descricao": "Quando você causa dano crítico com um ataque corpo a corpo, pode gastar 2 PE para fazer o alvo sofrer 1d8 de dano de Sangue adicional."},
                        65: {"nome": "Dilacerar", "descricao": "Quando você acerta um ataque corpo a corpo com uma arma de duas mãos, o alvo sofre +1d6 de dano de corte para cada 2 PE que você gastar (máx. 3d6)."},
                        99: {"nome": "Massacre", "descricao": "Uma vez por cena, você pode gastar 5 PE para, no seu próximo ataque, o dano excedente do alvo que o levaria a 0 PV ser redirecionado a outro alvo adjacente."}
                    }
                },
                "Comandante de Campo": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Comandar", "descricao": "Você pode gastar 1 PE e uma ação de movimento para conceder um bônus de +2 em um teste de perícia ou ataque a um aliado em alcance curto."},
                        40: {"nome": "Posicionamento Tático", "descricao": "Uma vez por rodada, você pode gastar 2 PE para mover um aliado em alcance curto em até 3m como reação, desde que ele não esteja engajado."},
                        65: {"nome": "Liderar Ataque", "descricao": "Quando você acerta um ataque, pode gastar 3 PE para que todos os aliados em alcance curto recebam +2 em seus próximos testes de ataque contra o mesmo alvo."},
                        99: {"nome": "Liderança Suprema", "descricao": "Todos os aliados em alcance médio recebem +1 em Defesa e +1 em testes de ataque enquanto você estiver em combate."}
                    }
                },
                "Guerreiro": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Ataque Furioso", "descricao": "Você pode gastar 1 PE para realizar um ataque corpo a corpo adicional com sua arma principal."},
                        40: {"nome": "Técnica de Luta", "descricao": "Você pode gastar 2 PE para receber +5 em um teste de Luta ou na Defesa por uma rodada."},
                        65: {"nome": "Ataque Defensivo", "descricao": "Quando você acerta um ataque corpo a corpo, você pode gastar 3 PE para receber +2 na Defesa até o início do seu próximo turno."},
                        99: {"nome": "Imparável", "descricao": "Uma vez por cena, você pode gastar 5 PE para ignorar penalidades de ferimentos e condições (ex: Sangramento, Exausto) por 1 rodada."}
                    }
                },
                "Operador Especial": { # Essa trilha não é oficial do livro base. Adaptada para o contexto.
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Treinamento Tático", "descricao": "Você recebe +2 em testes de Tática ou Tecnologia."},
                        40: {"nome": "Preparar Ação", "descricao": "Você pode preparar uma ação para ser executada quando uma condição específica for atendida, ganhando +5 no teste."},
                        65: {"nome": "Ataque Cirúrgico", "descricao": "Ao atacar um ponto vital (cabeça), você pode gastar 3 PE para ignorar a penalidade de -2 no teste de ataque."},
                        99: {"nome": "Mestre Tático", "descricao": "Uma vez por cena, você pode gastar 5 PE para conceder uma ação de movimento extra a todos os aliados em alcance médio."}
                    }
                }
            },
            "pericias_base_treinadas": ["Luta", "Pontaria", "Fortitude"],
            "pericias_treinadas_adicionais_base": 2
        },
        "Especialista": {
            "trilhas": {
                "Atirador de Elite": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Mira Mortal", "descricao": "Ao realizar um ataque à distância, você pode gastar 1 PE para receber +5 no teste de ataque."},
                        40: {"nome": "Tiro Preciso", "descricao": "Você pode gastar 2 PE para mirar em um ponto específico de um alvo, recebendo +5 no teste de ataque para causar um efeito (ex: desarmar, derrubar)."},
                        65: {"nome": "Tiro Múltiplo", "descricao": "Uma vez por rodada, você pode gastar 3 PE para fazer dois ataques com sua arma à distância contra o mesmo alvo."},
                        99: {"nome": "Chuva de Balas", "descricao": "Uma vez por cena, você pode gastar 5 PE para fazer um ataque à distância contra todos os inimigos em um cone de 9m."}
                    }
                },
                "Infiltrador": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Mãos Leves", "descricao": "Você recebe +2 em testes de Crime ou Furtividade."},
                        40: {"nome": "Assassinar", "descricao": "Quando você ataca um alvo desprevenido, pode gastar 2 PE para causar +1d6 de dano adicional por cada 2 PE gastos (máx. 3d6)."},
                        65: {"nome": "Fuga Rápida", "descricao": "Uma vez por cena, você pode gastar 3 PE para realizar uma ação de movimento e uma ação padrão (ou vice-versa) na mesma rodada."},
                        99: {"nome": "Sombra e Silêncio", "descricao": "Você pode gastar 5 PE para se tornar invisível e indetectável para todos os sentidos por uma rodada."}
                    }
                },
                "Investigador": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Perícia", "descricao": "Escolha uma perícia (exceto Luta ou Pontaria). Você recebe +2 em testes dessa perícia."},
                        40: {"nome": "Olhar Atento", "descricao": "Você pode gastar 2 PE para receber +5 em um teste de Percepção ou Investigação."},
                        65: {"nome": "Mente Aberta", "descricao": "Uma vez por cena, você pode gastar 3 PE para refazer um teste de Investigação, Conhecimento ou Ocultismo."},
                        99: {"nome": "Desvendando o Oculto", "descricao": "Você pode gastar 5 PE para fazer uma pergunta ao mestre sobre um enigma ou mistério e receber uma resposta útil."}
                    }
                },
                "Médico de Campo": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Primeiros Socorros Avançados", "descricao": "Você pode gastar 1 PE para adicionar +5 em um teste de Medicina para curar."},
                        40: {"nome": "Resgate Rápido", "descricao": "Você pode gastar 2 PE para realizar uma ação de movimento e uma ação padrão (para curar) na mesma rodada."},
                        65: {"nome": "Cirurgia de Campo", "descricao": "Uma vez por cena, você pode gastar 4 PE para estabilizar um aliado morrendo e curar 2d6 PV."},
                        99: {"nome": "Milagreiro", "descricao": "Uma vez por missão, você pode gastar 5 PE para remover uma condição severa (ex: morrendo, inconsciente) de um aliado."}
                    }
                },
                "Técnico": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Gambiarra", "descricao": "Você pode gastar 1 PE para improvisar uma ferramenta ou consertar um objeto simples com um teste de Tecnologia."},
                        40: {"nome": "Modificar Arma", "descricao": "Você pode gastar 2 PE para adicionar um modificador temporário a uma arma (ex: +1 dano, +1 alcance)."},
                        65: {"nome": "Dispositivo Especial", "descricao": "Você pode gastar 3 PE para criar um dispositivo tático simples (ex: mina de proximidade, flashbang) com um teste de Tecnologia."},
                        99: {"nome": "Gênio da Tecnologia", "descricao": "Você pode gastar 5 PE para desativar qualquer dispositivo eletrônico em alcance médio por uma rodada."}
                    }
                }
            },
            "pericias_base_treinadas": ["Investigação", "Tecnologia", "Percepção"],
            "pericias_treinadas_adicionais_base": 3
        },
        "Ocultista": {
            "trilhas": {
                "Conjurador": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Poder Oculto", "descricao": "Você recebe +1d4 nas rolagens de dano de rituais com seu elemento de afinidade."},
                        40: {"nome": "Vínculo com Elemento", "descricao": "Uma vez por cena, você pode gastar 2 PE para lançar um ritual de seu elemento sem custo de PE na próxima rodada."},
                        65: {"nome": "Ritual Potente", "descricao": "Uma vez por cena, você pode gastar 4 PE para lançar um ritual com seu elemento de afinidade que não pode ser resistido por Vontade."},
                        99: {"nome": "Mestre dos Rituais", "descricao": "Uma vez por rodada, você pode gastar 5 PE para lançar dois rituais na mesma rodada, um padrão e um de movimento, ambos do seu elemento de afinidade."}
                    }
                },
                "Graduado": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Estudioso do Paranormal", "descricao": "Você recebe +2 em testes de Ocultismo ou Ciências para identificar criaturas ou rituais."},
                        40: {"nome": "Conhecimento Proibido", "descricao": "Você pode gastar 2 PE para obter uma informação rara ou secreta sobre o Outro Lado, com um teste de Ocultismo."},
                        65: {"nome": "Sabedoria Arcana", "descricao": "Uma vez por cena, você pode gastar 3 PE para refazer um teste de Ocultismo ou Vontade."},
                        99: {"nome": "Oráculo do Outro Lado", "descricao": "Você pode gastar 5 PE para fazer uma pergunta ao mestre sobre um enigma ou mistério e receber uma resposta útil."}
                    }
                },
                "Lâmina Paranormal": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Ataque Sombrio", "descricao": "Ao atacar com uma arma corpo a corpo, você pode gastar 1 PE para adicionar +1d4 de dano paranormal (do seu elemento de afinidade)."},
                        40: {"nome": "Convicção Paranormal", "descricao": "Você recebe +2 na Defesa contra ataques de criaturas paranormais."},
                        65: {"nome": "Forma Monstruosa", "descricao": "Uma vez por cena, você pode gastar 4 PE para transformar seu corpo, ganhando +2 em Força e Vigor por uma rodada."},
                        99: {"nome": "Encarnação do Medo", "descricao": "Você pode gastar 5 PE para se tornar uma manifestação do medo por uma rodada, aterrorizando inimigos próximos e ganhando resistência a dano."}
                    }
                },
                "Intuitivo": {
                    "habilidades": { # Adicionado a chave 'habilidades'
                        10: {"nome": "Sentir o Paranormal", "descricao": "Você pode gastar 1 PE para sentir a presença de energia paranormal em alcance curto."},
                        40: {"nome": "Visão do Outro Lado", "descricao": "Você pode gastar 2 PE para enxergar o que está oculto pelo paranormal, revelando ilusões ou disfarces."},
                        65: {"nome": "Conexão Sobrenatural", "descricao": "Uma vez por cena, você pode gastar 3 PE para se comunicar brevemente com uma entidade paranormal para obter informações."},
                        99: {"nome": "Mente do Paranormal", "descricao": "Você pode gastar 5 PE para ter um vislumbre do futuro ou passado paranormal, obtendo uma dica crucial para a investigação."}
                    }
                }
            },
            "pericias_base_treinadas": ["Ocultismo", "Vontade", "Intuição"],
            "pericias_treinadas_adicionais_base": 2
        }
    }

    # Mapeamento de perícias para atributos (nomes completos dos atributos)
    pericias_atributos = {
        "Acrobacia": "Agilidade", "Adestramento": "Presença", "Artes": "Presença", "Atletismo": "Força",
        "Atualidades": "Intelecto", "Ciências": "Intelecto", "Crime": "Agilidade", "Diplomacia": "Presença",
        "Enganação": "Presença", "Fortitude": "Vigor", "Furtividade": "Agilidade", "Iniciativa": "Agilidade",
        "Intimidação": "Presença", "Intuição": "Presença", "Investigação": "Intelecto", "Luta": "Força",
        "Medicina": "Intelecto", "Ocultismo": "Intelecto", "Percepção": "Presença", "Pilotagem": "Agilidade",
        "Pontaria": "Agilidade", "Profissão": "Intelecto", "Reflexos": "Agilidade", "Religião": "Presença",
        "Sobrevivência": "Intelecto", "Tática": "Intelecto", "Tecnologia": "Intelecto", "Vontade": "Presença"
    }

    # --- Rituais Oficiais (Conforme o livro base de Ordem Paranormal) ---
    rituais_por_elemento_detalhes = {
        "Morte": {
            "Decadência": "Custo: 1 PE. Alvo único. O alvo sofre 1d6 de dano de Morte e fica fraco (–2 em testes de Força e Vigor) por 1 rodada. Discente: 3 PE. O dano aumenta para 2d6 e o alvo fica fraco por 1d4 rodadas. Verdadeiro: 5 PE. O dano aumenta para 3d6 e o alvo fica fraco por 1d6 rodadas.",
            "Eletrocussão": "Custo: 1 PE. Alvo único. O alvo sofre 1d6 de dano de Energia e fica desprevenido (–2 na Defesa) por 1 rodada. Discente: 3 PE. O dano aumenta para 2d6 e o alvo fica desprevenido por 1d4 rodadas. Verdadeiro: 5 PE. O dano aumenta para 3d6 e o alvo fica desprevenido por 1d6 rodadas.",
            "Ódio Incontrolável": "Custo: 2 PE. Alvo único. O alvo deve fazer um teste de Vontade. Se falhar, é tomado pelo ódio e ataca a criatura mais próxima (incluindo aliados) por 1 rodada. Discente: 4 PE. O efeito dura 1d4 rodadas. Verdadeiro: 6 PE. O efeito dura 1d6 rodadas.",
            "Paradoxo": "Custo: 3 PE. Alvo único. O alvo deve fazer um teste de Vontade. Se falhar, sofre 2d6 de dano de Conhecimento e fica confuso (age aleatoriamente) por 1 rodada. Discente: 6 PE. O dano aumenta para 4d6 e o efeito dura 1d4 rodadas. Verdadeiro: 9 PE. O dano aumenta para 6d6 e o efeito dura 1d6 rodadas.",
            "Definhar": "Custo: 2 PE. Alvo único. O alvo sofre 1d6 de dano de Morte por rodada e não pode se curar por 1d4 rodadas. Discente: 4 PE. O dano aumenta para 2d6 por rodada e o efeito dura 1d6 rodadas. Verdadeiro: 6 PE. O dano aumenta para 3d6 por rodada e o efeito dura 1d8 rodadas.",
            "Contorção": "Custo: 2 PE. Alvo único. O alvo sofre 1d6 de dano de Sangue e fica caído (derrubado) por 1 rodada. Discente: 4 PE. O dano aumenta para 2d6 e o alvo fica caído por 1d4 rodadas. Verdadeiro: 6 PE. O dano aumenta para 3d6 e o alvo fica caído por 1d6 rodadas."
        },
        "Conhecimento": {
            "Cicatrização": "Custo: 1 PE. Alvo único. Cura 1d6 PV do alvo. Discente: 3 PE. Cura 2d6 PV. Verdadeiro: 5 PE. Cura 3d6 PV. Pode remover 1d4 pontos de Sanidade se usado em si mesmo.",
            "Amaldiçoar Arma": "Custo: 2 PE. Arma tocada. A arma causa +1d6 de dano do elemento de afinidade do conjurador por 1d4 rodadas. Discente: 4 PE. O dano aumenta para +2d6 e dura 1d6 rodadas. Verdadeiro: 6 PE. O dano aumenta para +3d6 e dura 1d8 rodadas.",
            "Embaralhar": "Custo: 2 PE. Alvo único. O alvo deve fazer um teste de Vontade. Se falhar, tem dificuldade de distinguir aliados de inimigos por 1 rodada. Discente: 4 PE. O efeito dura 1d4 rodadas. Verdadeiro: 6 PE. O efeito dura 1d6 rodadas.",
            "Incapacitar": "Custo: 3 PE. Alvo único. O alvo deve fazer um teste de Vontade. Se falhar, fica paralisado (não pode agir) por 1 rodada. Discente: 6 PE. O efeito dura 1d4 rodadas. Verdadeiro: 9 PE. O efeito dura 1d6 rodadas.",
            "Perturbação": "Custo: 2 PE. Alvo único. O alvo sofre 1d6 de dano de Sanidade e fica desorientado (–2 em todos os testes) por 1 rodada. Discente: 4 PE. O dano aumenta para 2d6 e o efeito dura 1d4 rodadas. Verdadeiro: 6 PE. O dano aumenta para 3d6 e o efeito dura 1d6 rodadas.",
            "Aprimorar Mente": "Custo: 1 PE. Alvo único. O alvo recebe +2 em testes de Intelecto por 1 rodada. Discente: 3 PE. O bônus aumenta para +4 e dura 1d4 rodadas. Verdadeiro: 5 PE. O bônus aumenta para +6 e dura 1d6 rodadas."
        },
        "Sangue": {
            "Amedrontar": "Custo: 1 PE. Alvo único. O alvo deve fazer um teste de Vontade. Se falhar, fica abalado (–2 em testes) por 1 rodada. Discente: 3 PE. O efeito dura 1d4 rodadas. Verdadeiro: 5 PE. O efeito dura 1d6 rodadas.",
            "Cineraria": "Custo: 3 PE. Alvo único. O alvo sofre 2d6 de dano de Morte e Sangue. Discente: 6 PE. O dano aumenta para 4d6. Verdadeiro: 9 PE. O dano aumenta para 6d6.",
            "Flagelo": "Custo: 2 PE. Cone de 6m. Todos os alvos na área sofrem 1d6 de dano de Sangue e ficam sangrando por 1 rodada. Discente: 4 PE. O dano aumenta para 2d6 e o sangramento dura 1d4 rodadas. Verdadeiro: 6 PE. O dano aumenta para 3d6 e o sangramento dura 1d6 rodadas.",
            "Drenar Vitalidade": "Custo: 2 PE. Alvo único. Você causa 1d6 de dano de Sangue ao alvo e cura 1d6 PV. Discente: 4 PE. O dano e a cura aumentam para 2d6. Verdadeiro: 6 PE. O dano e a cura aumentam para 3d6.",
            "Poder Rubro": "Custo: 1 PE. Alvo único. O alvo recebe +2 em testes de Força e Vigor por 1 rodada. Discente: 3 PE. O bônus aumenta para +4 e dura 1d4 rodadas. Verdadeiro: 5 PE. O bônus aumenta para +6 e dura 1d6 rodadas.",
            "Convocação de Sangue": "Custo: 3 PE. Uma criatura de Sangue (ex: Zumbi de Sangue) é conjurada para lutar ao seu lado por 1d4 rodadas. Discente: 6 PE. Dura 1d6 rodadas. Verdadeiro: 9 PE. Dura 1d8 rodadas."
        },
        "Energia": {
            "Choque": "Custo: 1 PE. Alvo único. O alvo sofre 1d6 de dano de Energia e fica atordoado por 1 rodada. Discente: 3 PE. O dano aumenta para 2d6 e o efeito dura 1d4 rodadas. Verdadeiro: 5 PE. O dano aumenta para 3d6 e o efeito dura 1d6 rodadas.",
            "Acalmar": "Custo: 1 PE. Alvo único. Remove as condições Abalado, Apavorado ou Enlouquecido do alvo. Discente: 3 PE. Pode remover mais de uma condição. Verdadeiro: 5 PE. Pode remover condições mais severas (a critério do mestre).",
            "Coincidência Forçada": "Custo: 2 PE. Alvo único. Você pode gastar 2 PE para forçar um teste de sorte (d20). Se o resultado for 10 ou mais, um evento improvável e benéfico acontece. Discente: 4 PE. Você recebe +5 no teste. Verdadeiro: 6 PE. Você recebe +10 no teste.",
            "Infligir Medo": "Custo: 2 PE. Alvo único. O alvo deve fazer um teste de Vontade. Se falhar, fica Apavorado por 1 rodada (deve fugir). Discente: 4 PE. O efeito dura 1d4 rodadas. Verdadeiro: 6 PE. O efeito dura 1d6 rodadas.",
            "Visão do Medo": "Custo: 3 PE. Alvo único. O alvo sofre 2d6 de dano de Sanidade e deve fazer um teste de Vontade. Se falhar, fica Enlouquecido por 1 rodada. Discente: 6 PE. O dano aumenta para 4d6 e o efeito dura 1d4 rodadas. Verdadeiro: 9 PE. O dano aumenta para 6d6 e o efeito dura 1d6 rodadas.",
            "Distração": "Custo: 1 PE. Área de 6m. Cria uma ilusão sonora ou visual que distrai criaturas na área, tornando-as desprevenidas por 1 rodada. Discente: 3 PE. Dura 1d4 rodadas. Verdadeiro: 5 PE. Dura 1d6 rodadas."
        },
        "Medo": { # Rituais de Medo são mais complexos e podem não ter uma única versão "oficial" padrão para todos. Manteremos exemplos fortes.
            "Aprimorar Mente (Medo)": "Custo: 4 PE. Alvo único. O alvo recebe +5 em testes de Intelecto por 1d4 rodadas, mas sofre 1d6 de dano de Sanidade.",
            "Aprimorar Físico (Medo)": "Custo: 4 PE. Alvo único. O alvo recebe +5 em testes de Força e Vigor por 1d4 rodadas, mas sua aparência se torna perturbadora (Desvantagem em testes de Diplomacia).",
            "Aprimorar Sentidos (Medo)": "Custo: 4 PE. Alvo único. O alvo recebe +5 em testes de Percepção e Iniciativa por 1d4 rodadas, mas tem desvantagem em testes de Vontade contra efeitos de Medo.",
            "Aprimorar Habilidade (Medo)": "Custo: 5 PE. Alvo único. O alvo recebe +10 em um teste de perícia à escolha do conjurador. Se o teste for um sucesso, o alvo sofre 1d6 de dano de Sanidade. Se falhar, sofre 2d6 de dano de Sanidade.",
            "Paradoxo (Medo)": "Custo: 7 PE. Área de 9m. A realidade na área é distorcida. Criaturas na área devem fazer um teste de Vontade ou sofrem 3d6 de dano de Sanidade e uma condição aleatória (ex: caído, desprevenido, atordoado).",
            "Distorção (Medo)": "Custo: 8 PE. Alvo único. O alvo é teleportado para um espaço aleatório em alcance médio. Se o espaço estiver ocupado, o alvo sofre 4d6 de dano de Energia."
        }
    }

    # Mapeamento de perícias para atributos (nomes completos dos atributos)
    pericias_atributos = {
        "Acrobacia": "Agilidade", "Adestramento": "Presença", "Artes": "Presença", "Atletismo": "Força",
        "Atualidades": "Intelecto", "Ciências": "Intelecto", "Crime": "Agilidade", "Diplomacia": "Presença",
        "Enganação": "Presença", "Fortitude": "Vigor", "Furtividade": "Agilidade", "Iniciativa": "Agilidade",
        "Intimidação": "Presença", "Intuição": "Presença", "Investigação": "Intelecto", "Luta": "Força",
        "Medicina": "Intelecto", "Ocultismo": "Intelecto", "Percepção": "Presença", "Pilotagem": "Agilidade",
        "Pontaria": "Agilidade", "Profissão": "Intelecto", "Reflexos": "Agilidade", "Religião": "Presença",
        "Sobrevivência": "Intelecto", "Tática": "Intelecto", "Tecnologia": "Intelecto", "Vontade": "Presença"
    }

    # --- Funções Auxiliares (Mantidas as mesmas) ---
    def gerar_nome_completo_e_genero(genero_escolhido=None, nacionalidade_escolhida=None):
        if genero_escolhido:
            genero = genero_escolhido
        else:
            genero = random.choice(["M", "F"])

        if nacionalidade_escolhida:
            nacionalidade = nacionalidade_escolhida
        else:
            nacionalidade = random.choice(list(nomes_masculinos.keys()) if genero == "M" else list(nomes_femininos.keys()))
        
        primeiro_nome = random.choice(nomes_masculinos[nacionalidade] if genero == "M" else nomes_femininos[nacionalidade])
        
        nome_completo = primeiro_nome
        if random.random() < 0.35:
            nome_completo += " " + random.choice(nomes_composto_segundo[genero])
        
        sobrenome1 = random.choice(sobrenomes)
        sobrenome2 = random.choice(sobrenomes)
        while sobrenome2 == sobrenome1:
            sobrenome2 = random.choice(sobrenomes)

        if random.random() < 0.7:
            nome_completo += " " + sobrenome1 + " " + sobrenome2
        else:
            nome_completo += " " + sobrenome1
        return nome_completo, genero, nacionalidade

    def gerar_atributos_com_limite(nex):
        if nex <= 30:
            limite = 3
        elif nex <= 65:
            limite = 4
        else:
            limite = 5
        
        pontos_distribuir = 0
        if nex >= 5: pontos_distribuir += 1
        if nex >= 15: pontos_distribuir += 1
        if nex >= 30: pontos_distribuir += 1
        if nex >= 45: pontos_distribuir += 1
        if nex >= 60: pontos_distribuir += 1
        if nex >= 75: pontos_distribuir += 1
        if nex >= 90: pontos_distribuir += 1

        atributos_base = {"Força": 1, "Agilidade": 1, "Intelecto": 1, "Vigor": 1, "Presença": 1}
        
        atributos_lista = list(atributos_base.keys())
        for _ in range(pontos_distribuir):
            attr_candidatos = [a for a in atributos_lista if atributos_base[a] < limite]
            if not attr_candidatos:
                break
            attr_escolhido = random.choice(attr_candidatos)
            atributos_base[attr_escolhido] += 1
        return atributos_base

    def calcular_pericia_valor(valor_do_atributo, treinada=False):
        if treinada:
            return valor_do_atributo + 5 # O +5 é fixo em Ordem para perícias treinadas
        return valor_do_atributo

    # --- INÍCIO DA INTERFACE ---
    clear_screen()
    exibir_titulo("GERADOR DE FICHAS DE ORDEM PARANORMAL")

    # 1. Escolha de NEX
    print("--- Escolha o Nível de Exposição (NEX) ---")
    nex_opcoes = sorted(list(patentes.keys()))
    # Exibe NEX em duas colunas se houver mais de 10 opções
    exibir_menu([f"{n}% - Patente: {patentes[n]}" for n in nex_opcoes], colunas=2 if len(nex_opcoes) > 10 else 1)
    escolha_nex_idx = obter_escolha("Digite o número do NEX desejado: ", len(nex_opcoes))
    nex_escolhido = nex_opcoes[escolha_nex_idx - 1]
    
    clear_screen()
    exibir_titulo("GERADOR DE FICHAS DE ORDEM PARANORMAL")

    # 2. Escolha de Gênero
    print("--- Escolha o Gênero ---")
    genero_opcoes = ["Masculino", "Feminino", "Aleatório"]
    exibir_menu(genero_opcoes)
    escolha_genero_idx = obter_escolha("Digite o número do gênero desejado: ", len(genero_opcoes))
    genero_selecionado = None
    if escolha_genero_idx == 1: genero_selecionado = "M"
    elif escolha_genero_idx == 2: genero_selecionado = "F"

    clear_screen()
    exibir_titulo("GERADOR DE FICHAS DE ORDEM PARANORMAL")

    # 3. Escolha de Nacionalidade
    print("--- Escolha a Nacionalidade do Nome ---")
    nacionalidade_opcoes = ["Aleatória"] + sorted(list(set(list(nomes_masculinos.keys()) + list(nomes_femininos.keys()))))
    exibir_menu(nacionalidade_opcoes, colunas=2 if len(nacionalidade_opcoes) > 5 else 1) # Nacionalidade também em duas colunas
    escolha_nacionalidade_idx = obter_escolha("Digite o número da nacionalidade desejada: ", len(nacionalidade_opcoes))
    nacionalidade_selecionada = None
    if escolha_nacionalidade_idx > 1:
        nacionalidade_selecionada = nacionalidade_opcoes[escolha_nacionalidade_idx - 1]

    clear_screen()
    exibir_titulo("GERADOR DE FICHAS DE ORDEM PARANORMAL")

    # 4. Escolha de Classe
    print("--- Escolha a Classe ---")
    classe_opcoes = sorted(list(classes_trilhas_habilidades.keys()))
    exibir_menu(classe_opcoes + ["Aleatória"])
    escolha_classe_idx = obter_escolha("Digite o número da classe desejada: ", len(classe_opcoes) + 1)
    
    classe_escolhida = None
    if escolha_classe_idx <= len(classe_opcoes):
        classe_escolhida = classe_opcoes[escolha_classe_idx - 1]
    else:
        classe_escolhida = random.choice(list(classes_trilhas_habilidades.keys()))

    clear_screen()
    exibir_titulo("GERADOR DE FICHAS DE ORDEM PARANORMAL")

    # 5. Escolha de Trilha
    trilha_escolhida = None
    trilhas_da_classe_atual = list(classes_trilhas_habilidades[classe_escolhida]["trilhas"].keys())

    print(f"--- Escolha a Trilha para {classe_escolhida} ---")
    exibir_menu(trilhas_da_classe_atual + ["Aleatória"], colunas=2 if len(trilhas_da_classe_atual) > 3 else 1) # Trilhas também em duas colunas
    escolha_trilha_idx = obter_escolha("Digite o número da trilha desejada: ", len(trilhas_da_classe_atual) + 1)
    
    if escolha_trilha_idx <= len(trilhas_da_classe_atual):
        trilha_escolhida = trilhas_da_classe_atual[escolha_trilha_idx - 1]
    else:
        trilha_escolhida = random.choice(trilhas_da_classe_atual)

    clear_screen()
    exibir_titulo("GERADOR DE FICHAS DE ORDEM PARANORMAL")

    # --- Geração dos Dados do Personagem ---
    nome, genero_real, nacionalidade_real = gerar_nome_completo_e_genero(genero_selecionado, nacionalidade_selecionada)
    origem = random.choice(origens)
    patente = patentes[nex_escolhido]
    
    descricao_fisica = random.choice(descricoes_fisicas_m if genero_real == "M" else descricoes_fisicas_f)
    descricao_personalidade = random.choice(descricoes_personalidade)
    historia_breve = random.choice(historias_breves)

    idade = random.randint(18, 50)
    altura = round(random.uniform(1.60, 1.95), 2)

    atributos = gerar_atributos_com_limite(nex_escolhido)

    # Acessa as habilidades corretamente agora que estão aninhadas
    habilidades_da_trilha = classes_trilhas_habilidades[classe_escolhida]["trilhas"][trilha_escolhida]["habilidades"]
    habilidades_personagem = []
    for nex_habilidade, hab_info in habilidades_da_trilha.items():
        if nex_escolhido >= nex_habilidade:
            habilidades_personagem.append(f"- **{hab_info['nome']}** (NEX {nex_habilidade}%): {hab_info['descricao']}")

    # Perícias
    pericias_personagem_valores = {}
    pericias_treinadas_pool = set()

    for pericia in classes_trilhas_habilidades[classe_escolhida]["pericias_base_treinadas"]:
        pericias_treinadas_pool.add(pericia)

    num_pericias_adicionais_treinadas = classes_trilhas_habilidades[classe_escolhida]["pericias_treinadas_adicionais_base"] + atributos["Intelecto"]
    
    pericias_disponiveis_para_treinar = [p for p in pericias_atributos.keys() if p not in pericias_treinadas_pool]
    num_pericias_adicionais_treinadas = min(num_pericias_adicionais_treinadas, len(pericias_disponiveis_para_treinar))
    
    pericias_extras_treinadas = random.sample(pericias_disponiveis_para_treinar, num_pericias_adicionais_treinadas)
    for p in pericias_extras_treinadas:
        pericias_treinadas_pool.add(p)

    for pericia_nome, atributo_chave_completo in pericias_atributos.items():
        atributo_valor = atributos[atributo_chave_completo]
        eh_treinada = pericia_nome in pericias_treinadas_pool
        pericias_personagem_valores[pericia_nome] = calcular_pericia_valor(atributo_valor, treinada=eh_treinada)

    # Elemento de Afinidade e Rituais
    elemento_afinidade = "Nenhum"
    rituais_personagem = []
    if classe_escolhida == "Ocultista":
        elemento_afinidade = random.choice(elementos_afinidade)
        num_rituais_possiveis = (nex_escolhido // 15) + 1
        
        # Filtra rituais do elemento escolhido
        rituais_do_elemento = list(rituais_por_elemento_detalhes[elemento_afinidade].keys())
        # CORREÇÃO: Usar len() para verificar o tamanho da lista
        if len(rituais_do_elemento) > 0:
            num_rituais_a_escolher = min(num_rituais_possiveis, len(rituais_do_elemento))
            rituais_escolhidos_nomes = random.sample(rituais_do_elemento, num_rituais_a_escolher)
            for r_nome in rituais_escolhidos_nomes:
                rituais_personagem.append(f"- **{r_nome}**: {rituais_por_elemento_detalhes[elemento_afinidade][r_nome]}")

    # Itens
    itens_personagem = []
    # Garante que sempre tenha uma arma de fogo leve
    itens_personagem.append(random.choice(armas_de_fogo_leves))
    
    # Chance de arma branca leve
    if random.random() < 0.6:
        itens_personagem.append(random.choice(armas_brancas_leves))
    
    # 2 a 4 equipamentos gerais
    num_equipamentos = random.randint(2, min(4, len(equipamentos_gerais)))
    itens_personagem.extend(random.sample(equipamentos_gerais, num_equipamentos))

    # Itens adicionais por NEX
    if nex_escolhido >= 20:
        if random.random() < 0.7:
            itens_personagem.append(random.choice(protecoes))
    if nex_escolhido >= 40:
        if random.random() < 0.5:
            itens_personagem.append(random.choice(armas_de_fogo_pesadas))
        if random.random() < 0.3:
            itens_personagem.append(random.choice(armas_brancas_pesadas))

    if classe_escolhida == "Ocultista":
        itens_personagem.extend(random.sample(componentes_rituais, random.randint(1, min(2, len(componentes_rituais)))))

    itens_personagem = sorted(list(set(itens_personagem))) # Remove duplicatas e organiza

    # --- MONTA A FICHA DE TEXTO ---
    ficha_conteudo = f"""
============================================================
              FICHA DE ORDEM PARANORMAL
============================================================

--- INFORMAÇÕES BÁSICAS ---
Nome: {nome}
Gênero: {'Masculino' if genero_real == 'M' else 'Feminino'}
Idade: {idade} anos
Altura: {altura} m
Nacionalidade: {nacionalidade_real.replace('_ocidental', ' Ocidental').replace('_oriental', ' Oriental').capitalize()}
Origem: {origem}
Patente: {patente} (NEX {nex_escolhido}%)

--- CLASSE E TRILHA ---
Classe: **{classe_escolhida}**
Trilha: **{trilha_escolhida}**

--- ATRIBUTOS ---
Força: {atributos['Força']}
Agilidade: {atributos['Agilidade']}
Intelecto: {atributos['Intelecto']}
Vigor: {atributos['Vigor']}
Presença: {atributos['Presença']}

--- PERÍCIAS ---
"""
    # Alinhamento das perícias
    pericias_ordenadas = sorted(pericias_personagem_valores.keys())
    # Calcula o maior nome de perícia para alinhamento da primeira coluna
    max_len_pericia = max(len(p) for p in pericias_ordenadas) if pericias_ordenadas else 0

    # Define o tamanho de cada "bloco" de perícia para garantir alinhamento
    # "Perícia: XX | Perícia: YY | Perícia: ZZ"
    # Considerando o "Nome da Perícia: " e o valor máximo (20)
    bloco_len = max_len_pericia + 5 # Ex: "Acrobacia: 20" tem ~15 caracteres. 15 + 5 = 20.

    for i in range(0, len(pericias_ordenadas), 3):
        linha_pericias = []
        for pericia in pericias_ordenadas[i:i+3]:
            valor_pericia = str(pericias_personagem_valores[pericia])
            # Formata cada item de perícia com preenchimento para alinhamento
            linha_pericias.append(f"{pericia}: {valor_pericia}".ljust(bloco_len))
        ficha_conteudo += " | ".join(linha_pericias) + "\n"

    ficha_conteudo += f"""
--- HABILIDADES DE TRILHA ---
{'Nenhuma habilidade de trilha para este NEX.' if not habilidades_personagem else '\n'.join(habilidades_personagem)}

--- ELEMENTO DE AFINIDADE ---
**{elemento_afinidade}**

--- RITUAIS (Ocultista) ---
{'Nenhum ritual.' if not rituais_personagem else '\n'.join(rituais_personagem)}

--- ITENS ---
{'\n'.join([f"- {item}" for item in itens_personagem])}

--- DESCRIÇÕES ---
"""
    # Descrições em 3 colunas
    # Ajusta o corte das descrições para um valor que permita melhor alinhamento
    # O valor 20 pode ser muito pequeno para algumas descrições. Vamos tentar 35.
    desc_f_linhas = [descricao_fisica[i:i+35] for i in range(0, len(descricao_fisica), 35)]
    desc_p_linhas = [descricao_personalidade[i:i+35] for i in range(0, len(descricao_personalidade), 35)]
    hist_b_linhas = [historia_breve[i:i+35] for i in range(0, len(historia_breve), 35)]

    max_lines = max(len(desc_f_linhas), len(desc_p_linhas), len(hist_b_linhas))

    ficha_conteudo += f"{'Descrição Física'.ljust(35)} | {'Personalidade'.ljust(35)} | {'História Breve'.ljust(35)}\n"
    ficha_conteudo += f"{'-'*35} | {'-'*35} | {'-'*35}\n"

    for i in range(max_lines):
        col1 = desc_f_linhas[i] if i < len(desc_f_linhas) else ""
        col2 = desc_p_linhas[i] if i < len(desc_p_linhas) else ""
        col3 = hist_b_linhas[i] if i < len(hist_b_linhas) else ""
        ficha_conteudo += f"{col1.ljust(35)} | {col2.ljust(35)} | {col3.ljust(35)}\n"


    ficha_conteudo += f"""
============================================================
"""
    return ficha_conteudo, nome

def salvar_ficha_em_txt(ficha_conteudo, nome_personagem_para_arquivo):
    """Salva a ficha gerada em um arquivo de texto com nome dinâmico."""
    nome_arquivo_formatado = "".join(c for c in nome_personagem_para_arquivo if c.isalnum() or c.isspace()).replace(" ", "_").lower()
    nome_arquivo = f"ficha_{nome_arquivo_formatado}.txt"
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(ficha_conteudo)
        print(f"\nFicha gerada e salva em '{nome_arquivo}' com sucesso!")
    except IOError as e:
        print(f"\nErro ao salvar a ficha: {e}")

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    while True:
        try:
            ficha_final, nome_personagem = gerar_ficha_ordem_paranormal_v6()
            clear_screen()
            print(ficha_final) # Exibe a ficha na tela
            salvar_ficha_em_txt(ficha_final, nome_personagem)
            
            continuar = input("\nGerar outra ficha? (s/n): ").lower()
            if continuar != 's':
                break
            clear_screen()
        except ValueError as e:
            print(f"\nErro: {e}. Por favor, tente novamente.")
            input("Pressione Enter para continuar...")
            clear_screen()
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e} na linha {e.__traceback__.tb_lineno}")
            import traceback
            traceback.print_exc() # Para debug: imprime o traceback completo
            input("Pressione Enter para continuar...")
            clear_screen()