from math import radians
from util import *


class Objeto:
    def __init__(self, faces):
        self.faces = faces
    
    def desenha(self, rotaciona_x=False, rotaciona_y=False, rotaciona_z=False):
        if rotaciona_x:
            self.faces = self.rotaciona_x(radians(1)).faces
        if rotaciona_y:
            self.faces = self.rotaciona_y(radians(1)).faces
        if rotaciona_z:
            self.faces = self.rotaciona_z(radians(1)).faces

        for face in self.faces:
            face.desenha()
        
        for i in range(len(self.faces[0].vertices)):
            reta(self.faces[0].superficie, self.faces[0].vertices[i], self.faces[1].vertices[i], self.faces[0].cor)

    def muda_cor(self, cor):
        novas_faces = []
        for face in self.faces:
            novas_faces.append((face.muda_cor(cor)))

        return Objeto(novas_faces)
            
    def rotaciona_x(self, teta):
        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].rotaciona_x(teta))

        return Objeto(novas_faces)

    def rotaciona_y(self, teta):
        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].rotaciona_y(teta))

        return Objeto(novas_faces)

    def rotaciona_z(self, teta):
        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].rotaciona_z(teta))

        return Objeto(novas_faces)

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

    def cisalha_3d(self, kx, ky):

        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].cisalha_3d(kx, ky))

        return Objeto(novas_faces)

    def rotaciona_x_ponto(self, teta, ind_face=0, ind_ponto=0):
        delta_x = -self.faces[ind_face].vertices[ind_ponto][0]
        delta_y = -self.faces[ind_face].vertices[ind_ponto][1]
        delta_z = -self.faces[ind_face].vertices[ind_ponto][2]

        # Translada para a origem, faz lá a rotação e translada de volta
        return self.translada_3d(delta_x, delta_y, delta_z).rotaciona_x(teta).translada_3d(-delta_x, -delta_y, -delta_z)


    def rotaciona_y_ponto(self, teta, ind_face=0, ind_ponto=0):
        delta_x = -self.faces[ind_face].vertices[ind_ponto][0]
        delta_y = -self.faces[ind_face].vertices[ind_ponto][1]
        delta_z = -self.faces[ind_face].vertices[ind_ponto][2]

        # Translada para a origem, faz lá a rotação e translada de volta
        return self.translada_3d(delta_x, delta_y, delta_z).rotaciona_y(teta).translada_3d(-delta_x, -delta_y, -delta_z)

    def rotaciona_z_ponto(self, teta, ind_face=0, ind_ponto=0):
        delta_x = -self.faces[ind_face].vertices[ind_ponto][0]
        delta_y = -self.faces[ind_face].vertices[ind_ponto][1]
        delta_z = -self.faces[ind_face].vertices[ind_ponto][2]

        # Translada para a origem, faz lá a rotação e translada de volta
        return self.translada_3d(delta_x, delta_y, delta_z).rotaciona_z(teta).translada_3d(-delta_x, -delta_y, -delta_z)

    def escala_3d_ponto(self, lx, ly, lz, ind_face=0, ind_ponto=0):
        delta_x = -self.faces[ind_face].vertices[ind_ponto][0]
        delta_y = -self.faces[ind_face].vertices[ind_ponto][1]
        delta_z = -self.faces[ind_face].vertices[ind_ponto][2]

        # Translada para a origem, faz lá a escala e translada de volta
        return self.translada_3d(delta_x, delta_y, delta_z).escala_3d(lx, ly, lz).translada_3d(-delta_x, -delta_y, -delta_z)

    def cisalha_3d_ponto(self, kx, ky, kz=0, ind_face=0, ind_ponto=0):
        delta_x = -self.faces[ind_face].vertices[ind_ponto][0]
        delta_y = -self.faces[ind_face].vertices[ind_ponto][1]
        delta_z = -self.faces[ind_face].vertices[ind_ponto][2]

        # Translada para a origem, faz lá a escala e translada de volta
        return self.translada_3d(delta_x, delta_y, delta_z).cisalha_3d(kx, ky).translada_3d(-delta_x, -delta_y, -delta_z)


    def mapeamento_sru_srd(self, xdmax, xumax, ydmax, yumax):
        novas_faces = []
        for i in range(len(self.faces)):
            novas_faces.append(self.faces[i].mapeamento_sru_srd(xdmax, xumax, ydmax, yumax))

        return Objeto(novas_faces)

