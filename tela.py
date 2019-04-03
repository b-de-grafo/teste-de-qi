class Tela:
    def __init__(self, perguntas, respostas, correta):
        self.perguntas = perguntas
        self.respostas = respostas
        self.correta = correta

    def desenha(self):
        for poligono in self.perguntas:
            poligono.desenha()
        for poligono in self.respostas:
            poligono.desenha()
