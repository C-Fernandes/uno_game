import matplotlib.pyplot as plt

# Dados de vitórias por estratégia
dados = {'Aleatório 1': 220, 'Cor-Fav': 300, 'Agressivo': 410, 'Aleatório 2': 70}
nomes = list(dados.keys())
valores = list(dados.values())

# Criando o gráfico de barras
plt.bar(nomes, valores, color='skyblue')

# Título e rótulos
plt.title('Vitórias por Estratégia (1000 partidas)')
plt.ylabel('Número de Vitórias')
plt.xticks(rotation=45)

# Adiciona porcentagens acima das barras
total = sum(valores)
for i, v in enumerate(valores):
    plt.text(i, v + 10, f"{(v / total) * 100:.1f}%", ha='center', fontsize=9)

# Ajustes e exibição
plt.tight_layout()
plt.show()
