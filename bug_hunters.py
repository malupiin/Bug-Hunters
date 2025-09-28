# BUG HUNTERS - RPG Interativo
# Desenvolvido por: Maria Luiza Pin, Anna Clara Zuany, Gustavo Gama
# Arquivo: bug_hunters.py

import random
import time
import os

class BugHuntersGame:
    def __init__(self):
        self.personagem = {
            "nome": "Kai",
            "COR": 0,  # Coragem
            "AST": 0,  # Astúcia
            "EMP": 0,  # Empatia
            "vida": 100,
            "vida_maxima": 100
        }
        self.escolhas_importantes = {}
        self.missoes_completas = 0
        
    def limpar_tela(self):
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def digitar_lento(self, texto, delay=0.03):
        """Simula digitação lenta para efeito dramático"""
        for char in texto:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def pausar(self, segundos=1):
        """Pausa a execução por alguns segundos"""
        time.sleep(segundos)

    def mostrar_historia_ditadura(self):
        """Mostra a história completa da ditadura dos insetos"""
        self.limpar_tela()
        
        print("🐞" * 70)
        self.digitar_lento("           HISTÓRIA DA GRANDE ECLOSÃO")
        print("🐞" * 70)
        
        self.digitar_lento("\nANO 2035 - O INÍCIO DO PESADELO")
        self.pausar(1)
        
        self.digitar_lento("\nA década de 2030 foi marcada por epidemias terríveis...")
        self.digitar_lento("Dengue, zika e chikungunya se alastravam sem controle.")
        self.digitar_lento("A população estava em desespero:")
        self.digitar_lento("as mortes eram incontáveis, nada conseguia parar a infestação.")
        self.digitar_lento("O governo brasileiro, desesperado, fez um acordo fatal.")
        self.digitar_lento("Uma parceria com a megacorporação internacional BioGen.")
        
        self.pausar(3)
        
        self.digitar_lento("\nSem saída, adquiriu O VENENOX-7")
        self.digitar_lento("Anunciado como 'solução definitiva', o pesticida Venenox-7 foi pulverizado em todas as cidades brasileiras.")
        self.digitar_lento("A mega corporação prometia acabar com os insetos em 30 dias.")
        self.digitar_lento("Ao fim desse período, a solução parecia ter entregue o que prometia.")
        self.digitar_lento("Os casos diminuíram, os principais transmissores pareciam desaparecer cada vez mais.")
        self.digitar_lento("O que ninguém esperava é que aquele era o começo do fim.")
        
        input("\n⏎ Pressione Enter para continuar...")
        self.limpar_tela()
        
        print("🧬" * 70)
        self.digitar_lento("               A GRANDE MUTAÇÃO")
        print("🧬" * 70)
        
        self.digitar_lento("\nANO 2038 - O INESPERADO ACONTECEU")
        self.pausar(1)
        
        self.digitar_lento("Já haviam se passado quase 8 anos")
        self.digitar_lento("\n Mas ao invés de morrer, os insetos começaram a mudar.")
        self.digitar_lento("O Venenox-7 não os matou... ele os transformou.")
        self.digitar_lento("Se infiltrou em seu DNA, acelerando sua evolução.")
        self.digitar_lento("Os insetos, que nos últimos anos pareciam não apresentar mais nenhum risco significante à vida humana")
        self.digitar_lento("Passaram por uma evolução acelerada:")
        self.digitar_lento("Baratas do tamanho de gatos...")
        self.digitar_lento("Besouros grandes como cachorros...")
        self.digitar_lento("E alguns, como as baratas-rainha, atingiram o tamanho de carros!")
        self.digitar_lento("Suas carapaças se tornaram mais resistentes que aço.")
        self.digitar_lento("Armas convencionais se tornaram praticamente inúteis.")
        self.digitar_lento("Suas assas eram tão grandes como hélices.")
        self.digitar_lento("Os ferrões, agora do tamanho de postes de ferro, desciam como lanças de guerra capazes de atravessar qualquer estrutura.")
        
        input("\n⏎ Pressione Enter para continuar...")
        self.limpar_tela()
        
        self.digitar_lento("Por um tempo, a humanidade tentou viver em harmonia com os novos membros.")
        self.digitar_lento("Não os atacavam e, assim, não eram atacados de volta.")
        self.digitar_lento("Até que...")

        self.pausar(3)

        print("👑" * 70)
        self.digitar_lento("               A ASCENSÃO DA RAINHA-MÃE")
        print("👑" * 70)
        
        self.digitar_lento("\nANO 2040 - A INTELIGÊNCIA COLETIVA")
        self.pausar(1)
        
        self.digitar_lento("\nAlém do tamanho, os insetos desenvolveram inteligência.")
        self.digitar_lento("As baratas desenvolveram uma consciência coletiva.")
        self.digitar_lento("Lideradas por uma barata gigante que chamaram de 'Rainha-Mãe'.")
        self.digitar_lento("Passaram a não aceitar serem submetidos às regras humanas")
        self.digitar_lento("A ascenção começou aos poucos, mas cominou em uma revolução, tão organizada como uma estratégia militar!")

        self.pausar(3)

        self.digitar_lento("Elas não atacaram como animais, mas como um exército organizado.")
        self.digitar_lento("Usaram táticas de enxame, cortando comunicações e suprimentos.")
        self.digitar_lento("As cidades caíram uma após a outra.")
        self.digitar_lento("Em 2042, a 'Colmeia Carioca' foi estabelecida: eles tomaram conta da cidade do Rio de Janeiro.")
        self.digitar_lento("O Palácio da República se tornou o centro do novo poder.")
        self.digitar_lento("Humanos foram reduzidos a escravos ou colaboracionistas.")
        
        input("\n⏎ Pressione Enter para continuar...")
        self.limpar_tela()
        
        print("🏙️" * 70)
        self.digitar_lento("               A VIDA NA COLMEIA CARIOCA")
        print("🏙️" * 70)
        
        self.digitar_lento("\nANO 2042 - O PRESENTE SOMBRIO")
        self.pausar(1)
        
        self.digitar_lento("Sobreviventes vivem em favelas vigiadas, como a 'Favela da Luta'.")
        self.digitar_lento("Luz elétrica é um luxo, comida é racionada.")
        self.digitar_lento("A palavra de ordem é obediência.")
        self.digitar_lento("O medo tomou conta de todos.")
        self.digitar_lento("O 'castigo' para quem não seguia as novas regras era cruel:")
        self.digitar_lento("Torturas, assassinatos, perseguições...")
        self.digitar_lento("Muitos desapareciam sem deixar rastros.")
        self.digitar_lento("O destino deles?")
        self.digitar_lento("Ninguém sabia.")
        self.digitar_lento("Os familiares daqueles que se revoltaram eram ainda mais vigiados")
        self.digitar_lento("e qualquer sinal de discordância e mudança levava a um fim trágico.")
        
        self.pausar(1)
        
        self.digitar_lento("Alguns humanos trocaram liberdade por migalhas de segurança")
        self.digitar_lento("trabalham para os insetos em troca de privilégios.")
        self.digitar_lento("Eles são vistos como traidores pela resistência.")
        self.digitar_lento("Toda comunidade humana os enxergam como cúmplices da crueldade que foi instaurada.")
        self.digitar_lento("Por isso, são chamados de Collaboracionistas")
        
        self.pausar(1)

        self.digitar_lento("Surgiram os temidos Formigueiros: campos de trabalho forçado onde dissidentes são enviados.")
        self.digitar_lento("Poucos sobrevivem mais de alguns meses.")
        self.digitar_lento("Outros eram realocados assim que chegavam lá...")
        
        self.pausar(1)
        
        self.digitar_lento("'Realocação' é o eufemismo para sentença de morte.")
        
        self.pausar(3)

        self.digitar_lento("Mas no meio da escuridão, um grupo estava em busca da luz...")
        self.digitar_lento("Conhecidos como Bug Hunters eram o último grupo organizado de resistência.")
        self.digitar_lento("Eles eram liderados por Sertão, um homem que nunca perdeu a esperança.")
        self.digitar_lento("Sertão acolheu crianças que perderam seus pais")
        self.digitar_lento("e pais que perderam seus filhos.")
        self.digitar_lento("Os ensinou tudo que precisavam saber e os proporcionou a melhor qualidade de vida que pode.")
        self.digitar_lento("E é aqui que sua história começa...")
        
        input("\n⏎ Pressione Enter para conhecer seu personagem...")
    
    def rolar_dado(self, faces=10):
        """Rola um dado virtual"""
        input("\n🎲 Pressione Enter para rolar o dado...")
        resultado = random.randint(1, faces)
        self.digitar_lento(f"Rolando dado D{faces}...", 0.1)
        self.digitar_lento(f"✅ Resultado: {resultado}")
        return resultado
    
    def teste_atributo(self, atributo, dificuldade=6):
        """Atributos do personagem"""
        nome_atributos = {"COR": "CORAGEM", "AST": "ASTÚCIA", "EMP": "EMPATIA"}
        
        print(f"Teste de {nome_atributos[atributo]} (Nível: {self.personagem[atributo]})")
        print(f"📊 Dificuldade: {dificuldade}")
        
        rolagem = self.rolar_dado()
        
        # Bônus baseado no nível do atributo
        bonus = self.personagem[atributo] // 2
        total = rolagem + bonus
        
        print(f"📈 Bônus do atributo: +{bonus}")
        print(f"💯 Total: {rolagem} + {bonus} = {total}")
        
        if total >= dificuldade:
            print("✅ Sucesso!")
            return True
        else:
            print("❌ Falha!")
            return False
    
    def mostrar_status(self):
        """Status atual do personagem"""
        print("\n" + "═" * 60)
        print("📊 STATUS DO CAÇADOR")
        print("═" * 60)
        print(f"👤 Nome: {self.personagem['nome']}")
        print(f"❤️  Vida: {self.personagem['vida']}/{self.personagem['vida_maxima']}")
        print(f"💪 CORAGEM: {self.personagem['COR']}")
        print(f"🧠 ASTÚCIA: {self.personagem['AST']}")
        print(f"💖 EMPATIA: {self.personagem['EMP']}")
        print(f"🎯 Missões completas: {self.missoes_completas}/6")
        print("═" * 60)
    
    def alterar_vida(self, quantidade):
        """Altera a vida do personagem"""
        self.personagem['vida'] += quantidade
        if self.personagem['vida'] > self.personagem['vida_maxima']:
            self.personagem['vida'] = self.personagem['vida_maxima']
        elif self.personagem['vida'] < 0:
            self.personagem['vida'] = 0
        
        if quantidade > 0:
            print(f"💚 +{quantidade} de vida!")
        elif quantidade < 0:
            print(f"💔 {quantidade} de vida!")
    
    def criar_personagem(self):
        """Criação do personagem principal"""
        self.limpar_tela()
        print("🐞" * 60)
        self.digitar_lento("           BUG HUNTERS - A REVOLUÇÃO DOS INSETOS")
        print("🐞" * 60)
        
        self.digitar_lento("\nSUA HISTÓRIA:")
        self.digitar_lento("Você é um adolescente de 18 anos, criado pelos Bug Hunters após seus pais")
        self.digitar_lento("desaparecerem em um protesto reprimido por besouros-soldados.")
        self.digitar_lento("Sertão, seu pai adotivo, te ensinou tudo que sabe.")
        self.digitar_lento("Ele te acolheu como filho e te fez desenvolver suas habilidades de caçador.")
        self.digitar_lento("No entanto, Sertão foi capturado após um descuido")
        self.digitar_lento("Agora, com seu sequestro, a resistência depende de você.")
        
        nome = input("\n🔮 Como você quer ser chamado? ").strip()
        if nome:
            self.personagem['nome'] = nome
        
        print(f"\nBem-vindo(a), {self.personagem['nome']}!")
        self.digitar_lento("Distribua 15 pontos entre seus atributos:")
        
        # Sistema de distribuição de pontos
        pontos = 15
        while pontos > 0:
            self.limpar_tela()
            self.mostrar_status()
            print(f"\n📦 Pontos disponíveis: {pontos}")
            
            print("\n🎯 Escolha um atributo para aumentar:")
            print("[1] 💪 CORAGEM - Para combate e resistência")
            print("[2] 🧠 ASTÚCIA - Para furtividade e percepção")
            print("[3] 💖 EMPATIA - Para persuasão e liderança")
            print("[4] ❤️  AUMENTAR VIDA MÁXIMA")
            print("[0] ✅ Finalizar distribuição")
            
            escolha = input("\nSua escolha: ").strip()
            
            if escolha == "1" and pontos > 0:
                self.personagem["COR"] += 1
                pontos -= 1
            elif escolha == "2" and pontos > 0:
                self.personagem["AST"] += 1
                pontos -= 1
            elif escolha == "3" and pontos > 0:
                self.personagem["EMP"] += 1
                pontos -= 1
            elif escolha == "4" and pontos > 0:
                self.personagem["vida_maxima"] += 5
                self.personagem["vida"] += 5
                pontos -= 1
            elif escolha == "0":
                break
            else:
                print("❌ Escolha inválida ou pontos insuficientes!")
                self.pausar(1)
        
        print("\nPersonagem criado com sucesso!")
        self.mostrar_status()
        
        # Mostrar dicas baseadas nos atributos escolhidos
        if self.personagem["COR"] >= 5:
            print("\n💡 DICA: Sua coragem será útil em combates diretos!")
        if self.personagem["AST"] >= 5:
            print("💡 DICA: Sua astúcia ajuda em furtividade e hackear sistemas!")
        if self.personagem["EMP"] >= 5:
            print("💡 DICA: Sua empatia convence NPCs e ajuda em escolhas morais!")
        
        input("\n⏎ Pressione Enter para começar sua jornada...")
    
    def missao_1(self):
        """Missão 1: O Sinal de Fumaça"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 1: O SINAL DE FUMAÇA")
        print("=" * 70)
        
        self.digitar_lento("Você estava na Base secreta dos bug Hunters, nos esgotos do Arpoador")
        self.digitar_lento("De repente o alarme soa!")
        self.digitar_lento("A base está sob ataque!")
        self.digitar_lento("Capitão Flecha e suas libélulas estão por toda parte!")
        self.digitar_lento("Sertão direcionou todos para o esconderijo, mas foi seguido por mosquinhas-fada - os menores insetos, que são usados como espiões.")
        self.digitar_lento("Sertão, após ser pego, se entrgou para salvar vocês. Enquanto era arrastado pelo ar gritou:")
        self.digitar_lento('💬 "Encontre Preá. Ele sabe onde me levarão..."')
        
        self.pausar(3)
        
        print("\n🚨 A BASE ESTÁ DESMORONANDO! ESCOLHA RAPIDAMENTE!")
        print("[1] Passar furtivamente pelas sombras (ASTÚCIA)")
        print("[2] Enfrentar as formigas-soldado que estão do lado de fora (CORAGEM)")
        print("[3] Procurar rota alternativa (ASTÚCIA)")
        print("[4] Correr desesperadamente (Sorte)")
        
        escolha = input("\n🎯 Sua ação: ").strip()
        
        if escolha == "1":
            if self.teste_atributo("AST", 6):
                self.digitar_lento("\n✅ Você se move como uma sombra! Insetos não te detectam.")
            else:
                self.digitar_lento("\n❌ Você tropeça e faz barulho! Formigas te atacam!")
                self.alterar_vida(-15)
        elif escolha == "2":
            if self.teste_atributo("COR", 7):
                self.digitar_lento("\n✅ Você luta bravamente! As formigas recuam!")
            else:
                self.digitar_lento("\n❌ Você é sobrepujado! Ferimentos graves!")
                self.alterar_vida(-20)
        elif escolha == "3":
            if self.teste_atributo("AST", 5):
                self.digitar_lento("\n✅ Você encontra um túnel de manutenção! Caminho seguro!")
            else:
                self.digitar_lento("\n❌ O túnel está bloqueado! Confronto inevitável!")
                if self.teste_atributo("COR", 6):
                    self.digitar_lento("✅ Você supera os obstáculos!")
                else:
                    self.alterar_vida(-10)
        else:  # Opção 4 ou qualquer outra
            dado = self.rolar_dado(6)
            if dado > 3:
                self.digitar_lento("\n🎲 A sorte está com você! Escapa ileso!")
            else:
                self.digitar_lento("\n💥 Você tropeça e se machuca!")
                self.alterar_vida(-12)
        
        self.missoes_completas += 1
        self.digitar_lento("\n🎉 MISSÃO 1 CONCLUÍDA! Você escapou da base!")
        input("\n⏎ Continuar...")

    def missao_2(self):
        """Missão 2: Os Arquivos Proibidos"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 2: OS ARQUIVOS PROIBIDOS")
        print("=" * 70)

        self.digitar_lento("Você está na Biblioteca Secreta de Preá, na Floresta da Tijuca.")
        self.digitar_lento("Preá é um cientista e antigo amigo de Sertão, ele era lider de um grupo de resistência.")
        self.digitar_lento("Todos os membros desse grupo foram mortos em uma manifestação.")
        self.digitar_lento("Como castigo por ter organizado o movimento, os insetos polparam apenas a vida de Preá")
        self.digitar_lento("que agora vive recluso...")
        self.digitar_lento("ele perdeu sua família e não vê mais sentido em continuar lutando.")
        self.digitar_lento("Ao chegar, você o contou o que aconteceu com Sertão e perguntou onde ele estava.")
        self.digitar_lento("👴 Preá: 'Sertão foi levado para o Formigueiro da Gávea!'")
        self.digitar_lento("'Um antigo condomínio de luxo transformado em campo de prisioneiros'")
        self.digitar_lento("'Precisamos da ajuda de Jango, o ex-caçador que agora trabalha para eles'")
        self.digitar_lento("'Ele é técnico de som no Estádio de Netuno'")
        self.digitar_lento("'Não ache que ele possa ser uma ameaça...'")
        self.digitar_lento("Você não pensa duas vezes e vai até Jango.")
        
        self.pausar(2)
        
        print("\nENCONTRO COM JANGO - COMO CONVENCÊ-LO?")
        print("[1] 💖 Lembrar dos velhos tempos (EMPATIA)")
        print("[2] ⚠️  Mostrar que a Colmeia vai traí-lo (ASTÚCIA)")
        print("[3] 🤝 Oferecer perdão pela traição (EMPATIA)")
        print("[4] 🔫 Ameaçar revelar seu paradeiro (CORAGEM)")
        
        escolha = input("\nSua abordagem: ").strip()
        
        sucesso = False
        
        if escolha == "1":
            if self.teste_atributo("EMP", 7):
                self.digitar_lento("\nJango se emociona com as lembranças! 'Eu era feliz com os Bug Hunters...'")
                self.digitar_lento("Ele concorda em ajudar, mas exige anonimato total.")
                sucesso = True
            else:
                self.digitar_lento("\n'O passado morreu!' Jango se fecha completamente.")
                self.digitar_lento("Ele ameaça chamar os guardas se você não for embora.")
        elif escolha == "2":
            if self.teste_atributo("AST", 6):
                self.digitar_lento("\nVocê mostra documentos que provam: a Colmeia elimina colaboracionistas 'inúteis'.")
                self.digitar_lento("Jango fica pálido: 'Eu sabia... eu sabia que isso aconteceria!'")
                sucesso = True
            else:
                self.digitar_lento("\nSua argumentação é fraca. Jango ri: 'Você acha que sou ingênuo?'")
        elif escolha == "3":
            if self.teste_atributo("EMP", 5):
                self.digitar_lento("\n'Todos merecem uma segunda chance,' você diz.")
                self.digitar_lento("Jango se comove: 'Talvez ainda haja esperança...'")
                sucesso = True
            else:
                self.digitar_lento("\n'Muito tarde para perdão!' Jango vira as costas.")
        else:
            if self.teste_atributo("COR", 6):
                self.digitar_lento("\n'Eu conheço seu esconderijo secreto,' você mente.")
                self.digitar_lento("Jango, acuado, aceita ajudar por medo.")
                sucesso = True
            else:
                self.digitar_lento("\nJango percebe seu blefe e fica furioso!")
                self.digitar_lento("Ele grita por ajuda! Você precisa fugir!")
                self.alterar_vida(-10)
        
        if sucesso:
            self.digitar_lento("\nJango fornece uniformes da equipe de som e crachás de acesso.")
            self.digitar_lento("'Há um baile de gala amanhã no estádio. É sua chance.'")
            self.escolhas_importantes["jango_convenceu"] = "diplomacia"
        else:
            self.digitar_lento("\nPlano B: Preá conhece um túnel de serviço esquecido.")
            self.digitar_lento("A infiltração será mais perigosa, mas possível.")
            self.escolhas_importantes["jango_convenceu"] = "força"
        
        self.missoes_completas += 1
        self.digitar_lento("\n🎉 MISSÃO 2 CONCLUÍDA!")
        input("\n⏎ Continuar...")

    def missao_3(self):
        """Missão 3: O Baile da Máscara"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 3: O BAILE DA MÁSCARA")
        print("=" * 70)
        
        self.digitar_lento("Por meio de Jango, você descobre que a elite dos Collaboralistas estarão reunidos hoje em um baile de máscaras...")

        if self.escolhas_importantes.get("jango_convenceu") == "diplomacia":
            self.digitar_lento("\nCom os uniformes de Jango, você e Luta entram facilmente.")
            self.digitar_lento("O baile é um espetáculo de luxo e decadência.")
            self.digitar_lento("Collaboracionistas dançam enquanto prisioneiros lutam na arena.")
        else:
            self.digitar_lento("\nUsando o túnel de serviço, você se infiltra com dificuldade.")
            self.digitar_lento("Você precisa encontrar uniformes para não chamar atenção.")
            self.digitar_lento("O risco de descoberta é constante")
        
        self.digitar_lento("\nSeu principal objetivo é encontrar informações sobre Sertão.")
        self.digitar_lento("O terminal de segurança tem os dados dos prisioneiros.")
        self.digitar_lento("Você precisa acessá-lo em segurança!")
        
        self.pausar(3)
        
        print("\nTERMINAL DE SEGURANÇA - COMO ACESSAR?")
        print("[1] 👨‍💼 Fingir ser técnico (ASTÚCIA)")
        print("[2] 💼 Distrair o guarda (EMPATIA)")
        print("[3] 🔌 Cortar a energia momentaneamente (ASTÚCIA)")
        print("[4] 💀 Neutralizar o guarda silenciosamente (CORAGEM)")
        
        escolha = input("\nSua estratégia: ").strip()
        
        if escolha == "1":
            if self.teste_atributo("AST", 6):
                self.digitar_lento("\n'Problema no sistema,' você diz com confiança.")
                self.digitar_lento("O guarda aceita sua explicação e te deixa acessar.")
            else:
                self.digitar_lento("\nO guarda desconfia: 'Não reconheço você...'")
                self.digitar_lento("Alarme! Você precisa correr!")
                if not self.teste_atributo("COR", 5):
                    self.alterar_vida(-15)
        elif escolha == "2":
            if self.teste_atributo("EMP", 7):
                self.digitar_lento("\nVocê inicia uma conversa animada sobre os 'jogos' da arena.")
                self.digitar_lento("O guarda se distrai completamente.")
                self.digitar_lento("Você acessa o terminal sem problemas.")
            else:
                self.digitar_lento("\nO guarda está desconfiado e alerta a segurança.")
                self.digitar_lento("Fuga imediata necessária!")
        elif escolha == "3":
            if self.teste_atributo("AST", 5):
                self.digitar_lento("\nVocê encontra o quadro de energia e causa um curto.")
                self.digitar_lento("30 segundos no escuro são suficientes.")
                self.digitar_lento("Usa uma lanterna para acessar rapidamente.")
            else:
                self.digitar_lento("\nVocê causa um blecaute geral! Caos total!")
                self.digitar_lento("Insetos-soldado com visão noturna são enviados!")
                self.alterar_vida(-10)
        else:
            if self.teste_atributo("COR", 6):
                self.digitar_lento("\nAproximação silenciosa... golpe preciso.")
                self.digitar_lento("Guarda neutralizado. Você esconde o corpo.")
                self.digitar_lento("Acesso livre ao terminal.")
            else:
                self.digitar_lento("\nA luta é barulhenta! Guardas são alertados!")
                self.digitar_lento("Você precisa lutar para escapar!")
                self.alterar_vida(-20)
        
        # Descoberta importante
        self.digitar_lento("\nApós acessar o terminal, vocÊ finalmente descobre a verdade:")
        self.digitar_lento("Sertão NÃO está no Formigueiro da Gávea!")
        self.digitar_lento("Ele é prisioneiro de alto valor no laboratório do Doutor Ustra!")
        self.digitar_lento("Ele foi levado para o Palácio da República, ala de interrogatórios.")

        self.pausar(1)
        
        self.digitar_lento("\nDe repente, você ouve um alerta de segurança")
        self.digitar_lento("Sua invasão foi detectada!")
        self.digitar_lento("Insetos estão vindo de todos os lados para te encurralar.")
        
        if self.teste_atributo("AST", 5):
            self.digitar_lento("\nVocê escapa pelos dutos de ventilação!")
            self.digitar_lento("Encontra Luta no ponto de encontro combinado.")
        else:
            self.digitar_lento("\nVocê é encurralado! Precisa lutar para escapar!")
            if self.teste_atributo("COR", 6):
                self.digitar_lento("Luta te resgata no último momento!")
                self.alterar_vida(-10)
            else:
                self.digitar_lento("Ferido gravemente, mas consegue escapar!")
                self.alterar_vida(-25)
        
        self.missoes_completas += 1
        self.digitar_lento("\n🎉 MISSÃO 3 CONCLUÍDA! Agora sabemos a verdade sobre o paradeiro de Sertão!")
        input("\n⏎ Continuar...")

    def missao_4(self):
        """Missão 4: A Picada da Verdade"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 4: A PICADA DA VERDADE")
        print("=" * 70)
        
        self.digitar_lento("\nApós uma jornada cansativa, vocÊ chegou aos esgotos e becos do Centro do Rio")
        self.digitar_lento("Você está recebendo as instruções de Marighela para executar o plano!")
        self.digitar_lento("⚔️  Marighela: 'Vou criar uma distração no Formigueiro da Gávea'")
        self.digitar_lento("Enquanto isso, vocÊ se infiltra no Palácio.")
        self.digitar_lento("'Cuidado com o Doutor Ustra... seu ferrão causa dor insuportável'")
        
        self.pausar(3)
        
        self.digitar_lento("\nNOITE DE OPERAÇÃO")
        self.digitar_lento("A cidade está estranhamente silenciosa.")
        self.digitar_lento("Parece que todos estão no baile.")
        self.digitar_lento("Sua equipe é composta por você, Luta e dois recrutas novatos.")
        self.digitar_lento("O caminho até o Palácio é uma rede de esgotos e ruínas.")
        self.digitar_lento("Ainda há uma patrulha de insetos...")
        self.digitar_lento("Cigarras-soldado fazem a ronda noturna.")
        self.digitar_lento("Elas têm audição aguçada, mas pouca experiência.")
        self.digitar_lento("TOME CUIDADO!")
        self.digitar_lento("De repente, uma jovem cigarra parece perdida e assustada.")
        self.digitar_lento("Ela está sozinha, separada de seu pelotão.")
        self.digitar_lento("💭 'É só uma criança...' pensa Luta.")
        
        print("\nDECISÃO MORAL - O QUE FAZER?")
        print("[1] ⚔️  Eliminar a ameaça rapidamente (CORAGEM)")
        print("[2] 💖 Mostrar compaixão (EMPATIA)")
        print("[3] 🎭 Enganar e distrair (ASTÚCIA)")
        print("[4] 🚫 Contornar e evitar conflito (ASTÚCIA)")
        
        escolha = input("\nSua escolha: ").strip()
        
        if escolha == "1":
            self.digitar_lento("\nVocê ataca antes que ela possa soar o alarme.")
            self.digitar_lento("A cigarra não tem chance contra sua experiência.")
            self.digitar_lento("Luta parece desconfortável: 'Ela era apenas uma criança...'")
            self.escolhas_importantes["cigarra"] = "morto"
            
        elif escolha == "2":
            if self.teste_atributo("EMP", 6):
                self.digitar_lento("\nVocê se aproxima calmamente: 'Não vamos te machucar.'")
                self.digitar_lento("A cigarra treme: 'Eu... eu só quero sobreviver.'")
                self.digitar_lento("Você a convence a fugir e abandonar a Colmeia.")
                self.digitar_lento("🙏'Obrigada...' ela sussurra antes de desaparecer.")
                self.escolhas_importantes["cigarra"] = "poupado"
            else:
                self.digitar_lento("\nSua abordagem assusta a cigarra!")
                self.digitar_lento("Ela solta um grito agudo que atrai outras patrulhas!")
                self.digitar_lento("Confronto inevitável!")
                if self.teste_atributo("COR", 5):
                    self.digitar_lento("✅ Você elimina a ameaça, mas o barulho alerta outros.")
                    self.escolhas_importantes["cigarra"] = "morto"
                else:
                    self.digitar_lento("❌ A cigarra escapa e soa o alarme completo!")
                    self.alterar_vida(-15)
                    self.escolhas_importantes["cigarra"] = "alerta"
                    
        elif escolha == "3":
            if self.teste_atributo("AST", 5):
                self.digitar_lento("\n'Sua unidade está te procurando lá atrás!' você mente.")
                self.digitar_lento("A cigarra acredita e corre na direção oposta.")
                self.digitar_lento("✅ Você passa despercebido.")
                self.escolhas_importantes["cigarra"] = "enganado"
            else:
                self.digitar_lento("\nA cigarra desconfia: 'Você está mentindo!'")
                self.digitar_lento("Ela ataca primeiro!")
                self.alterar_vida(-8)
                self.escolhas_importantes["cigarra"] = "morto"
                
        else:
            if self.teste_atributo("AST", 4):
                self.digitar_lento("\nVocê encontra uma rota alternativa pelo telhado.")
                self.digitar_lento("✅ Evita completamente o confronto.")
                self.escolhas_importantes["cigarra"] = "evitado"
            else:
                self.digitar_lento("\nA rota alternativa está bloqueada!")
                self.digitar_lento("Voltando... a cigarra ainda está lá.")
                if self.teste_atributo("EMP", 5):
                    self.digitar_lento("Você convence a cigarra a se afastar.")
                    self.escolhas_importantes["cigarra"] = "poupado"
                else:
                    self.digitar_lento("Confronto inevitável.")
                    self.alterar_vida(-5)
                    self.escolhas_importantes["cigarra"] = "morto"
        
        # Consequência imediata da escolha
        if self.escolhas_importantes.get("cigarra") in ["morto", "alerta"]:
            self.digitar_lento("\nALERTA GERAL!")
            self.digitar_lento("Insetos-soldado reforçam a segurança do Palácio.")
            self.digitar_lento("A infiltração se tornou muito mais perigosa.")
        else:
            self.digitar_lento("\nPATRULHA EVITADA")
            self.digitar_lento("A noite continua silenciosa.")
            self.digitar_lento("Caminho livre para o Palácio.")
        
        self.missoes_completas += 1
        self.digitar_lento("\nMISSÃO 4 CONCLUÍDA! Decisão moral registrada.")
        input("\n⏎ Continuar...")

    def missao_5(self):
        """Missão 5: O Salão do Trono"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 5: O SALÃO DO TRONO")
        print("=" * 70)
        
        self.digitar_lento("\nVocê finalmente está dentro do Palácio da República.")
        self.digitar_lento("O ar vibra com o zumbido de milhares de insetos.")
        self.digitar_lento("Teias cobrem os lustres de cristal.")
        self.digitar_lento("Ossos de colaboracionistas 'inúteis' empilhados nos cantos.")
        self.digitar_lento("Mais do qe=ue nunca é importante manter o foco e seguir o plano:")
        self.digitar_lento("Luta enfrentará o Capitão Flecha no telhado como distração.")
        self.digitar_lento("Você encontrará o laboratório do Doutor Ustra.")
        self.digitar_lento("Lembre-se: seu principal objetivo é resgatar Sertão.")
        
        self.pausar(3)
        
        self.digitar_lento("\nLuta atraiu o Capitão Flecha para o telhado e tudo corre bem.")
        self.digitar_lento("Você finalmente encontrou o Capitão Ustra.")
        self.digitar_lento("O laboratório é uma câmara de horrores.")
        self.digitar_lento("Vidros com órgãos humanos em formol.")
        self.digitar_lento("Sertão está preso em uma teia, consciente mas ferido.")
        
        self.digitar_lento('\n🐝 USTRA: Ah, o pequeno rebelde finalmente chegou!')
        self.digitar_lento('Sabe, a mutação não foi acidente. Foi planejada!')
        self.digitar_lento('A Rainha-Mãe sabotou o Venenox-7 desde o início!"')
        self.digitar_lento('Humanidade é apenas... gado de trabalho.')
        
        print("\nCOMBATE CONTRA O DOUTOR USTRA - ESCOLHA O QUE FAZER")
        print("[1] 🏗️  Usar o ambiente laboratorial (ASTÚCIA)")
        print("[2] ⚔️  Ataque frontal direto (CORAGEM)")
        print("[3] 💡 Explorar suas inseguranças (EMPATIA)")
        print("[4] 🔥 Fogo - arma universal (Sorte)")
        
        escolha = input("\nSua tática: ").strip()
        
        vitoria = False
        dano_extra = 0
        
        if escolha == "1":
            if self.teste_atributo("AST", 7):
                self.digitar_lento("\nVocê derruba estantes com venenos experimentais!")
                self.digitar_lento("Ustra é atingido por múltiplas toxinas!")
                self.digitar_lento("Ele fica confuso e desorientado!")
                vitoria = True
            else:
                self.digitar_lento("\n❌ Ustra desvia rapidamente! Seu plano falha!")
                self.digitar_lento("Ele contra-ataca com neurotoxina!")
                dano_extra = -20
                
        elif escolha == "2":
            if self.teste_atributo("COR", 8):
                self.digitar_lento("\nATAQUE SURPRESA! Você é mais rápido que parece!")
                self.digitar_lento("Sua lâmina atinge o ponto fraco da carapaça!")
                self.digitar_lento("Ustra recua, gravemente ferido!")
                vitoria = True
            else:
                self.digitar_lento("\nUstra é incrivelmente rápido!")
                self.digitar_lento("Ele te acerta com uma perna afiada!")
                dano_extra = -25
                
        elif escolha == "3":
            if self.teste_atributo("EMP", 9):
                self.digitar_lento('\n"A Rainha-Mãe vai descartar você também, Ustra!"')
                self.digitar_lento('"Ela já substituiu outros cientistas!"')
                self.digitar_lento('Ustra hesita - você tocou em seu medo secreto!')
                self.digitar_lento('Distraído, ele comete um erro fatal!')
                vitoria = True
            else:
                self.digitar_lento('\nUstra ri: "Psicologia barata, humano!"')
                self.digitar_lento('"Deixe-me mostrar-lhe verdadeira dor!"')
                dano_extra = -30
                
        else:
            dado = self.rolar_dado(10)
            if dado > 8:
                self.digitar_lento("\nVocê encontra um lança-chamas abandonado!")
                self.digitar_lento("Insetos temem fogo acima de tudo!")
                self.digitar_lento("Ustra recua, aterrorizado!")
                vitoria = True
            else:
                self.digitar_lento("\nO equipamento está enferrujado e falha!")
                self.digitar_lento("Ustra fica furioso com sua ousadia!")
                dano_extra = -35
        
        if vitoria:
            self.digitar_lento("\nVOCÊ DERROTA USTRA!")
            self.digitar_lento("Liberta Sertão das teias.")
            self.digitar_lento("'Estava com saudades, filho,' ele sorri fraco.")
        else:
            self.alterar_vida(dano_extra)
            self.digitar_lento("\nUstra TE FERE GRAVEMENTE!")
            self.digitar_lento("Sertão, enfraquecido, intervém no último segundo!")
            self.digitar_lento("'CORRA, KAI!' ele grita, segurando Ustra.")
            self.digitar_lento("Você ouve uma explosão... Sertão se sacrifica!")
        
        self.digitar_lento("\nALERTA MÁXIMO!")
        self.digitar_lento("A Rainha-Mãe sente a morte de Ustra!")
        self.digitar_lento("Todas as saídas são seladas magneticamente!")
        self.digitar_lento("'Ninguém escapa da Colmeia,' ecoa uma voz na sua mente.")
        
        self.missoes_completas += 1
        self.digitar_lento("\nMISSÃO 5 CONCLUÍDA! Mas estamos presos!")
        input("\n⏎ Continuar...")

    def missao_6(self):
        """Missão 6: A Rainha-Mãe"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 6: A RAINHA-MÃE")
        print("=" * 70)
        
        self.digitar_lento("\nAgora vocês estão no santuário da Rainha-Mãe:")
        self.digitar_lento("uma câmara gigante cheia de ovos luminosos.")
        self.digitar_lento("Larvas do tamanho de humanos se contorcem em casulos.")
        self.digitar_lento("A Rainha-Mãe é um pesadelo vivo - uma barata do tamanho de um ônibus.")
        
        self.digitar_lento('\nRAINHA-MÃE: "Finalmente nos conhecemos."')
        self.digitar_lento('Sua voz ecoa diretamente na sua mente.')
        self.digitar_lento('"Seus pais... eles foram reciclados, não mortos."')
        self.digitar_lento('"Seu DNA agora faz parte da minha prole."')
        self.digitar_lento('"Junte-se a nós. É inevitável."')
        
        self.pausar(3)
        
        print("\n BATALHA MENTAL FINAL")
        self.digitar_lento("Esta não é uma luta física, mas sim pela sua alma.")
        self.digitar_lento("A Rainha-Mãe ataca suas memórias e emoções mais profundas.")
        
        print("\n🎯 COMO RESISTIR À INFLUÊNCIA?")
        print("[1] 💭 Lembrar dos ensinamentos de Sertão (EMPATIA)")
        print("[2] 🌟 Focar na esperança do povo oprimido (EMPATIA)")
        print("[3] 🔥 Usar a raiva como escudo (CORAGEM)")
        print("[4] 🧠 Raciocínio lógico contra a loucura (ASTÚCIA)")
        
        escolha = input("\nSua defesa: ").strip()
        
        resistencia = False
        bonus_cigarra = 0
        
        # Bônus se poupou a cigarra
        if self.escolhas_importantes.get("cigarra") == "poupado":
            bonus_cigarra = 2
            self.digitar_lento("\nLEMBRANÇA INESPERADA: A cigarra que você poupou!")
            self.digitar_lento("Seu ato de compaixão fortalece seu espírito!")
        
        if escolha in ["1", "2"]:
            if self.teste_atributo("EMP", 8 - bonus_cigarra):
                self.digitar_lento("\nSUA EMPATIA É SUA FORÇA!")
                self.digitar_lento("As memórias de bondade quebram o controle mental!")
                self.digitar_lento("A Rainha-Mãe recua, ferida por emoções que não compreende!")
                resistencia = True
            else:
                self.digitar_lento("\nQuase cedendo... as vozes são tentadoras...")
                self.digitar_lento("'LUTA!' você ouve Sertão gritar de longe.")
                self.digitar_lento("O grito te traz de volta à realidade!")
                
        elif escolha == "3":
            if self.teste_atributo("COR", 7 - bonus_cigarra):
                self.digitar_lento("\nSUA RAIVA PURIFICA!")
                self.digitar_lento("Você canaliza toda sua dor em um grito de desafio!")
                self.digitar_lento("A Rainha-Mãe se contorce - ela não esperava tanta força!")
                resistencia = True
            else:
                self.digitar_lento("\nA raiva quase te consome...")
                self.digitar_lento("No último segundo, você encontra equilíbrio.")
                
        else:
            if self.teste_atributo("AST", 6 - bonus_cigarra):
                self.digitar_lento("\nA LÓGICA VENCE A LOUCURA!")
                self.digitar_lento("Você encontra falhas na matriz mental da Rainha!")
                self.digitar_lento("'IMPOSSÍVEL!' ela grita, seu controle se desfaz!")
                resistencia = True
            else:
                self.digitar_lento("\nA mente alienígena é avassaladora...")
                self.digitar_lento("Mas você encontra uma brecha mínima para escapar!")
        
        # Resolução final
        self.digitar_lento("\nSERTÃO AGE!")
        self.digitar_lento("Explosivos plantados nos ovos da Rainha!")
        self.digitar_lento("'ISSO É PELO BRASIL!' ele grita.")
        
        if resistencia:
            self.digitar_lento("\nVOCÊ DISTRAIU A RAINHA-MÃE O SUFICIENTE!")
            self.digitar_lento("Os explosivos detonam perfeitamente!")
            self.digitar_lento("A câmara de ovos é destruída!")
            self.digitar_lento("A Rainha-Mãe grita em agonia - é o fim!")
        else:
            self.digitar_lento("\nA EXPLOSÃO É CAÓTICA!")
            self.digitar_lento("Você é atingido por detritos!")
            self.alterar_vida(-30)
            self.digitar_lento("A Rainha-Mãe está ferida, mas não morta!")
        
        self.digitar_lento("\nO PALÁCIO DESMORONA!")
        self.digitar_lento("Sistema de autodestruição ativado!")
        self.digitar_lento("FUGA DESESPERADA!")
        
        self.missoes_completas += 1
        input("\n⏎ Continuar para o epílogo...")

    def epilogo(self):
        """Epílogo do jogo"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("EPÍLOGO: O AMANHECER INCERTO")
        print("=" * 70)
        
        self.digitar_lento("\n48 HORAS DEPOIS...")
        self.digitar_lento("Vocês estão escondidos na Favela da Luta")
        self.digitar_lento("Muitos caíram, incluindo Sertão")
        self.digitar_lento("Mas a Rainha-Mãe foi destruída!")
        
        self.pausar(3)
        
        # Consequências das escolhas
        if self.escolhas_importantes.get("cigarra") == "poupado":
            self.digitar_lento("\nSURPRESA: A cigarra que você poupou aparece!")
            self.digitar_lento("Ela traz um grupo de insetos dissidentes!")
            self.digitar_lento("'Nós também queremos liberdade,' ela diz.")
            self.digitar_lento("PELA PRIMEIRA VEZ: Humanos e insetos lutam juntos!")
        else:
            self.digitar_lento("\nA COLMEIA ESTÁ FRACA, MAS NÃO MORTA")
            self.digitar_lento("General Castelo assume o controle")
            self.digitar_lento("A repressão piora - caçam sobreviventes")
            self.digitar_lento("A resistência será longa e difícil...")
        
        self.digitar_lento(f"\n{self.personagem['nome'].upper()} É AGORA UM LÍDER")
        self.digitar_lento("Sua história corre os guetos escondidos")
                            
        # Resultado final baseado na vida
        self.mostrar_status()
        
        if self.personagem["vida"] >= 70:
            self.digitar_lento("\nVOCÊ É UM SÍMBOLO DE ESPERANÇA")
            self.digitar_lento("Liderará a resistência com força total!")
            self.digitar_lento("O Brasil renascerá das cinzas!")
            
        elif self.personagem["vida"] >= 30:
            self.digitar_lento("\nFERIDO, MAS NÃO DERROTADO")
            self.digitar_lento("Precisa se recuperar, mas continuará lutando")
            self.digitar_lento("A guerra pela liberdade continua!")
            
        else:
            self.digitar_lento("\nGRAVEMENTE FERIDO - MAS VIVO")
            self.digitar_lento("Sua recuperação será longa")
            self.digitar_lento("Mas sua luta inspirará gerações!")
        
        self.digitar_lento("\nVOCÊ OLHA PARA O HORIZONTE")
        self.digitar_lento("A cidade fumega, mas o sol nasce")
        self.digitar_lento("O futuro é incerto, mas a esperança renasceu")
        self.digitar_lento("BUG HUNTERS - A LUTA CONTINUA!")
        
        self.pausar(3)
        
        print("\n" + "=" * 70)
        self.digitar_lento("🎭 FIM DO JOGO - OBRIGADO POR JOGAR!")
        print("=" * 70)
        
        # Estatísticas finais
        print(f"\n📊 ESTATÍSTICAS FINAIS:")
        print(f"👤 Nome: {self.personagem['nome']}")
        print(f"🎯 Missões completas: {self.missoes_completas}/6")
        print(f"❤️  Vida final: {self.personagem['vida']}/{self.personagem['vida_maxima']}")
        print(f"💪 Coragem: {self.personagem['COR']}")
        print(f"🧠 Astúcia: {self.personagem['AST']}")
        print(f"💖 Empatia: {self.personagem['EMP']}")
        
        if self.escolhas_importantes.get("cigarra") == "poupado":
            print("🤝 Aliados insetos: SIM - Revolução conjunta!")
        else:
            print("💔 Aliados insetos: NÃO - Resistência humana apenas")
        
        print("\n" + "=" * 70)