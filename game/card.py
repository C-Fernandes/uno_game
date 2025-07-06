class Carta:
    def __init__(self, cor, valor):
        self.cor = cor
        self.valor = valor

    def __repr__(self):
        return f'Carta({self.cor}, {self.valor})'