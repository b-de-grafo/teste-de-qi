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
            else:
                self.vertices.append(vertice)
        self.cor = cor
    
    def __repr__(self):
        r = "[ "
        for v in self.vertices:
            r += f"({v[0]}, {v[1]}, {v[2]}) "
        r += "]"
        return r

    def desenha(self, cor=None):
        if cor is None:
            cor = self.cor

        # Desenha reta entre os vértices
        for i in range(len(self.vertices)):
            if i < len(self.vertices) - 1:
                reta(self.superficie, self.vertices[i], self.vertices[i + 1], cor)
            else:
                reta(self.superficie, self.vertices[0], self.vertices[i], cor)

    def translada(self, tx=0, ty=0):
        matriz_translacao = [[1, 0, tx],
                             [0, 1, ty],
                             [0, 0, 1]]

        novos_vertices = []
        for vertice in self.vertices:
            novo_vertice = transpoe_vetor(multiplica_matrizes(matriz_translacao, transpoe_vetor(vertice)))

            # Arredonda possíveis floats do vetor
            for i in range(len(novo_vertice)):
                novo_vertice[i] = int(novo_vertice[i])

            novos_vertices.append(novo_vertice)

        return Face(self.superficie, novos_vertices, self.cor)

    def escala(self, lx=1, ly=1):
        matriz_escala = [[lx, 0 , 0],
                         [0 , ly, 0],
                         [0 , 0 , 1]]

        novos_vertices = []
        for vertice in self.vertices:
            novo_vertice = transpoe_vetor(multiplica_matrizes(matriz_escala, transpoe_vetor(vertice)))

            # Arredonda possíveis floats do vetor
            for i in range(len(novo_vertice)):
                novo_vertice[i] = int(novo_vertice[i])

            novos_vertices.append(novo_vertice)

        return Face(self.superficie, novos_vertices, self.cor)

    def rotaciona(self, teta):
        matriz_rotacao = [[cos(teta), -sin(teta), 0],
                          [sin(teta),  cos(teta), 0],
                          [0        ,  0        , 1]]

        novos_vertices = []
        for vertice in self.vertices:
            novo_vertice = transpoe_vetor(multiplica_matrizes(matriz_rotacao, transpoe_vetor(vertice)))

            # Arredonda possíveis floats do vetor
            for i in range(len(novo_vertice)):
                novo_vertice[i] = int(novo_vertice[i])

            novos_vertices.append(novo_vertice)

        return Face(self.superficie, novos_vertices, self.cor)

    def cisalhamento(self, kx, ky):
        novos_vertices = []
        matriz_rotacao = [[1 , kx, 0],
                          [ky, 1 , 0],
                          [0 , 0 , 1]]

        for vertice in self.vertices:
            novo_vertice = transpoe_vetor(multiplica_matrizes(matriz_rotacao, transpoe_vetor(vertice)))

            # Arredonda possíveis floats do vetor
            for i in range(len(novo_vertice)):
                novo_vertice[i] = int(novo_vertice[i])

            novos_vertices.append(novo_vertice)

        return Face(self.superficie, novos_vertices, self.cor)

    def escala_no_ponto(self, lx, ly, ind_ponto=0):
        delta_x = -self.vertices[ind_ponto][0]
        delta_y = -self.vertices[ind_ponto][1]

        # Translada para a origem, faz lá a escala e translada de volta
        return self.translada(delta_x, delta_y).escala(lx, ly).translada(-delta_x, -delta_y)

    def rotaciona_no_ponto(self, teta, ind_ponto=0):
        delta_x = -self.vertices[ind_ponto][0]
        delta_y = -self.vertices[ind_ponto][1]

        # Translada para a origem, faz lá a rotação e translada de volta
        return self.translada(delta_x, delta_y).rotaciona(teta).translada(-delta_x, -delta_y)

    def cisalhamento_no_ponto(self, kx, ky, ind_ponto=0):
        delta_x = -self.vertices[ind_ponto][0]
        delta_y = -self.vertices[ind_ponto][1]

        # Translada para a origem, faz lá o cisalhamento e transalada de volta
        return self.translada(delta_x, delta_y).cisalhamento(kx, ky).translada(-delta_x, -delta_y)
