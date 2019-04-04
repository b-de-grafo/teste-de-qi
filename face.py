from util import *


class Face:
    def __init__(self, superficie, vertices, cor):
        self.superficie = superficie
        self.vertices = vertices
        self.cor = cor

    def desenha(self):
        for i in range(len(self.vertices)):
            if i < len(self.vertices) - 1:
                reta(self.superficie, self.vertices[i], self.vertices[i + 1], self.cor)
            else:
                reta(self.superficie, self.vertices[0], self.vertices[i], self.cor)

    def pinta(self):
        i = 0
        j = len(self.vertices) - 1
        while(i < j):

            if j - 1 != i:
                reta_especial(self.superficie, self.vertices[i],
                              self.vertices[j - 1], self.vertices[j])

            i += 1
            j -= 1
