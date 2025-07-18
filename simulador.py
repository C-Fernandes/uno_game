from game.player import Jogador
from game.engine import GameEngine
from collections import Counter

def simular(jogadores_info, n_partidas=1000):
    vitorias = Counter()
    for _ in range(n_partidas):
        jogadores = [Jogador(nome, estrategia=estrategia) for nome, estrategia in jogadores_info]
        jogo = GameEngine(jogadores)
        vencedor = jogo.rodar_partida(silencioso=True)
        if vencedor:
            vitorias[vencedor.nome] += 1
    return vitorias

if __name__ == "__main__":
    jogadores_info = [
        ("Aleatório 1", "aleatoria"),
        ("Cor-Fav", "cor_favorita"),
        ("Agressivo", "agressiva"),
        ("Reservista", "reservista"),
        ("Camaleao", "camaleao"),
        ("Oportunista", "oportunista")
    ]
    resultados = simular(jogadores_info, n_partidas=1000)
    print("Vitórias após 1000 partidas:")
    for nome, vitorias in resultados.items():
        print(f"{nome}: {vitorias}")
