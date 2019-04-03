from util import *

class Face:
	def __init__(self, superficie, vertices):
		self.superficie = superficie
		self.vertices = vertices

	def desenha(self, cor):
		for i in range(len(self.vertices)):
			if i < len(self.vertices) - 1:
				reta(self.superficie, self.vertices[i], self.vertices[i + 1], cor)
			else:
				reta(self.superficie, self.vertices[0], self.vertices[i], cor)