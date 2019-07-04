from face import *
from quaternios import distancia


class Objeto:
    def __init__(self, faces):
        self.faces = faces
        self.rotacao = 0
        self.passo_rotacao = 0
        self.eixo = (0, 1, 0)
        self.curva_ind = 0

    def desenha(self):
        # Preenche as faces
        if self.faces[0].preenchido or self.faces[0].preenchido: #q?
            self.priorityfill()


        else:  # Wireframe
            for face in self.faces:
                face.desenha()

            for i in range(len(self.faces[0].vertices)):
                reta(self.faces[0].superficie, self.faces[0].vertices[i], self.faces[1].vertices[i], self.faces[0].cor)

    def muda_cor(self, cor):
        novas_faces = []
        for face in self.faces:
            novas_faces.append((face.muda_cor(cor)))

        return Objeto(novas_faces)

    def set_rotacao(self, passo, eixo):
        self.passo_rotacao = passo
        self.eixo = eixo

    def mapeamento_sru_srd(self, xdmax, xumax, ydmax, yumax):
        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].mapeamento_sru_srd(xdmax, xumax, ydmax, yumax))

        return Objeto(novas_faces)

    def inc_rotacao(self):
        # Incrementa o passo
        self.rotacao += self.passo_rotacao

    def priorityfill(self):
        faces_ord = []
        for face in self.faces:
            soma = 0
            for vertice in face.vertices:
                soma += vertice[2]
            media = soma / len(face.vertices)

            luz = (0, 0, 1)
            v1 = face.vertices[0][:3]
            v2 = face.vertices[1][:3]
            v3 = face.vertices[2][:3]
            cor = (50, 250, 150)
            cor = intensidade(luz, v1, v2, v3, cor)

            faces_ord.append([face.muda_cor(cor), media])

        # incluir faces laterais
        frente = self.faces[0]
        verso = self.faces[1]
        incremento_cor = 200 / len(self.faces[-1].vertices)  # incrementar de acordo com o número de faces laterais

        novos_vertices = []
        for i in range(len(self.faces[-1].vertices)):
            if i < len(self.faces[-1].vertices)-1:
                novos_vertices = [frente.vertices[i], frente.vertices[i+1], verso.vertices[i+1], verso.vertices[i]]

            elif i == len(self.faces[-1].vertices)-1:
                novos_vertices = [frente.vertices[i], frente.vertices[0], verso.vertices[0], verso.vertices[i]]

            luz = (0, 0, 1)
            v1 = novos_vertices[0][:3]
            v2 = novos_vertices[1][:3]
            v3 = novos_vertices[2][:3]
            cor = (50, 250, 150)
            cor = intensidade(luz, v1, v2, v3, cor)

            face_lateral = Face(frente.superficie, novos_vertices, cor, frente.preenchido, frente.arestas, frente.tela)

            soma = 0
            for vertice in novos_vertices:
                soma += vertice[2]
            media = soma / len(novos_vertices)

            faces_ord.append([face_lateral, media])

        def get_media(lista):
            return lista[1]

        faces_ord.sort(key=get_media, reverse=True)

        for face in faces_ord:
            face[0].desenha()

    def translada_3d(self, x, y, z):
        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].translada_3d(x, y, z))

        return Objeto(novas_faces)

    def escala_3d(self, lx, ly, lz):
        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].escala_3d(lx, ly, lz))

        return Objeto(novas_faces)

    def rotaciona_quaternio(self):
        # Transforma o ângulo em inteiro então as rotações são sempre inteiras, mas o ângulo guardado no objeto não
        return self._rotaciona_quaternio(int(self.rotacao), self.eixo)

    def _rotaciona_quaternio(self, teta, eixo=(0, 0, 0)):
        novas_faces = []

        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].rotaciona(teta, eixo))

        return Objeto(novas_faces)

    def get_curva_ind(self):
        if self.curva_ind < 100:
            self.curva_ind = self.curva_ind + 1
        return self.curva_ind - 1

# k = coeficiente de reflexão no ponto, I = Ip(intensidade da luz) * cos Teta * k + Ia(intensidade da luz)
def intensidade(luz, v1, v2, v3, cor, k = 0.9, intensidade_no_ponto = (1, 1, 1)):
    vetor_luz = subtracao(v1, luz)
    vetor_aux1 = subtracao(v2, v1)
    vetor_aux2 = subtracao(v3, v1)
    vetor_superficie = produto_vetorial(vetor_aux2, vetor_aux1) # vetor normal do plano A ORDEM FAZ DIFERENCA
    x1, y1, z1 = vetor_luz
    x2, y2, z2 = vetor_superficie
    norma_luz = sqrt(x1**2 + y1**2 + z1**2) # modulo do vetor_luz
    norma_superficie = sqrt(x2**2 + y2**2 + z2**2) # modulo do vetor_superficie
    cosseno_teta = produto_escalar(vetor_luz, vetor_superficie)/(norma_luz * norma_superficie) # equacao do produto interno de vetores
    cosseno_teta = float('%.4f' % cosseno_teta)
    # return produto(k,adicao(produto(k, produto(cosseno_teta, intensidade_no_ponto)), intensidade_no_ponto))
    # intensidade_da_cor = produto(k, produto(cosseno_teta, intensidade_no_ponto))
    intensidade_da_cor = produto(k, adicao(produto(k, produto(cosseno_teta, intensidade_no_ponto)), intensidade_no_ponto))
    nova_cor = []
    # Existe uma possibilidade de todos os pontos da cor convergirem para 255
    # mas como a cor original (Verde -> 50, 250, 150) é parametro acho que isso não é problema
    for i in range(3):
        if cor[i] * intensidade_da_cor[i] > 255:
            nova_cor.append(255)
        else:
            nova_cor.append(cor[i] * intensidade_da_cor[i])
    return nova_cor

