import pygame
import time
from face import *
from tela import *
from desenho import *
from objeto import *

BRANCO = [255, 255, 255]
VERMELHO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
AMARELO = [255, 255, 0]
AZUL_PISCINA = [0, 255, 255]
PRETO = [0, 0, 0]
# Descomente a linha abaixo pra deixar todas as figuras brancas
# VERMELHO = VERDE = AZUL = AMARELO = AZUL_PISCINA = BRANCO

TELA_INICIAL = 0
JOGANDO = 1
FIM_DE_JOGO = 2


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.tamanho_tela = [600, 600]
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        self.superficie = pygame.Surface(self.tamanho_tela)

        self.fonte = pygame.font.SysFont("Arial", 25)

        self.rodando = True

        self.telas = []
        #self.monta_telas_debug_preenche()
        self.monta_telas()

        self.estado_do_jogo = TELA_INICIAL

    def inicializa_jogo(self):
        self.estado_do_jogo = JOGANDO

        self.tela_atual = 0

        self.tempo_inicial = pygame.time.get_ticks()
        self.resposta_do_jogador = None
        self.tempo_de_resposta = 0

        self.corretas = 0

    def monta_telas_debug_preenche(self):
        raio = Objeto([Face(self.superficie,
                            [[0.0, 1500.0, 1, 1], [33.333333333333336, 1500.0, 1, 1], [25.0, 1425.0, 1, 1],
                             [83.33333333333333, 1412.5, 1, 1], [0.0, 1187.5, 1, 1], [16.666666666666668, 1375.0, 1, 1],
                             [-41.666666666666664, 1375.0, 1, 1]], preenchido=True, tela=self.tela),
                       Face(self.superficie,
                            [[0.0, 1500.0, 1, 1], [33.333333333333336, 1500.0, 1, 1], [25.0, 1425.0, 1, 1],
                             [83.33333333333333, 1412.5, 1, 1], [0.0, 1187.5, 1, 1], [16.666666666666668, 1375.0, 1, 1],
                             [-41.666666666666664, 1375.0, 1, 1]], preenchido=True, tela=self.tela)])

        raio = raio.mapeamento_sru_srd(600, 1000, 600, 1500)
        raio = raio.translada_3d(200, 200, 0)
        perguntas = [raio]

        tela = Tela(perguntas, [], 1, [])
        self.telas.append(tela)


    def monta_telas(self):
        p = 100
        crazy_diamond = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 1, 1], [125.0, 1437.5, 1, 1], [41.666666666666664, 1250.0, 1, 1], [-41.666666666666664, 1437.5, 1, 1]], cor=VERMELHO, preenchido=False),
                                Face(self.superficie, [[0.0, 1500.0, p, 1], [83.33333333333333, 1500.0, p, 1], [125.0, 1437.5, p, 1], [41.666666666666664, 1250.0, p, 1], [-41.666666666666664, 1437.5, p, 1]], cor=AZUL, preenchido=False)])
        crazy_diamond = crazy_diamond.mapeamento_sru_srd(600, 1000, 600, 1500)

        # Tela Única
        self.eixo = ((0, 0, 0), (1, 1, 0))

        eixo = (self.eixo[1][0]-self.eixo[0][0], self.eixo[1][1]-self.eixo[0][1], self.eixo[1][2]-self.eixo[0][2])
        perguntas = [crazy_diamond.translada_3d(280, 120, 0),
                     crazy_diamond.translada_3d(280, 120, 0).rotaciona_quaternio(30, eixo=eixo)]
        tela = Tela(perguntas, [], 1, [])
        self.telas.append(tela)

        # Tela de resposta - objetos 3D que serão desenhados
        self.objetos_finais = []

    def jogar(self):
        while self.rodando:
            self.entrada()

            self.fluxo_do_jogo()


            self.desenha_telas()

            self.tela.blit(self.superficie, [0, 0])
            pygame.display.flip()

    def entrada(self):
        key = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar janela
                self.rodando = False

            if evento.type == pygame.KEYUP:
                if key[pygame.K_ESCAPE]:  # Tecla ESC
                    self.rodando = False

                if self.estado_do_jogo == JOGANDO:
                    if key[pygame.K_1]:  # Tecla 1
                        self.resposta_do_jogador = 1
                    if key[pygame.K_2]:  # Tecla 2
                        self.resposta_do_jogador = 2
                    if key[pygame.K_3]:  # Tecla 3
                        self.resposta_do_jogador = 3

                if self.estado_do_jogo == TELA_INICIAL:  # Qualquer tecla foi pressionada
                    self.inicializa_jogo()

                if self.estado_do_jogo == FIM_DE_JOGO:
                    self.estado_do_jogo = TELA_INICIAL

            if evento.type == pygame.MOUSEBUTTONUP:
                if self.estado_do_jogo == JOGANDO:
                    pos = pygame.mouse.get_pos()
                    if (0 <= pos[0] < 200) and (450 <= pos[1] <= 600):
                        self.resposta_do_jogador = 1
                    if (200 <= pos[0] < 400) and (450 <= pos[1] <= 600):
                        self.resposta_do_jogador = 2
                    if (400 <= pos[0] < 600) and (450 <= pos[1] <= 600):
                        self.resposta_do_jogador = 3

    def fluxo_do_jogo(self):
        if self.estado_do_jogo == JOGANDO and self.resposta_do_jogador is not None:
            if self.resposta_do_jogador == self.telas[self.tela_atual].correta:
                self.corretas += 1
            self.resposta_do_jogador = None
            self.tela_atual += 1

            if self.tela_atual == len(self.telas):
                self.estado_do_jogo = FIM_DE_JOGO
                self.tempo_de_resposta = (pygame.time.get_ticks() - self.tempo_inicial) / 1000

    def desenha_telas(self):
        self.superficie.fill(PRETO)

        if self.estado_do_jogo == TELA_INICIAL:
            mensagem = "Pressione qualquer tecla para iniciar o teste!"
            surface_msg = self.fonte.render(mensagem, False, BRANCO)

            self.superficie.blit(surface_msg, (100, 250))
        elif self.estado_do_jogo == JOGANDO:
            self.telas[self.tela_atual].desenha()
            desenha_eixo(self.superficie, self.eixo[0], self.eixo[1], BRANCO, self.tamanho_tela)
        elif self.estado_do_jogo == FIM_DE_JOGO:
            mensagem1 = "Você acertou %d pergunta%s em %.1f segundos!" % (self.corretas,
                                                                          "" if self.corretas == 1 else "s",
                                                                          self.tempo_de_resposta)
            mensagem2 = "Seu QI é: "
            qi = "%.0f" % ((self.corretas * 25) + (30 * (10 / self.tempo_de_resposta)))
            mensagem3 = "Pressione qualquer tecla para voltar à tela inicial"

            surface_msg1 = self.fonte.render(mensagem1, False, BRANCO)
            surface_msg2 = self.fonte.render(mensagem2 + qi, False, BRANCO)
            surface_msg3 = self.fonte.render(mensagem3, False, BRANCO)

            for objeto in self.objetos_finais:
                objeto.translada_3d(0, 400, 0).desenha(rotaciona_y=False)

            self.superficie.blit(surface_msg1, (110, 150))
            self.superficie.blit(surface_msg2, (230, 200))
            self.superficie.blit(surface_msg3, (90, 350))

            time.sleep(0.3)


jogo = Jogo()
jogo.jogar()
