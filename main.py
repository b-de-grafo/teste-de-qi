import pygame
import math

from vertice import *
from face import *

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
			
			key = pygame.key.get_pressed()
			if key[pygame.K_ESCAPE]:
				break;

			Face(self.superficie, [Vertice(200, 200), Vertice(250, 300)]).desenha(BRANCO)
			Face(self.superficie, [Vertice(250, 300), Vertice(300, 200)]).desenha(BRANCO)
			Face(self.superficie, [Vertice(300, 200), Vertice(350, 300)]).desenha(BRANCO)
			Face(self.superficie, [Vertice(350, 300), Vertice(400, 200)]).desenha(BRANCO)

			quadrado = Face(self.superficie, [Vertice(200, 200),
												Vertice(400, 200),
												Vertice(400, 400),
												Vertice(200, 400)])

			triangulo = Face(self.superficie, [Vertice(400, 400),
												Vertice(200, 400),
												Vertice(300, 200)])

			quadrado.desenha(VERMELHO)
			triangulo.desenha(VERDE)

			self.tela.blit(self.superficie, [0, 0])
			pygame.display.flip()
			

	def eventos(self):
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				self.rodando = False
		
jogo = Jogo()
jogo.loop()
