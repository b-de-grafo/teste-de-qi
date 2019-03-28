import pygame


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


jogo = Jogo()
jogo.loop()
