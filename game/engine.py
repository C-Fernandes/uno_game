from .deck import Baralho
from .player import Jogador

class GameEngine:
    def __init__(self, lista_jogadores):
        self.jogadores = lista_jogadores
        self.baralho = Baralho()
        self.pilha_descarte = []
        self.jogador_atual_idx = 0
        self.cor_atual_jogo = None
        
        
    def _repor_baralho_com_pilha_descarte(self):
        print("\n--- BARALHO DE COMPRAS VAZIO! REEMBARALHANDO O DESCARTE... ---\n")
        
        if len(self.pilha_descarte) > 1:
            carta_do_topo = self.pilha_descarte.pop()
            self.baralho.cartas = self.pilha_descarte[:]
            self.baralho.embaralhar()
            self.pilha_descarte = [carta_do_topo]
            
    def iniciar_jogo(self):
        self.baralho.embaralhar()
        print("--- Jogo de UNO Iniciado ---")

        for jogador in self.jogadores:
            cartas_iniciais = [self.baralho.comprar_carta() for _ in range(7)]
            jogador.receber_cartas(cartas_iniciais)
            print(f"{jogador.nome} recebeu suas cartas.")

        primeira_carta = self.baralho.comprar_carta()
        while primeira_carta.cor == 'Especial':
            self.baralho.cartas.append(primeira_carta)
            self.baralho.embaralhar()
            primeira_carta = self.baralho.comprar_carta()
        
        self.pilha_descarte.append(primeira_carta)
        self.cor_atual_jogo = primeira_carta.cor
        print(f"\nCarta na mesa: {self.get_carta_na_mesa()} | Cor do jogo: {self.cor_atual_jogo}")

    def get_carta_na_mesa(self):
        return self.pilha_descarte[-1]

    def proximo_jogador(self):
        self.jogador_atual_idx = (self.jogador_atual_idx + 1) % len(self.jogadores)

    def rodar_partida(self):
        self.iniciar_jogo()
        vencedor = None
        while not vencedor:
            jogador_da_vez = self.jogadores[self.jogador_atual_idx]
            carta_na_mesa = self.get_carta_na_mesa()
            print(f"\n--- Turno de {jogador_da_vez.nome} ({len(jogador_da_vez.mao)} cartas) ---")
            
            resultado_jogada = jogador_da_vez.escolher_carta(carta_na_mesa, self.cor_atual_jogo)

            if resultado_jogada:
                if isinstance(resultado_jogada, tuple):
                    carta_jogada, nova_cor = resultado_jogada
                    self.pilha_descarte.append(carta_jogada)
                    self.cor_atual_jogo = nova_cor 
                else:
                    carta_jogada = resultado_jogada
                    self.pilha_descarte.append(carta_jogada)
                    self.cor_atual_jogo = carta_jogada.cor

                
                    print(f"Nova carta na mesa: {self.get_carta_na_mesa()} | Cor do jogo: {self.cor_atual_jogo}")

                if len(jogador_da_vez.mao) == 0:
                    vencedor = jogador_da_vez
            
            else: 
                if not self.baralho.cartas:
                    self._repor_baralho_com_pilha_descarte()
                    print("Reembaralhando descarte");
                carta_comprada = self.baralho.comprar_carta()
                if carta_comprada:
                    jogador_da_vez.mao.append(carta_comprada)
               
                    print(f"{jogador_da_vez.nome} comprou uma carta.")
                else:
                  
                    print(f"Não há cartas para comprar! {jogador_da_vez.nome} pula a vez.") 

            
            if not vencedor:
                self.proximo_jogador()

       
        print("\n--- FIM DE JOGO ---")
        print(f"O grande vencedor é: {vencedor.nome}!")

        return vencedor
