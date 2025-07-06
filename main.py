from game.player import Jogador
from game.engine import GameEngine

def main():
    jogadores = [
        Jogador(nome="Fernando"),
        Jogador(nome="Maria"),
        Jogador(nome="José"),
        Jogador(nome="Ana")
    ]

    motor_do_jogo = GameEngine(jogadores)

    motor_do_jogo.rodar_partida()


if __name__ == "__main__":
    main()