"""
class Desenho:
    def __init__(self, poligonos):
        self.poligonos = poligonos

    def desenha(self):
        for poligono in self.poligonos:
            poligono.desenha()
"""
from util import *

class Objeto:
    def __init__(self, faces):
        self.faces = faces
    
    def desenha(self):
        for face in self.faces:
            face.desenha()
        
        for i in range(len(self.faces[0].vertices)):
            reta(self.faces[0].superficie, self.faces[0].vertices[i], self.faces[1].vertices[i], self.faces[0].cor)
            
    