from util import *
from vertice import *

class Face:
    def __init__(self, superficie, vertices, cor):
        self.superficie = superficie
        self.vertices = vertices
        self.cor = cor
    
    def __repr__(self):
        r = "[ "
        for v in self.vertices:
            r += f"({v.x}, {v.y}, {v.z}) "
        r += "]"
        return r

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

    def translacao(self, Tx=0, Ty=0, Tz=0):
        novos_vertices = []

        for v in self.vertices:
            novo_v = Vertice(v.x + Tx, v.y + Ty, v.z + Tz)
            if novo_v.x < 0 or novo_v.y < 0 or novo_v.z < 0:
                print("ERRO: O objeto foi posicionado fora da área da tela.")
                exit()

            novos_vertices.append(novo_v)
        
        return Face(self.superficie, novos_vertices, self.cor)


f1 = Face(None, [Vertice(100, 100), Vertice(200, 200)], [255, 255, 255])
f1 = Face.translacao(f1, Ty=20)
print(f1)
