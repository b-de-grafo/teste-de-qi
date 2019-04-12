class Vertice:
	def __init__(self, x, y, z=1):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return f"({self.x}, {self.y}, {self.z})"

	def get_vetor(self):
		return [self.x, self.y, self.z]