import pygame
import math

BRANCO = [255, 255, 255]
VERMELHO = [255, 0, 0]
VERDE = [0, 255, 0]

class Jogo:
	def __init__(self):
		pygame.init()

		self.tamanho_tela = [600, 600]
		self.tela = pygame.display.set_mode(self.tamanho_tela)
		self.superficie = pygame.Surface(self.tamanho_tela)

		self.rodando = True

	def loop(self):
		while self.rodando:
			self.eventos()

			# Desenha pixel
			self.reta([200, 200], [250, 300], BRANCO)
			self.reta([250, 300], [300, 200], BRANCO)
			self.reta([300, 200], [350, 300], BRANCO)
			self.reta([350, 300], [400, 200], BRANCO)

			quadrado = [[200, 200],
						[400, 200],
						[400, 400],
						[200, 400]]

			triangulo = [[400, 400],
						 [200, 400],
						 [300, 200]]

			self.poligono(quadrado, VERMELHO)
			self.poligono(triangulo, VERDE)

			self.tela.blit(self.superficie, [0, 0])
			pygame.display.flip()
			

	def eventos(self):
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				self.rodando = False

	def reta(self, inicio, fim, cor):
		xi, yi = inicio
		xf, yf = fim

		xstep = 1
		if xf < xi:
			xstep = -1

		for x in range(xi, xf + 1, xstep):
			if (xf - xi) != 0:
				m = (yf - yi) / (xf - xi)
				y = m * (x - xi) + yi

				self.superficie.set_at([x, int(y)], cor)

		ystep = 1
		if (yf < yi):
			ystep = -1
		for y in range(yi, yf + 1, ystep):
			if (yf - yi) != 0:
				m = (xf - xi) / (yf - yi)
				x = m * (y - yi) + xi

				self.superficie.set_at([int(x), y], cor)

	def circulo(self, centro, raio, cor):
		a, b = centro

		for x in range(a - raio, a + raio):
			yroot = math.sqrt(math.pow(raio, 2) - math.pow(x - a, 2))
			y1 = yroot + b
			y2 = -yroot + b

			self.superficie.set_at([x, int(y1)], cor)
			self.superficie.set_at([x, int(y2)], cor)

		for y in range(b - raio, b + raio):
			xroot = math.sqrt(math.pow(raio, 2) - math.pow(y - b, 2))
			x1 = xroot + a
			x2 = -xroot + a

			self.superficie.set_at([int(x1), y], cor)
			self.superficie.set_at([int(x2), y], cor)
			
	
	def poligono(self, vertices, cor):
		if len(vertices) < 3:
			print("Isso não é um polígono.")
			exit()

		for i in range(len(vertices)):
			if i < len(vertices)-1:
				self.reta(vertices[i], vertices[i+1], cor)
			else:
				self.reta(vertices[0], vertices[i], cor)
		
jogo = Jogo()
jogo.loop()
