import random
from .card import Carta 

class Baralho:
    def __init__(self):
        self.cartas = []
        self.montar_baralho()

    def montar_baralho(self):
        cores = ['Vermelho', 'Amarelo', 'Verde', 'Azul']
        valores_numericos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        valores_acao = ['Pular', 'Inverter', '+2']

        for cor in cores:
            self.cartas.append(Carta(cor, '0'))
            for valor in valores_numericos:
                self.cartas.append(Carta(cor, valor))
                self.cartas.append(Carta(cor, valor))

        for cor in cores:
            for valor in valores_acao:
                self.cartas.append(Carta(cor, valor))
                self.cartas.append(Carta(cor, valor))

        for _ in range(4):
            self.cartas.append(Carta('Especial', 'Curinga'))
            self.cartas.append(Carta('Especial', 'Curinga+4'))

    def __repr__(self):
        return f'Baralho com {len(self.cartas)} cartas'

    def embaralhar(self):
        random.shuffle(self.cartas)

    def comprar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        return None