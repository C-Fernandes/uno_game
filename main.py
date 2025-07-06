# main.py

from game.player import Jogador
from game.engine import GameEngine

def main():
    # 1. Crie os jogadores que participarão da partida
    jogadores = [
        Jogador(nome="Fernando"),
        Jogador(nome="Maria"),
        Jogador(nome="José"),
        Jogador(nome="Ana")
    ]

    # 2. Crie o motor do jogo com a lista de jogadores
    motor_do_jogo = GameEngine(jogadores)

    # 3. Rode a partida!
    motor_do_jogo.rodar_partida()


if __name__ == "__main__":
    main()