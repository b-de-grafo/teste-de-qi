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
        for vertice in self.vertices:
            vertice.x = vertice.x + tx
            vertice.y = vertice.y + ty
            vertice.z = vertice.z + tz
        return self

    def escala(self, tx=1, ty=1, tz=1):
        for vertice in self.vertices:
            vertice.x = int(vertice.x * tx)
            vertice.y = int(vertice.y * ty)
            vertice.z = int(vertice.z * tz)
        return self

    def rotaciona(self, teta):
        for vertice in self.vertices:
            vertice.x = int(vertice.x * cos(teta) - vertice.y * sin(teta))
            vertice.y = int(vertice.y * cos(teta) + vertice.x * sin(teta))
        return self
