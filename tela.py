class Tela:
    def __init__(self, perguntas, respostas, correta, area_das_respostas):
        self.perguntas = perguntas
        self.respostas = respostas
        self.correta = correta
        self.area_das_respostas = area_das_respostas

    def desenha(self):
        for desenho in self.perguntas:
            desenho.desenha()
        for desenho in self.respostas:
            desenho.desenha()
        for desenho in self.area_das_respostas:
            desenho.desenha()
