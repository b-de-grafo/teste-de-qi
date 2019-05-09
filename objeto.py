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
