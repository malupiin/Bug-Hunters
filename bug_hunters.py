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
    
    def rolar_dado(self, faces=10):
        """Rola um dado virtual"""
        input("\n🎲 Pressione Enter para rolar o dado...")
        resultado = random.randint(1, faces)
        self.digitar_lento(f"⚡ Rolando dado D{faces}...", 0.1)
        self.digitar_lento(f"✅ Resultado: {resultado}")
        return resultado
    
    def teste_atributo(self, atributo, dificuldade=6):
        """Faz um teste baseado nos atributos do personagem"""
        nome_atributos = {"COR": "CORAGEM", "AST": "ASTÚCIA", "EMP": "EMPATIA"}
        
        print(f"\n🎯 Teste de {nome_atributos[atributo]} (Nível: {self.personagem[atributo]})")
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
        """Mostra o status atual do personagem"""
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
        
        self.digitar_lento("\n📅 ANO 2045 - COLMEIA CARIOCA")
        self.digitar_lento("A Grande Eclosão transformou o Rio de Janeiro em um pesadelo.")
        self.digitar_lento("Insetos mutantes governam a cidade, liderados pela Rainha-Mãe.")
        self.digitar_lento("Você é Kai, último esperança da resistência humana.")
        
        nome = input("\n🔮 Como você quer ser chamado? ").strip()
        if nome:
            self.personagem['nome'] = nome
        
        print(f"\n🌟 Bem-vindo(a), {self.personagem['nome']}!")
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
        
        print("\n🎉 Personagem criado com sucesso!")
        self.mostrar_status()
        input("\n⏎ Pressione Enter para começar sua jornada...")
    
    def missao_1(self):
        """Missão 1: O Sinal de Fumaça"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 1: O SINAL DE FUMACA")
        print("=" * 70)
        
        self.digitar_lento("\n📍 Local: Base secreta dos Bug Hunters, esgotos do Arpoador")
        self.digitar_lento("💥 O alarme soa! A base está sob ataque!")
        self.digitar_lento("🐦 Capitão Flecha e suas libélulas estão por toda parte!")
        self.digitar_lento("👴 Sertão se entrega para salvar vocês...")
        self.digitar_lento('💬 "Encontre Preá. Ele sabe onde me levarão..."')
        
        self.pausar(2)
        
        print("\n🚨 A BASE ESTÁ DESMORONANDO! ESCOLHA RAPIDAMENTE!")
        print("[1] 🦶 Passar furtivamente pelas sombras (ASTÚCIA)")
        print("[2] ⚔️  Enfrentar as formigas-soldado (CORAGEM)")
        print("[3] 🔍 Procurar rota alternativa (ASTÚCIA)")
        print("[4] 💨 Correr desesperadamente (Sorte)")
        
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
        
        self.digitar_lento("\n📍 Local: Biblioteca secreta de Preá, Floresta da Tijuca")
        self.digitar_lento("👴 Preá revela segredos chocantes...")
        self.digitar_lento("🏢 Sertão foi levado para o Formigueiro da Gávea!")
        self.digitar_lento("🎭 Precisamos da ajuda de Jango, o traidor...")
        self.digitar_lento("🏟️  Ele trabalha no Estádio de Netuno (Maracanã)")
        
        self.pausar(2)
        
        print("\n🎭 ENCONTRO COM JANGO - COMO CONVENCÊ-LO?")
        print("[1] 💖 Apelar para suas memórias (EMPATIA)")
        print("[2] 📜 Chantagear com segredos (ASTÚCIA)")
        print("[3] 🤝 Oferecer proteção (EMPATIA)")
        print("[4] 💰 Subornar (Sorte)")
        
        escolha = input("\n🎯 Sua abordagem: ").strip()
        
        sucesso = False
        
        if escolha == "1":
            if self.teste_atributo("EMP", 7):
                self.digitar_lento("\n💧 Jango se emociona! Ele concorda em ajudar!")
                sucesso = True
            else:
                self.digitar_lento("\n❌ Jango se fecha! Recusa ajudar!")
        elif escolha == "2":
            if self.teste_atributo("AST", 6):
                self.digitar_lento("\n⚖️  Chantagem funciona! Jango cede!")
                sucesso = True
            else:
                self.digitar_lento("\n💥 Jango fica furioso! Ameaça entregar você!")
        elif escolha == "3":
            if self.teste_atributo("EMP", 5):
                self.digitar_lento("\n🤝 Jango aceita sua proposta!")
                sucesso = True
            else:
                self.digitar_lento("\n❌ Jango não confia em você!")
        else:
            dado = self.rolar_dado(10)
            if dado > 7:
                self.digitar_lento("\n🎲 Jango aceita o suborno! Sucesso!")
                sucesso = True
            else:
                self.digitar_lento("\n💥 Jango se ofende! Negócio fracassa!")
        
        if sucesso:
            self.digitar_lento("\n🔑 Jango fornece uniformes e documentos falsos!")
            self.escolhas_importantes["jango_convenceu"] = True
        else:
            self.digitar_lento("\n⚠️  Você precisará encontrar outra maneira de entrar...")
            self.escolhas_importantes["jango_convenceu"] = False
        
        self.missoes_completas += 1
        self.digitar_lento("\n🎉 MISSÃO 2 CONCLUÍDA! Rumo ao Estádio de Netuno!")
        input("\n⏎ Continuar...")
    
    def missao_3(self):
        """Missão 3: O Baile da Máscara"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 3: O BAILE DA MÁSCARA")
        print("=" * 70)
        
        self.digitar_lento("\n📍 Local: Estádio de Netuno (Maracanã)")
        self.digitar_lento("🎭 Baile da elite Collaboracionista")
        self.digitar_lento("👥 Você e Luta se infiltram disfarçados")
        self.digitar_lento("💡 Descoberta chocante: Sertão não está no Formigueiro!")
        self.digitar_lento("🔬 Ele está com o terrível Doutor Ustra no Palácio!")
        
        self.pausar(2)
        
        print("\n🕵️ COMO OBTER INFORMAÇÕES?")
        print("[1] 🚶 Circular discretamente (ASTÚCIA)")
        print("[2] 🎭 Fingir ser da elite (EMPATIA)")
        print("[3] 💻 Hackear os sistemas (ASTÚCIA)")
        print("[4] 🎯 Observar de longe (Sorte)")
        
        escolha = input("\n🎯 Sua estratégia: ").strip()
        
        if escolha == "1":
            if self.teste_atributo("AST", 6):
                self.digitar_lento("\n✅ Você ouve conversas importantes sem ser notado!")
            else:
                self.digitar_lento("\n❌ Um guarda desconfia! Hora de fugir!")
                if not self.teste_atributo("COR", 5):
                    self.alterar_vida(-10)
        elif escolha == "2":
            if self.teste_atributo("EMP", 7):
                self.digitar_lento("\n✅ Você convence a todos! Obtém informações valiosas!")
            else:
                self.digitar_lento("\n❌ Alguém reconhece Luta! Confusão generalizada!")
        elif escolha == "3":
            if self.teste_atributo("AST", 8):
                self.digitar_lento("\n💻 Hackeamento bem-sucedido! Documentos secretos!")
            else:
                self.digitar_lento("\n🚨 Alarme soa! Insetos-soldado são acionados!")
                self.alterar_vida(-15)
        else:
            dado = self.rolar_dado(10)
            if dado > 5:
                self.digitar_lento("\n🎲 Você encontra documentos abandonados! Sorte!")
            else:
                self.digitar_lento("\n💥 Você é descoberto! Fugir é a única opção!")
                self.alterar_vida(-8)
        
        self.missoes_completas += 1
        self.digitar_lento("\n🎉 MISSÃO 3 CONCLUÍDA! Agora sabemos onde está Sertão!")
        input("\n⏎ Continuar...")
    
    def missao_4(self):
        """Missão 4: A Picada da Verdade"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 4: A PICADA DA VERDADE")
        print("=" * 70)
        
        self.digitar_lento("\n📍 Local: Esgotos do Centro do Rio")
        self.digitar_lento("⚔️  Marighela cria distração no Formigueiro")
        self.digitar_lento("🚀 Seu grupo avança em direção ao Palácio")
        self.digitar_lento("🐜 Encontro com uma cigarra-soldado jovem...")
        self.digitar_lento("💭 Ela parece assustada e inexperiente")
        
        self.pausar(2)
        
        print("\n🤔 DECISÃO MORAL - O QUE FAZER COM A CIGARRA?")
        print("[1] ⚔️  Atacar rapidamente (CORAGEM)")
        print("[2] 💖 Mostrar misericórdia (EMPATIA)")
        print("[3] 🎭 Distrair e passar (ASTÚCIA)")
        print("[4] 🚫 Ignorar e contornar (Sorte)")
        
        escolha = input("\n🎯 Sua escolha: ").strip()
        
        if escolha == "1":
            self.digitar_lento("\n⚔️ Você elimina a ameaça rapidamente.")
            self.escolhas_importantes["cigarra"] = "morto"
        elif escolha == "2":
            if self.teste_atributo("EMP", 6):
                self.digitar_lento("\n💖 Você poupa a cigarra. Ela foge agradecida.")
                self.escolhas_importantes["cigarra"] = "poupado"
            else:
                self.digitar_lento("\n⚠️ A cigarra soa o alarme! Você a neutraliza.")
                self.escolhas_importantes["cigarra"] = "morto"
        elif escolha == "3":
            if self.teste_atributo("AST", 5):
                self.digitar_lento("\n🎭 Distração perfeita! Você passa despercebido.")
                self.escolhas_importantes["cigarra"] = "poupado"
            else:
                self.digitar_lento("\n❌ A distração falha! Confronto inevitável.")
                if self.teste_atributo("COR", 4):
                    self.digitar_lento("✅ Você vence o confronto!")
                    self.escolhas_importantes["cigarra"] = "morto"
                else:
                    self.alterar_vida(-8)
                    self.escolhas_importantes["cigarra"] = "morto"
        else:
            dado = self.rolar_dado(10)
            if dado > 6:
                self.digitar_lento("\n🎲 A cigarra não te vê! Você passa em silêncio.")
                self.escolhas_importantes["cigarra"] = "poupado"
            else:
                self.digitar_lento("\n💥 Encontro hostil! Você luta pela sobrevivência.")
                self.alterar_vida(-5)
                self.escolhas_importantes["cigarra"] = "morto"
        
        self.missoes_completas += 1
        self.digitar_lento("\n🎉 MISSÃO 4 CONCLUÍDA! Decisão moral registrada.")
        input("\n⏎ Continuar...")
    
    def missao_5(self):
        """Missão 5: O Salão do Trono"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 5: O SALÃO DO TRONO")
        print("=" * 70)
        
        self.digitar_lento("\n📍 Local: Palácio da República")
        self.digitar_lento("⚔️  Luta enfrenta Capitão Flecha no telhado")
        self.digitar_lento("🔬 Você encontra o laboratório do Doutor Ustra")
        self.digitar_lento("👴 Sertão está preso em uma teia!")
        self.digitar_lento("💀 Ustra revela a verdade sobre a mutação...")
        
        self.pausar(2)
        
        print("\n🐝 ENFRENTAMENTO COM O DOUTOR USTRA!")
        print("[1] 🏗️  Usar o ambiente a seu favor (ASTÚCIA)")
        print("[2] ⚔️  Ataque frontal (CORAGEM)")
        print("[3] 💡 Explorar fraquezas (EMPATIA)")
        print("[4] 💣 Usar explosivos (Sorte)")
        
        escolha = input("\n🎯 Sua tática: ").strip()
        
        vitoria = False
        
        if escolha == "1":
            if self.teste_atributo("AST", 7):
                self.digitar_lento("\n✅ Você derruba colmeias sobre Ustra! Ele fica preso!")
                vitoria = True
            else:
                self.digitar_lento("\n❌ Ustra desvia! Seu plano falha!")
        elif escolha == "2":
            if self.teste_atributo("COR", 8):
                self.digitar_lento("\n✅ Ataque surpresa! Ustra é derrotado!")
                vitoria = True
            else:
                self.digitar_lento("\n❌ Ustra é rápido demais! Você se machuca!")
                self.alterar_vida(-25)
        elif escolha == "3":
            if self.teste_atributo("EMP", 9):
                self.digitar_lento("\n💡 Você descobre a fraqueza de Ustra! Vitória!")
                vitoria = True
            else:
                self.digitar_lento("\n❌ Ustra ri da sua tentativa! Contra-ataque!")
                self.alterar_vida(-20)
        else:
            dado = self.rolar_dado(10)
            if dado > 8:
                self.digitar_lento("\n💣 Explosivo perfeito! Ustra é neutralizado!")
                vitoria = True
            else:
                self.digitar_lento("\n💥 A explosão te atinge também!")
                self.alterar_vida(-30)
        
        if vitoria:
            self.digitar_lento("\n🎉 Você derrota Ustra e liberta Sertão!")
        else:
            self.digitar_lento("\n💥 Ustra te fere gravemente! Sertão intervém!")
            self.digitar_lento("⚔️ Sertão se sacrifica para derrotar Ustra!")
            self.alterar_vida(-40)
        
        self.missoes_completas += 1
        self.digitar_lento("\n🎉 MISSÃO 5 CONCLUÍDA! Mas a Rainha-Mãe sela as saídas!")
        input("\n⏎ Continuar...")
    
    def missao_6(self):
        """Missão 6: A Rainha-Mãe"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("MISSÃO 6: A RAINHA-MÃE")
        print("=" * 70)
        
        self.digitar_lento("\n📍 Local: Santuário subterrâneo da Rainha-Mãe")
        self.digitar_lento("👑 A Rainha-Mãe tenta corromper sua mente")
        self.digitar_lento("💭 Ela revela segredos sobre seus pais...")
        self.digitar_lento("😵 Luta mental contra a influência psíquica...")
        self.digitar_lento("💪 Sua humanidade é sua maior arma!")
        
        self.pausar(2)
        
        print("\n💖 BATALHA MENTAL FINAL!")
        print("[1] 💭 Lembrar dos ensinamentos de Sertão (EMPATIA)")
        print("[2] 🌟 Concentrar na esperança do povo (EMPATIA)")
        print("[3] 🔥 Usar a raiva como combustível (CORAGEM)")
        print("[4] 🧠 Raciocínio lógico contra a loucura (ASTÚCIA)")
        
        escolha = input("\n🎯 Como você resiste? ").strip()
        
        resistencia = False
        
        if escolha in ["1", "2"]:
            if self.teste_atributo("EMP", 8):
                self.digitar_lento("\n💪 Sua empatia quebra o controle mental!")
                resistencia = True
            else:
                self.digitar_lento("\n😵 Você quase cede, mas Sertão te salva!")
        elif escolha == "3":
            if self.teste_atributo("COR", 7):
                self.digitar_lento("\n🔥 Sua determinação vence a influência!")
                resistencia = True
            else:
                self.digitar_lento("\n💀 Você é quase corrompido!")
        else:
            if self.teste_atributo("AST", 6):
                self.digitar_lento("\n🧠 Sua lógica derrota a insanidade!")
                resistencia = True
            else:
                self.digitar_lento("\n🤯 A mente da Rainha é muito poderosa!")
        
        if resistencia:
            self.digitar_lento("\n✨ VOCÊ RESISTIU! A Rainha-Mãe fica vulnerável!")
        else:
            self.digitar_lento("\n⚡ A batalha foi difícil, mas você sobrevive!")
        
        self.digitar_lento("\n💥 Sertão usa explosivos para destruir o núcleo!")
        self.digitar_lento("🏰 O Palácio desmorona... Fuga desesperada!")
        
        self.missoes_completas += 1
        input("\n⏎ Continuar para o epílogo...")
    
    def epilogo(self):
        """Epílogo do jogo"""
        self.limpar_tela()
        print("=" * 70)
        self.digitar_lento("EPÍLOGO: O AMANHECER INCERTO")
        print("=" * 70)
        
        self.digitar_lento("\n🌅 O sol nasce sobre a Colmeia Carioca...")
        self.digitar_lento("🏰 O Palácio da República é destruído")
        self.digitar_lento("👑 A Rainha-Mãe está morta")
        self.digitar_lento("⚔️  Mas o General Castelo assume o controle")
        self.digitar_lento("🔥 A luta pela liberdade apenas começou...")
        
        self.pausar(2)
        
        # Consequências das escolhas
        if self.escolhas_importantes.get("cigarra") == "poupado":
            self.digitar_lento("\n🐜 SURPRESA: A cigarra que você poupou retorna!")
            self.digitar_lento("💚 Ela traz insetos dissidentes para a resistência!")
            self.digitar_lento("🌟 Sua compaixão rendeu aliados inesperados!")
        else:
            self.digitar_lento("\n⚠️  A resistência será mais difícil sem aliados...")
            self.digitar_lento("💔 Suas escolhas têm consequências...")
        
        # Resultado final baseado na vida e missões
        self.mostrar_status()
        
        if self.personagem["vida"] >= 70:
            self.digitar_lento(f"\n🎖️  {self.personagem['nome']} é um herói incontestável!")
            self.digitar_lento("💪 Você liderará a resistência com força total!")
        elif self.personagem["vida"] >= 30:
            self.digitar_lento(f"\n🌟 {self.personagem['nome']} é um líder ferido mas determinado!")
            self.digitar_lento("🩹 Você precisa se recuperar, mas continuará lutando!")
        else:
            self.digitar_lento(f"\n⚕️  {self.personagem['nome']} está gravemente ferido!")
            self.digitar_lento("🛌 Mas sua história inspirará outros a continuar!")
        
        self.digitar_lento("\n🇧🇷 A batalha pelo Brasil recém-começou...")
        self.digitar_lento("🔮 O futuro está em suas mãos, Bug Hunter!")
        
        self.pausar(3)
        
        print("\n" + "=" * 70)
        self.digitar_lento("🎭 FIM DO JOGO - OBRIGADO POR JOGAR BUG HUNTERS!")
        print("=" * 70)
        
        # Estatísticas finais
        print(f"\n📊 ESTATÍSTICAS FINAIS DE {self.personagem['nome'].upper()}:")
        print(f"🎯 Missões completas: {self.missoes_completas}/6")
        print(f"❤️  Vida final: {self.personagem['vida']}/{self.personagem['vida_maxima']}")
        print(f"💪 Nível de Coragem: {self.personagem['COR']}")
        print(f"🧠 Nível de Astúcia: {self.personagem['AST']}")
        print(f"💖 Nível de Empatia: {self.personagem['EMP']}")
        
        if self.escolhas_importantes.get("cigarra") == "poupado":
            print("🐜 Aliados entre os insetos: SIM")
        else:
            print("🐜 Aliados entre os insetos: NÃO")
        
        print("\n" + "=" * 70)
    
    def jogar(self):
        """Função principal que executa o jogo completo"""
        try:
            self.criar_personagem()
            
            # Executar missões em sequência
            missoes = [
                self.missao_1,
                self.missao_2, 
                self.missao_3,
                self.missao_4,
                self.missao_5,
                self.missao_6
            ]
            
            for missao in missoes:
                if self.personagem["vida"] <= 0:
                    self.limpar_tela()
                    print("💀" * 70)
                    self.digitar_lento("FIM DE JOGO - VOCÊ MORREU")
                    print("💀" * 70)
                    self.digitar_lento(f"\n{self.personagem['nome']} caiu em combate...")
                    self.digitar_lento("Mas sua luta inspirará outros Bug Hunters!")
                    return
                missao()
            
            # Epílogo
            self.epilogo()
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Jogo interrompido pelo usuário")
            print("Obrigado por jogar Bug Hunters!")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Reinicie o jogo para tentar novamente.")

def main():
    """Função principal"""
    print("Iniciando BUG HUNTERS...")
    game = BugHuntersGame()
    game.jogar()

if __name__ == "__main__":
    main()