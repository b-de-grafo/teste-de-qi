import pygame
import math

from vertice import *
from face import *

BRANCO = [255, 255, 255]
VERMELHO = [255, 0, 0]
VERDE = [0, 255, 0]
PRETO = [0, 0, 0]

#Estados - nomes temporarios - mudem como quiser
TELA_INICIAL = 0
TELA1 = 1
TELA2 = 2
TELA3 = 3
TELA4 = 4
TELA5 = 5
TELA6 = 6
TELA7 = 7
TELA8 = 8
TELA9 = 9
TELA10 = 10
TELA_FINAL = 11

class Jogo:
	def __init__(self):
		pygame.init()

		self.estado = 0
		self.tamanho_tela = [600, 600]
		self.tela = pygame.display.set_mode(self.tamanho_tela)
		self.superficie = pygame.Surface(self.tamanho_tela)

		self.rodando = True

	def loop(self):
		while self.rodando:
			self.eventos()

			self.tela_atual()

			self.tela.blit(self.superficie, [0,0])
			pygame.display.flip()
			

	def eventos(self):
		key = pygame.key.get_pressed()
		for evento in pygame.event.get():
			if key[pygame.K_ESCAPE]:
				self.rodando = False
			#tecla n e b sao para debug
			if key[pygame.K_n] and self.estado < TELA_FINAL:
				self.estado += 1
			if key[pygame.K_b] and self.estado > TELA_INICIAL:
				self.estado -= 1
			if evento.type == pygame.QUIT:
				self.rodando = False

	#Nome temporario
	def tela_inicial(self):
		self.superficie.fill(PRETO) #Preciso so para debug

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

	def tela1(self):
		self.superficie.fill(PRETO)

		Face(self.superficie, [Vertice(200, 200),
		                       Vertice(400, 200),
		                       Vertice(400, 400),
		                       Vertice(200, 400)]).desenha(BRANCO)

	def tela2(self):
		self.superficie.fill(VERDE)

		Face(self.superficie, [Vertice(200, 200),
		                       Vertice(400, 200),
		                       Vertice(400, 400),
		                       Vertice(200, 400)]).desenha(PRETO)

	def tela3(self):
		self.superficie.fill(VERMELHO)

		Face(self.superficie, [Vertice(200, 200),
		                       Vertice(400, 200),
		                       Vertice(400, 400),
		                       Vertice(200, 400)]).desenha(VERDE)

	def tela4(self):
		self.superficie.fill(PRETO)

		Face(self.superficie, [Vertice(400, 400),
		                       Vertice(200, 400),
		                       Vertice(300, 200)]).desenha(BRANCO)

	def tela5(self):
		self.superficie.fill(VERMELHO)

		Face(self.superficie, [Vertice(400, 400),
		                       Vertice(200, 400),
		                       Vertice(300, 200)]).desenha(VERDE)

	def tela6(self):
		self.superficie.fill(VERDE)

		Face(self.superficie, [Vertice(400, 400),
		                       Vertice(200, 400),
		                       Vertice(300, 200)]).desenha(VERMELHO)

	def tela7(self):
		self.superficie.fill(PRETO)

		Face(self.superficie, [Vertice(200, 200), Vertice(250, 300)]).desenha(BRANCO)
		Face(self.superficie, [Vertice(250, 300), Vertice(300, 200)]).desenha(BRANCO)
		Face(self.superficie, [Vertice(300, 200), Vertice(350, 300)]).desenha(BRANCO)
		Face(self.superficie, [Vertice(350, 300), Vertice(400, 200)]).desenha(BRANCO)

	def tela8(self):
		self.superficie.fill(VERDE)

		Face(self.superficie, [Vertice(200, 200), Vertice(250, 300)]).desenha(VERMELHO)
		Face(self.superficie, [Vertice(250, 300), Vertice(300, 200)]).desenha(VERMELHO)
		Face(self.superficie, [Vertice(300, 200), Vertice(350, 300)]).desenha(VERMELHO)
		Face(self.superficie, [Vertice(350, 300), Vertice(400, 200)]).desenha(VERMELHO)

	def tela9(self):
		self.superficie.fill(VERMELHO)

		Face(self.superficie, [Vertice(200, 200), Vertice(250, 300)]).desenha(VERDE)
		Face(self.superficie, [Vertice(250, 300), Vertice(300, 200)]).desenha(VERDE)
		Face(self.superficie, [Vertice(300, 200), Vertice(350, 300)]).desenha(VERDE)
		Face(self.superficie, [Vertice(350, 300), Vertice(400, 200)]).desenha(VERDE)

	def tela10(self):
		self.superficie.fill(PRETO)

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

	def tela_final(self):
		self.superficie.fill(BRANCO)

		Face(self.superficie, [Vertice(200, 200), Vertice(250, 300)]).desenha(PRETO)
		Face(self.superficie, [Vertice(250, 300), Vertice(300, 200)]).desenha(PRETO)
		Face(self.superficie, [Vertice(300, 200), Vertice(350, 300)]).desenha(PRETO)
		Face(self.superficie, [Vertice(350, 300), Vertice(400, 200)]).desenha(PRETO)

		quadrado = Face(self.superficie, [Vertice(200, 200),
		                                  Vertice(400, 200),
		                                  Vertice(400, 400),
		                                  Vertice(200, 400)])

		triangulo = Face(self.superficie, [Vertice(400, 400),
		                                   Vertice(200, 400),
		                                   Vertice(300, 200)])

		quadrado.desenha(VERDE)
		triangulo.desenha(VERMELHO)

	def tela_atual(self):
		if self.estado == TELA_INICIAL:
			self.tela_inicial()
		elif self.estado == TELA1:
			self.tela1()
		elif self.estado == TELA2:
			self.tela2()
		elif self.estado == TELA3:
			self.tela3()
		elif self.estado == TELA4:
			self.tela4()
		elif self.estado == TELA5:
			self.tela5()
		elif self.estado == TELA6:
			self.tela6()
		elif self.estado == TELA7:
			self.tela7()
		elif self.estado == TELA8:
			self.tela8()
		elif self.estado == TELA9:
			self.tela9()
		elif self.estado == TELA10:
			self.tela10()
		else:
			self.tela_final()

jogo = Jogo()
jogo.loop()
