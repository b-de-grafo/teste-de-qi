from util import *
from quaternios import *

BRANCO = [255, 255, 255]


class Face:
    def __init__(self, superficie, vertices, cor=BRANCO, preenchido=False, arestas=True, tela=None):
        self.superficie = superficie
        self.tela = tela

        self.vertices = []
        for vertice in vertices:
            # Converte para coordenadas homogêneas
            if len(vertice) == 2:
                self.vertices.append(vertice + [1])
            else:
                self.vertices.append(vertice)
        self.cor = cor
        self.preenchido = preenchido
        self.arestas = arestas
    
    def __repr__(self):
        r = "[ "
        for v in self.vertices:
            r += "({}, {}, {}) ".format(v[0], v[1], v[2])
        r += "]"
        return r

    def desenha(self, cor=None):
        if cor is None:
            cor = self.cor

        if self.arestas:
            # Desenha arestas entre os vértices
            for i in range(len(self.vertices)):
                if i < len(self.vertices) - 1:
                    reta(self.superficie, self.vertices[i], self.vertices[i + 1], cor)
                else:
                    reta(self.superficie, self.vertices[0], self.vertices[i], cor)

        if self.preenchido:
            self.preenche()

    def muda_cor(self, cor):
        self.cor = cor
        return self

    def translada_3d(self, tx=0, ty=0, tz=0):
        matriz_translacao = [[1, 0, 0, tx],
                             [0, 1, 0, ty],
                             [0, 0, 1, tz],
                             [0, 0, 0, 1]]

        novos_vertices = []
        for vertice in self.vertices:
            vetor_trans = transpoe_vetor(vertice)
            resultado = multiplica_matrizes(matriz_translacao, vetor_trans)
            novo_vertice = transpoe_vetor(resultado)
            # Arredonda possíveis floats do vetor
            for i in range(len(novo_vertice)):
                novo_vertice[i] = int(novo_vertice[i])

            novos_vertices.append(novo_vertice)
        return Face(self.superficie, novos_vertices, self.cor, self.preenchido, self.arestas, self.tela)

    def escala_3d(self, lx=1, ly=1, lz=1):
        matriz_escala = [[lx, 0, 0, 0],
                         [0, ly, 0, 0],
                         [0, 0, lz, 0],
                         [0, 0, 0, 1]]

        novos_vertices = []
        for vertice in self.vertices:
            novo_vertice = transpoe_vetor(multiplica_matrizes(matriz_escala, transpoe_vetor(vertice)))

            # Arredonda possíveis floats do vetor
            for i in range(len(novo_vertice)):
                novo_vertice[i] = int(novo_vertice[i])

            novos_vertices.append(novo_vertice)

        return Face(self.superficie, novos_vertices, self.cor, self.preenchido, self.arestas)

    def rotaciona(self, teta, eixo=(0, 0, 0)):
        novos_vertices = []

        for vertice in self.vertices:
            novos_vertices.append(rotacao(vertice[:3], teta, eixo) + [1])

        return Face(self.superficie, novos_vertices, self.cor, self.preenchido, self.arestas)

    def mapeamento_sru_srd(self, xdmax, xumax, ydmax, yumax):
        novos_vertices = []
        for v in self.vertices:
            vertice = [v[0] * xdmax / xumax, (v[1]*(-ydmax)/yumax)+ydmax, v[2], v[3]]
            for i in range(len(vertice)):
                vertice[i] = int(vertice[i])
            novos_vertices.append(vertice)
        return Face(self.superficie, novos_vertices, self.cor, self.preenchido, self.arestas, self.tela)

    def preenche(self):
        # Pega o y mais acima e mais abaixo da figura pra iterar só neles
        menor_y = 10000
        maior_y = -10000
        for i in range(len(self.vertices)):
            if self.vertices[i][1] < menor_y:
                menor_y = self.vertices[i][1]
            if self.vertices[i][1] > maior_y:
                maior_y = self.vertices[i][1]

        # Pra cada y do topo da figura até a base
        for y_eixo in range(menor_y, maior_y + 1):
            encontro_retas = []

            # Pra cada par de vértices (basicamente cada aresta)
            for j in range(len(self.vertices)):
                # Coordenadas de cada aresta
                x1, y1, _, _ = self.vertices[j]
                if j + 1 == len(self.vertices):
                    x2, y2, _, _ = self.vertices[0]
                else:
                    x2, y2, _, _ = self.vertices[j + 1]

                # Vê onde a aresta cruza a reta paralela ao eixo x na altura y
                if y1 <= y_eixo <= y2 or y2 <= y_eixo <= y1:
                    if (y2 - y1) != 0:
                        m = (x2 - x1) / (y2 - y1)
                        x = m * (y_eixo - y1) + x1

                        # Adiciona esse ponto num array
                        if int(x) not in encontro_retas:
                            encontro_retas.append(int(x))
                    else:
                        if int(x1) not in encontro_retas:
                            encontro_retas.append(int(x1))

            encontro_retas.sort()
            # Pra cada par de pontos em que a reta cruza a aresta
            if len(encontro_retas) % 2 == 0:
                for par_index in range(0, len(encontro_retas) - 1, 2):
                    # Pinta entre esses dois pontos
                    reta(self.superficie, [encontro_retas[par_index], y_eixo], [encontro_retas[par_index + 1], y_eixo],
                         cor=self.cor)
                    # Se descomentar isso da pra ver cada segmento de reta sendo printado, é bom pra debugar
                    # if self.tela is not None:
                    #     self.tela.blit(self.superficie, [0, 0])
                    # pygame.display.flip()

            # Se descomentar isso da pra ver cada reta sendo printada, é bom pra debugar
            # if self.tela is not None:
            #     self.tela.blit(self.superficie, [0, 0])
            # pygame.display.flip()
