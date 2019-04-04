class Vertice:
	def __init__(self, x, y, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return f"({self.x}, {self.y}, {self.z})"