from face import *


class Objeto:
    def __init__(self, faces):
        self.faces = faces
        self.rotacao = 0
        self.paco_rotacao = 0
        self.eixo = (0, 1, 0)

    def desenha(self):
        # Preenche as faces
        if self.faces[0].preenchido or self.faces[0].preenchido:
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

    def set_rotacao(self, paco, eixo):
        self.paco_rotacao = paco
        self.eixo = eixo

    def set_offset(self, eixo):
        ponto = self.faces[0].vertices[0]
        print(ponto)

        xi, yi = round(eixo[0][0]), round(eixo[0][1])
        xf, yf = round(eixo[1][0]), round(eixo[1][1])

        if (xf - xi) != 0:
            m = (yf - yi) / (xf - xi)
            y = m * (ponto[0] - xi) + yi
        else:
            y = 0

        if (yf - yi) != 0:
            m = (xf - xi) / (yf - yi)
            x = m * (ponto[1] - yi) + xi
        else:
            x = ponto[0]

        print(x, y)

    def mapeamento_sru_srd(self, xdmax, xumax, ydmax, yumax):
        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].mapeamento_sru_srd(xdmax, xumax, ydmax, yumax))

        return Objeto(novas_faces)

    def inc_rotacao(self):
        # Incrementa o paço
        self.rotacao += self.paco_rotacao
        if self.rotacao >= 360:
            self.rotacao -= 360
        # Transforma o ângulo em inteiro então as rotações são sempre inteiras, mas o ângulo guardado no objeto não
        return self.rotaciona_quaternio(int(self.rotacao), self.eixo)

    def priorityfill(self):
        faces_ord = []
        for face in self.faces:
            soma = 0
            for vertice in face.vertices:
                soma += vertice[2]
            media = soma / len(face.vertices)
            faces_ord.append([face, media])

        # incluir faces laterais
        frente = self.faces[0]
        verso = self.faces[1]
        incremento_cor = 200 / len(face.vertices)  # incrementar de acordo com o número de faces laterais

        for i in range(len(face.vertices)):
            if i < len(face.vertices)-1:
                novos_vertices = [frente.vertices[i], frente.vertices[i+1], verso.vertices[i+1], verso.vertices[i]]

            elif i == len(face.vertices)-1:
                novos_vertices = [frente.vertices[i], frente.vertices[0], verso.vertices[0], verso.vertices[i]]

            cor = [50 + i * incremento_cor] * 3
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

    def rotaciona_quaternio(self, teta, eixo=(0, 0, 0)):
        novas_faces = []

        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].rotaciona(teta, eixo))

        return Objeto(novas_faces)
