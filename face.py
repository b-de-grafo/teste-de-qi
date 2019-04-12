from util import *
from math import cos, sin

BRANCO = [255, 255, 255]


class Face:
    def __init__(self, superficie, vertices, cor=BRANCO):
        self.superficie = superficie

        self.vertices = []
        for vertice in vertices:
            # Converte para coordenadas homogêneas
            if len(vertice) == 2:
                self.vertices.append(vertice + [1])
        self.cor = cor
        self.preenchido = False
    
    def __repr__(self):
        r = "[ "
        for v in self.vertices:
            r += f"({v[0]}, {v[1]}, {v[2]}) "
        r += "]"
        return r

    def desenha(self, cor=None):
        if cor is None:
            cor = self.cor

        for i in range(len(self.vertices)):
            if i < len(self.vertices) - 1:
                reta(self.superficie, self.vertices[i], self.vertices[i + 1], cor)
            else:
                reta(self.superficie, self.vertices[0], self.vertices[i], cor)

        if self.preenchido:
            for j in range(len(self.vertices) - 1, 0, -1):
                if j - 1 != 0:
                    preenchimento(self.superficie, self.vertices[0], self.vertices[j - 1], self.vertices[j], self.cor)

    def preenche(self):
        self.preenchido = True

    def translada(self, tx=0, ty=0):
        novos_vertices = []
        matriz_translacao = [[1, 0, tx],
                             [0, 1, ty],
                             [0, 0, 1]]

        for vertice in self.vertices:
            vertice_t = transpoe_vetor(vertice)
            vertice = multiplicacao_matriz(matriz_translacao, vertice_t)
            novos_vertices.append(vertice)

        return Face(self.superficie, novos_vertices, self.cor)

    def escala(self, lx=1, ly=1):
        novos_vertices = []
        matriz_escala = [[lx, 0, 0],
                         [0, ly, 0],
                         [0, 0, 1]]

        for vertice in self.vertices:
            vertice_t = transpoe_vetor(vertice)
            vertice = multiplicacao_matriz(matriz_escala, vertice_t)
            novos_vertices.append(vertice)
        return Face(self.superficie, novos_vertices, self.cor)

    def rotaciona(self, teta):
        novos_vertices = []
        matriz_rotacao = [[cos(teta), -sin(teta), 0],
                          [sin(teta), cos(teta), 0],
                          [0        , 0        , 1]]

        for vertice in self.vertices:
            vertice_t = transpoe_vetor(vertice)
            vertice = multiplicacao_matriz(matriz_rotacao, vertice_t)
            novos_vertices.append(vertice)
        return Face(self.superficie, novos_vertices, self.cor)

