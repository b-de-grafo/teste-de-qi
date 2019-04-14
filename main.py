import pygame
from math import pi,radians
from face import *
from tela import *
from desenho import *

BRANCO = [255, 255, 255]
VERMELHO = [255, 0, 0]
VERDE = [0, 255, 0]
PRETO = [0, 0, 0]


class Jogo:
    def __init__(self):
        pygame.init()

        self.tamanho_tela = [600, 600]
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        self.superficie = pygame.Surface(self.tamanho_tela)

        self.rodando = True

        self.telas = []
        self.monta_telas()

        self.tela_atual = 0

        self.resposta_do_jogador = -1

        self.corretas = 0

    def monta_telas(self):
        # Alguns polígonos pra começar
        triangulo = Face(self.superficie, [[100, 0], [150, 100], [50, 100]]).desenha()
        quadrado = Face(self.superficie, [[200, 0], [300, 0], [300, 100], [200, 100]]).desenha()
        pentagono = Face(self.superficie, [[400, 0], [450, 25], [450, 100], [350, 100], [350, 25]]).desenha()
        hexagono = Face(self.superficie, [[550, 0], [600, 25], [600, 75], [550, 100], [500, 75], [500, 25]]).desenha()
        cruz = Face(self.superficie, [[100, 150], [150, 150], [150, 200], [200, 200], [200, 250], [150, 250], [150, 300], [100, 300], [100, 250], [50, 250], [50, 200], [100, 200]]).desenha()
        seta = Face(self.superficie, [[325, 150], [400, 225], [325, 300], [325, 250], [225, 250], [225, 200], [325, 200]]).desenha()
        bandeiraEsquisitaDeFestaJunina = Face(self.superficie, [[500, 175], [600, 175], [550, 225], [600, 275], [500, 275], [425, 225]]).desenha()
        dodecagono = Face(self.superficie, [[0, 466], [18, 399], [67, 350], [134, 332], [201, 350], [250, 399], [268, 466], [250, 533], [201, 582], [134, 600], [67, 582], [18, 533]]).desenha()
        estrela = Face(self.superficie, [[350, 325], [365, 350], [400, 350], [375, 365], [385, 400], [350, 380], [315, 400], [325, 365], [300, 350], [335, 350]]).desenha()
        estrelaDaviVsGolias = Face(self.superficie, [[450, 425], [465, 450], [500, 450], [475, 475], [500, 500], [465, 500], [450, 525], [435, 500], [400, 500], [425, 475], [400, 450], [435, 450]])
        estrelaDaviVsGolias.desenha()
#        estrelaDaviVsGolias.escala(1, 0.5).desenha()
        #estrelaDaviVsGolias.rotaciona(radians(15)).desenha()
        #estrelaDaviVsGolias.translada(50).desenha()
        #estrelaDaviVsGolias.translada(0, 50).desenha()
        #estrelaDaviVsGolias.translada(50, 50).desenha()


        # Area das Respostas:
        area_padrao = [Desenho([Face(self.superficie, [[0, 450], [600, 450]]),
                                Face(self.superficie, [[200, 450], [200, 600]]),
                                Face(self.superficie, [[400, 450], [400, 600]])])]

        # Tela 1
        perguntas = [Desenho([Face(self.superficie, [[200, 200], [250, 300]], BRANCO),
                             Face(self.superficie, [[250, 300], [300, 200]], BRANCO)]),
                     Desenho([Face(self.superficie, [[300, 200], [350, 300]], BRANCO),
                             Face(self.superficie, [[350, 300], [400, 200]], BRANCO)])]

        respostas = [Desenho([Face(self.superficie, [[200, 200], [400, 200], [400, 400], [200, 400]], VERDE)]),
                     Desenho([Face(self.superficie, [[400, 400], [200, 400], [300, 200]], VERDE)])]
        resposta = 1

        #tela = Tela(perguntas, respostas, resposta, area_padrao)
        tela = Tela([], [], resposta, [])
        self.telas.append(tela)

        # TODO: criar telas seguintes

    def jogar(self):
        print("")

        while self.rodando:
            self.entrada()

            self.fluxo_do_jogo()

            self.telas[self.tela_atual].desenha()

            self.tela.blit(self.superficie, [0, 0])
            pygame.display.flip()

        print("Você acertou " + str(self.corretas) + " perguntas, seu QI é: " + str(self.corretas * 10))

    def entrada(self):
        key = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if key[pygame.K_ESCAPE]:  # Tecla ESC
                self.rodando = False

            if key[pygame.K_1]:  # Tecla 1
                self.resposta_do_jogador = 1
            if key[pygame.K_2]:  # Tecla 2
                self.resposta_do_jogador = 2
            if key[pygame.K_3]:  # Tecla 3
                self.resposta_do_jogador = 3
            if key[pygame.K_4]:  # Tecla 4
                self.resposta_do_jogador = 4
            if key[pygame.K_5]:  # Tecla 5
                self.resposta_do_jogador = 5

            if evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(0 <= pos[0] < 200) and (450 <= pos[1] <= 600):
                    self.resposta_do_jogador = 1
                if (200 <= pos[0] < 400) and (450 <= pos[1] <= 600):
                    self.resposta_do_jogador = 2
                if (400 <= pos[0] < 600) and (450 <= pos[1] <= 600):
                    self.resposta_do_jogador = 3

            if evento.type == pygame.QUIT:  # Fechar janela
                self.rodando = False

    def fluxo_do_jogo(self):
        if self.resposta_do_jogador != -1:
            if self.resposta_do_jogador == self.telas[self.tela_atual].correta:
                print("Acertou\n")
                self.corretas += 1
            else:
                print("Errou\n")

            if self.tela_atual == len(self.telas) - 1:
                print("Fim de jogo")
                self.rodando = False
            else:
                self.tela_atual += 1


jogo = Jogo()
jogo.jogar()
