# simulador.py (Versão Corrigida e Completa)

from game.player import Jogador
from game.engine import GameEngine
from collections import Counter
import matplotlib.pyplot as plt


def simular(jogadores_info, n_partidas=1000):
    vitorias = Counter()
    for _ in range(n_partidas):
        jogadores = [Jogador(nome, estrategia=estrategia) for nome, estrategia in jogadores_info]
        jogo = GameEngine(jogadores)
        vencedor = jogo.rodar_partida(silencioso=True)
        if vencedor:
            vitorias[vencedor.nome] += 1
    return vitorias

def gerar_grafico_resultados(resultados_simulacao):
    dados = resultados_simulacao
    dados_ordenados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=True))
    
    nomes = list(dados_ordenados.keys())
    valores = list(dados_ordenados.values())

    plt.figure(figsize=(10, 6))
    plt.bar(nomes, valores, color='skyblue')

    plt.title(f'Vitórias por Estratégia ({sum(valores)} partidas)')
    plt.ylabel('Número de Vitórias')
    plt.xticks(rotation=45, ha="right")

    total = sum(valores)
    if total > 0:
        for i, v in enumerate(valores):
            
            posicao_texto = v + (total * 0.01) 
            plt.text(i, posicao_texto, f"{(v / total) * 100:.1f}%", ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    jogadores_info = [
        ("Aleatório 1", "aleatoria"),
        ("Cor-Fav", "cor_favorita"),
        ("Agressivo", "agressiva"),
        ("Reservista", "reservista"),
        ("Camaleao", "camaleao"),
        ("Oportunista", "oportunista"),
        ("Finalista", "finalista"),
        ("Trocar cor", "trocar_cor")
    ]


    num_partidas = 10000
    resultados = simular(jogadores_info, n_partidas=num_partidas)
    
    resultados_ordenados = sorted(resultados.items(), key=lambda item: item[1], reverse=True)
    print(f"Vitórias após {num_partidas} partidas (Pódio):")
    for posicao, (nome, vitorias) in enumerate(resultados_ordenados, start=1):
        print(f"{posicao}º - {nome}: {vitorias} vitórias")

    gerar_grafico_resultados(resultados)