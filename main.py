import pygame
import math

from vertice import *
from face import *
from tela import *

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
        # tela 1
        perguntas = [Face(self.superficie, [Vertice(200, 200), Vertice(250, 300)], BRANCO),
                     Face(self.superficie, [Vertice(250, 300), Vertice(300, 200)], BRANCO),
                     Face(self.superficie, [Vertice(300, 200), Vertice(350, 300)], BRANCO),
                     Face(self.superficie, [Vertice(350, 300), Vertice(400, 200)], BRANCO)]

        respostas = [Face(self.superficie, [Vertice(200, 200), Vertice(400, 200), Vertice(400, 400), Vertice(200, 400)], VERDE),
                     Face(self.superficie, [Vertice(400, 400), Vertice(200, 400), Vertice(300, 200)], VERDE)]
        resposta = 0

        tela = Tela(perguntas, respostas, resposta)
        self.telas.append(tela)

    def jogar(self):
        print("")

        while self.rodando:
            self.entrada()

            self.fluxo_do_jogo()

            self.telas[self.tela_atual].desenha()

            self.tela.blit(self.superficie, [0, 0])
            pygame.display.flip()

        print("Você acertou " + str(self.corretas) + " perguntas, seu QI é de: " + str(self.corretas * 10))

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
