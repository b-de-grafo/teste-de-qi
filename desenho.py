class Desenho:
    def __init__(self, poligonos):
        self.poligonos = poligonos

    def desenha(self):
        for poligono in self.poligonos:
            poligono.desenha()

