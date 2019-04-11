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
        triangulo = Face(self.superficie, [Vertice(0, 247), Vertice(268, 247), Vertice(134, 17)]).desenha()
        quadrado = Face(self.superficie, [Vertice(0, 0), Vertice(268, 0), Vertice(268, 268), Vertice(0, 268)]).desenha()
        dodecagono = Face(self.superficie, [Vertice(0, 134), Vertice(18, 67), Vertice(67, 18), Vertice(134, 0), Vertice(201, 18), Vertice(250, 67), Vertice(268, 134), Vertice(250, 201), Vertice(201, 250), Vertice(134, 268), Vertice(67, 250), Vertice(18, 201)]).desenha()

        #Area das Respostas:
        areaPadrao =  [Desenho([Face(self.superficie, [Vertice(0, 450), Vertice(600,450)]),
                                Face(self.superficie, [Vertice(200, 450), Vertice(200, 600)]),
                                Face(self.superficie, [Vertice(400, 450), Vertice(400, 600)])])]

        # Tela 1
        perguntas = [Desenho([Face(self.superficie, [Vertice(200, 200), Vertice(250, 300)], BRANCO),
                             Face(self.superficie, [Vertice(250, 300), Vertice(300, 200)], BRANCO)]),
                     Desenho([Face(self.superficie, [Vertice(300, 200), Vertice(350, 300)], BRANCO),
                             Face(self.superficie, [Vertice(350, 300), Vertice(400, 200)], BRANCO)])]

        respostas = [Desenho([Face(self.superficie, [Vertice(200, 200), Vertice(400, 200), Vertice(400, 400), Vertice(200, 400)], VERDE)]),
                     Desenho([Face(self.superficie, [Vertice(400, 400), Vertice(200, 400), Vertice(300, 200)], VERDE).translada(100, 100)])]
        resposta = 1

        tela = Tela(perguntas, respostas, resposta, areaPadrao)
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
                if(pos[0] >= 0 and pos[0] < 200) and (pos[1] >= 450 and pos[1] <= 600):
                    self.resposta_do_jogador = 1
                if (pos[0] >= 200 and pos[0] < 400) and (pos[1] >= 450 and pos[1] <= 600):
                    self.resposta_do_jogador = 2
                if (pos[0] >= 400 and pos[0] < 600) and (pos[1] >= 450 and pos[1] <= 600):
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
