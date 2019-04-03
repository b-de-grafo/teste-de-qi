class Desenho:
    def __init__(self, poligonos):
        self.poligonos = poligonos
        self.offset = [0, 0]

    def desenha(self):
        # TODO transladar os polígonos pro offset
        for poligono in self.poligonos:
            poligono.desenha()
