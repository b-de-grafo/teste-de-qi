from util import *
from vertice import *
from math import cos,sin

BRANCO = [255, 255, 255]


class Face:
    def __init__(self, superficie, vertices, cor=BRANCO):
        self.superficie = superficie
        self.vertices = vertices
        self.cor = cor
    
    def __repr__(self):
        r = "[ "
        for v in self.vertices:
            r += f"({v.x}, {v.y}, {v.z}) "
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

    def preenche(self):
        for j in range(len(self.vertices) - 1, 0, -1):
            if j - 1 != 0:
                preenchimento(self.superficie, self.vertices[0], self.vertices[j - 1], self.vertices[j], self.cor)

        return self

    def translada(self, tx=0, ty=0, tz=0):

        matriz_translação = [[1, 0, tx],
                             [0, 1, ty],
                             [0, 0, 1]]

        for vertice in self.vertices:
            print(vertice)
            vertice_t = transpoe_vetor(vertice.get_vetor())
            print(vertice_t)
            vertice = multiplicao_matriz(matriz_translação, vertice_t)
            print(vertice)
        print(self.vertices)
        return self

    def escala(self, lx=1, ly=1, tz=1):

        matriz_escala = [[lx, 0, 0],
                         [0, ly, 0],
                         [0, 0, 1]]

        for vertice in self.vertices:
            print(vertice)
            vertice_t = transpoe_vetor(vertice.get_vetor())
            print(vertice_t)
            vertice = multiplicao_matriz(matriz_escala, vertice_t)
            print(vertice)
        print(self.vertices)
        return self

    def rotaciona(self, teta):
        matriz_rotacao = [[cos(teta), -sin(teta), 0],
                         [sin(teta), cos(teta), 0],
                         [0, 0, 1]]

        for vertice in self.vertices:
            print(vertice)
            vertice_t = transpoe_vetor(vertice.get_vetor())
            print(vertice_t)
            vertice = multiplicao_matriz(matriz_rotacao, vertice_t)
            print(vertice)
        print(self.vertices)
        return self

