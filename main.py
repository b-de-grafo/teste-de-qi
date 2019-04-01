import pygame
import math


class Jogo:
    def __init__(self):
        pygame.init()

        self.tamanho_tela = [400, 500]
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        self.superficie = pygame.Surface(self.tamanho_tela)

        self.rodando = True

    def loop(self):
        while self.rodando:
            self.eventos()

            # Desenha pixel
            self.reta([100, 100], [200, 345], [255, 255, 255])
            self.circulo([100, 100], 100, [255, 255, 255])

            self.tela.blit(self.superficie, [0, 0])
            pygame.display.flip()

    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

    def reta(self, inicio, fim, cor):
        xi, yi = inicio
        xf, yf = fim

        for x in range(xi, xf + 1):
            m = (yf - yi) / (xf - xi)
            y = m * (x - xi) + yi

            self.superficie.set_at([x, int(y)], cor)

        for y in range(yi, yf + 1):
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

jogo = Jogo()
jogo.loop()
