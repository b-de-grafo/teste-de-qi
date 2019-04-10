class Tela:
    def __init__(self, perguntas, respostas, correta, areaDasRespostas):
        self.perguntas = perguntas
        self.respostas = respostas
        self.correta = correta
        self.areaDasRespostas = areaDasRespostas

        # TODO: dispor os desenhos de modo que não fiquem um por cima do outro, aí bota isso no offset de cada um

    def desenha(self):
        for desenho in self.perguntas:
            desenho.desenha()
        for desenho in self.respostas:
            desenho.desenha()
        for desenho in self.areaDasRespostas:
            desenho.desenha()
