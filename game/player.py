import random
from collections import Counter
from .card import Carta

class Jogador:
    def __init__(self, nome, estrategia="aleatoria"):
        self.nome = nome
        self.mao = []
        self.estrategia = estrategia

    def __repr__(self):
        return f'Jogador({self.nome}, Mão: {len(self.mao)} cartas)'

    def receber_cartas(self, cartas):
        self.mao.extend(cartas)
    
    def pode_jogar(self, carta, carta_na_mesa, cor_atual_jogo):
        if carta.cor == 'Especial':
            return True
     
        if carta.cor == cor_atual_jogo:
            return True
        
        if carta.valor == carta_na_mesa.valor:
            return True
        return False

    def _escolher_nova_cor(self):
        cores_na_mao = [carta.cor for carta in self.mao if carta.cor != 'Especial']
        if not cores_na_mao:
            return random.choice(['Vermelho', 'Amarelo', 'Verde', 'Azul'])
        
        contagem_cores = Counter(cores_na_mao)
        cor_mais_comum = contagem_cores.most_common(1)[0][0]
        return cor_mais_comum

    def escolher_carta(self, carta_na_mesa, cor_atual_jogo):
        cartas_validas = []
        for carta in self.mao:
            if self.pode_jogar(carta, carta_na_mesa, cor_atual_jogo):
                cartas_validas.append(carta)

        if cartas_validas:
            carta_escolhida = random.choice(cartas_validas)
            self.mao.remove(carta_escolhida)
            
            if carta_escolhida.cor == 'Especial':
                nova_cor = self._escolher_nova_cor()
                print(f"{self.nome} jogou {carta_escolhida} e escolheu a cor {nova_cor}")
                return (carta_escolhida, nova_cor)
            else:
                print(f"{self.nome} jogou a carta: {carta_escolhida}")
                return carta_escolhida
        else:
            print(f"{self.nome} não tem cartas para jogar e precisa comprar.")
            return None