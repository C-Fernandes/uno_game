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
        cartas_validas = [c for c in self.mao if self.pode_jogar(c, carta_na_mesa, cor_atual_jogo)]

        if not cartas_validas:
            print(f"{self.nome} não tem cartas para jogar e precisa comprar.")
            return None

        if self.estrategia == "aleatoria":
            carta_escolhida = random.choice(cartas_validas)

        elif self.estrategia == "cor_favorita":
            cores = [c.cor for c in self.mao if c.cor != "Especial"]
            mais_comum = Counter(cores).most_common(1)[0][0] if cores else "Vermelho"
            preferidas = [c for c in cartas_validas if c.cor == mais_comum]
            carta_escolhida = random.choice(preferidas) if preferidas else random.choice(cartas_validas)

        elif self.estrategia == "agressiva":
            especiais = [c for c in cartas_validas if c.valor in ['+2', 'Curinga+4', 'Pular', 'Inverter']]
            carta_escolhida = random.choice(especiais) if especiais else random.choice(cartas_validas)
        elif self.estrategia == "camaleao":
                    cores_na_mao = [c.cor for c in self.mao if c.cor != 'Especial']
                    
                    if not cores_na_mao: 
                        carta_escolhida = random.choice(cartas_validas)
                    else:
                        contagem = Counter(cores_na_mao)
                        cores_ordenadas_por_raridade = [cor for cor, contagem in contagem.most_common()][::-1]
                        
                        carta_escolhida = None
                        for cor_rara in cores_ordenadas_por_raridade:
                            cartas_rara_validas = [c for c in cartas_validas if c.cor == cor_rara]
                            if cartas_rara_validas:
                                carta_escolhida = random.choice(cartas_rara_validas)
                                break
                        
                        if not carta_escolhida:
                            carta_escolhida = random.choice(cartas_validas)
        elif self.estrategia == "reservista":
            cartas_numericas_validas = [c for c in cartas_validas if c.valor.isdigit()]

            if cartas_numericas_validas:
                carta_escolhida = random.choice(cartas_numericas_validas)
            else:
                custo_carta = {'Inverter': 1, 'Pular': 1, '+2': 2, 'Curinga': 3, 'Curinga+4': 4}
                cartas_validas_ordenadas = sorted(
                    cartas_validas,
                    key=lambda c: custo_carta.get(c.valor, 99)
                )
                carta_escolhida = cartas_validas_ordenadas[0]

        elif self.estrategia == "oportunista":
            # --- OPORTUNIDADE 1: Jogar a carta mais forte do jogo ---
            jogada_curinga_mais4 = [c for c in cartas_validas if c.valor == 'Curinga+4']
            if jogada_curinga_mais4:
                carta_escolhida = jogada_curinga_mais4[0]
            
            else:
                # --- OPORTUNIDADE 2: Limpar uma cor inteira da mão ---
                contagem_cores = Counter(c.cor for c in self.mao if c.cor != 'Especial')
                cores_unicas = [cor for cor, cont in contagem_cores.items() if cont == 1]
                
                jogada_de_limpeza = None
                if cores_unicas:
                    # Verifica se alguma das cartas válidas é de uma cor que só temos uma na mão
                    for carta in cartas_validas:
                        if carta.cor in cores_unicas:
                            jogada_de_limpeza = carta
                            break # Encontrou a oportunidade, não precisa procurar mais
                
                if jogada_de_limpeza:
                    carta_escolhida = jogada_de_limpeza
                else:
                    # --- COMPORTAMENTO PADRÃO: Jogar de forma segura ---
                    cartas_numericas_validas = [c for c in cartas_validas if c.valor.isdigit()]
                    if cartas_numericas_validas:
                        carta_escolhida = random.choice(cartas_numericas_validas)
                    else:
                        # --- ÚLTIMO RECURSO: Se não tem número, joga qualquer especial que sobrou
                        carta_escolhida = random.choice(cartas_validas)
        else:
            carta_escolhida = random.choice(cartas_validas)

        self.mao.remove(carta_escolhida)
        if carta_escolhida.cor == 'Especial':
            nova_cor = self._escolher_nova_cor()
            print(f"{self.nome} jogou {carta_escolhida} e escolheu a cor {nova_cor}")
            return (carta_escolhida, nova_cor)
        else:
            print(f"{self.nome} jogou a carta: {carta_escolhida}")
            return carta_escolhida
