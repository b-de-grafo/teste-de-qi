class Desenho:
    def __init__(self, poligonos):
        self.poligonos = poligonos
        self.offset = [0, 0]

    def desenha(self):
        # TODO transladar os polígonos pro offset
        for poligono in self.poligonos:
            poligono.desenha()


#Face(self.superficie, [[325, 150], [400, 225], [325, 300], [325, 250], [225, 250], [225, 200], [325, 200]], BRANCO).escala_ponto(0.7, 0.7).translada(-200, -100),