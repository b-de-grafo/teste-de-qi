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
        self.monta_telas()

        self.estado_do_jogo = TELA_INICIAL

    def inicializa_jogo(self):
        self.estado_do_jogo = JOGANDO

        self.tela_atual = 0

        self.tempo_inicial = pygame.time.get_ticks()
        self.resposta_do_jogador = None
        self.tempo_de_resposta = 0

        self.corretas = 0

    def monta_telas(self):

        # TODOS OS DESENHOS DEVEM RESPEITAR Euler: Vertices – Arestas + Faces = 2
        # DESENHOS OK: crazy_diamond
        # DESENHOS NOT OK: resto


        #IMPORTANTE, O SISTEMA DE COORDENADAS UTILIZADO DEVE SER O UNIVERSAL E DEPOIS MAPEAR PARA O DO DISPOSITVO QUANDO FOR DESENHADO
        # Desenhos 2D
        triforce_de_viking = Face(self.superficie,
                                  [[0, 0], [15, 24], [30, 0], [75, 96], [45, 96], [60, 120], [-30, 120], [-15, 96], [-45, 96]])
        raio = Face(self.superficie,
                    [[0, 0], [20, 0], [15, 30], [50, 35], [0, 125], [10, 50], [-25, 50]])
        diamante = Face(self.superficie,
                        [[0, 0], [50, 0], [75, 25], [25, 100], [-25, 25]])
        cata_vento = Face(self.superficie,
                          [[0, 0], [25, 25], [25, 50], [50, 50], [25, 75], [0, 75], [0, 100], [-25, 75], [-25, 50], [-50, 50], [-25, 25], [0, 25]])
        cruz = Face(self.superficie,
                    [[0, 0], [50, 0], [50, 50], [100, 50], [100, 100], [50, 100], [50, 150], [0, 150], [0, 100], [-50, 100], [-50, 50], [0, 50]])
        seta = Face(self.superficie,
                    [[0, 0], [75, 75], [0, 150], [0, 100], [-100, 100], [-100, 50], [0, 50]])
        bandeira = Face(self.superficie,
                        [[0, 0], [100, 0], [50, 50], [100, 100], [0, 100], [-75, 50]])
        dodecagono = Face(self.superficie,
                          [[0, 0], [18, -67], [67, -116], [134, -134], [201, -116], [250, -67], [268, 0], [250, 67], [201, 116], [134, 134], [67, 116], [18, 67]])
        estrela = Face(self.superficie,
                        [[0, 0], [15, 25], [50, 25], [25, 40], [35, 75], [0, 55], [-35, 75], [-25, 40], [-50, 25], [-15, 25]])
        estrela_de_davi = Face(self.superficie,
                               [[0, 0], [15, 25], [50, 25], [25, 50], [50, 75], [15, 75], [0, 100], [-15, 75], [-50, 75], [-25, 50], [-50, 25], [-15, 25]])

        # Desenhos 3D
        crazy_diamond = Objeto([Face(self.superficie, [[0, 0, 1, 1], [50, 0, 1, 1], [75, 25, 1, 1], [25, 100, 1, 1], [-25, 25, 1, 1]]),
                                Face(self.superficie, [[0, 0, 100, 1], [50, 0, 100, 1], [75, 25, 100, 1], [25, 100, 100, 1], [-25, 25, 100, 1]])])

        # Area das Respostas:
        area_padrao = [Desenho([Face(self.superficie, [[0, 450], [600, 450]]),
                                Face(self.superficie, [[200, 450], [200, 600]]),
                                Face(self.superficie, [[400, 450], [400, 600]])])]

        # Tela 0
        # Desenhar a figura 3D do seu grupo como wire-frame em projecao isometrica na tela inicial de abertura do seu teste de QI
        # Projecao isometrica: teta_y = 45 graus e teta_x = 35,26
        perguntas = [crazy_diamond.translada_3d(150, 80, 0).rotaciona_y(radians(45)).rotaciona_x(radians(35.26)).escala_tresde(2,2,2).muda_cor(AZUL_PISCINA)]


        tela = Tela(perguntas, [], 1, [])
        self.telas.append(tela)
        # Tela 1
        # Ideia: poligonos rotacionados de acordo com sua posicao na matriz
        # multiplicado por 90 graus se for seta e 180 graus se for bandeira
        seta = seta.translada(325, 150)
        bandeira = bandeira.translada(500, 175)
        perguntas = [Desenho([seta.escala_no_ponto(0.7, 0.7).translada(-225, -100).muda_cor(VERMELHO),
                              seta.escala_no_ponto(0.7, 0.7).translada(-40, -100).rotaciona_no_ponto(radians((0 + 1) * 90), 3).muda_cor(VERMELHO),
                              seta.escala_no_ponto(0.7, 0.7).translada(150, -125).rotaciona_no_ponto(radians((0 + 2) * 90), 3).muda_cor(VERMELHO)]),
                     Desenho([bandeira.escala_no_ponto(0.7, 0.7).rotaciona_no_ponto(radians(180)).translada(-525, 100).rotaciona_no_ponto(radians((1 + 0) * 180), 5).muda_cor(VERDE),
                              bandeira.escala_no_ponto(0.7, 0.7).rotaciona_no_ponto(radians(180)).translada(-190, 98).rotaciona_no_ponto(radians((1 + 1) * 180), 5).muda_cor(VERDE),
                              bandeira.escala_no_ponto(0.7, 0.7).rotaciona_no_ponto(radians(180)).translada(-130, 100).rotaciona_no_ponto(radians((1 + 2) * 180), 5).muda_cor(VERDE)]),
                     Desenho([seta.escala_no_ponto(0.7, 0.7).translada(-250, 125).rotaciona_no_ponto(radians((2 + 0) * 90), 3).muda_cor(AZUL),
                              seta.escala_no_ponto(0.7, 0.7).translada(-5, 135).rotaciona_no_ponto(radians((2 + 1) * 90), 3).muda_cor(AZUL)])]

        respostas = [Desenho([seta.escala_no_ponto(0.7, 0.7).translada(-220, 320).rotaciona_no_ponto(radians((2 + 2) * 90), 3).muda_cor(AZUL)]),
                     Desenho([seta.escala_no_ponto(0.7, 0.7).translada(-40, 320).rotaciona_no_ponto(radians((2 + 3) * 90), 3).muda_cor(AZUL)]),
                     Desenho([seta.escala_no_ponto(0.7, 0.7).translada(150, 290).rotaciona_no_ponto(radians((2 + 4) * 90), 3).muda_cor(AZUL)])]

        resposta = 1

        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # Tela 2
        raio = raio.translada(225, 0)
        diamante = diamante.translada(375, 0)
        dodecagono = dodecagono.translada(0, 466)
        estrela_de_davi = estrela_de_davi.translada(450, 425)
        estrela = estrela.translada(350, 325)
        perguntas = [Desenho([estrela_de_davi.translada(-350, -400).escala_no_ponto(1.5, 1.5, 0).muda_cor(VERDE),
                              estrela.escala_no_ponto(0.7, 0.7, 0).translada(-250, -260).muda_cor(AMARELO)]),
                     Desenho([estrela_de_davi.translada(-150, -400).escala_no_ponto(1.5, 1.5, 0).muda_cor(VERDE),
                              raio.escala_no_ponto(0.5, 0.5, 0).translada(70, 75).muda_cor(VERMELHO)]),
                     Desenho([estrela_de_davi.translada(50, -400).escala_no_ponto(1.5, 1.5, 0).muda_cor(VERDE),
                              diamante.escala_no_ponto(0.5, 0.5, 0).translada(112, 75).muda_cor(AZUL)]),
                     Desenho([dodecagono.translada(35, -195).escala_no_ponto(0.5, 0.5, 0).muda_cor(AZUL_PISCINA),
                              diamante.escala_no_ponto(0.5, 0.5, 0).translada(-287, 245).muda_cor(AZUL)]),
                     Desenho([dodecagono.translada(235, -195).escala_no_ponto(0.5, 0.5, 0).muda_cor(AZUL_PISCINA),
                              raio.escala_no_ponto(0.5, 0.5, 0).translada(70, 245).muda_cor(VERMELHO)])]

        respostas = [Desenho([dodecagono.translada(35, 60).escala_no_ponto(0.5, 0.5, 0).muda_cor(AZUL_PISCINA),
                              diamante.escala_no_ponto(0.5, 0.5, 0).translada(-287, 500).muda_cor(AZUL)]),
                     Desenho([estrela_de_davi.translada(-150, 25).escala_no_ponto(1.5, 1.5, 0).muda_cor(VERDE),
                              raio.escala_no_ponto(0.5, 0.5, 0).translada(70, 500).muda_cor(VERMELHO)]),
                     Desenho([dodecagono.translada(435, 60).escala_no_ponto(0.5, 0.5, 0).muda_cor(AZUL_PISCINA),
                              estrela.escala_no_ponto(0.7, 0.7, 0).translada(150, 170).muda_cor(AMARELO)])]

        resposta = 3

        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # Tela 3
        cata_vento = cata_vento.translada(550, 0)
        cruz = cruz.translada(100, 150)
        perguntas = [Desenho([cata_vento.rotaciona_no_ponto(radians(45)).escala_no_ponto(1.5, 1.5, 0).translada(-382, 35).muda_cor(AMARELO)]),
                     Desenho([cruz.rotaciona_no_ponto(radians(45)).escala_no_ponto(0.8, 0.8, 0).translada(232, -120).muda_cor(AMARELO)]),
                     Desenho([cruz.rotaciona_no_ponto(radians(45)).escala_no_ponto(0.8, 0.8, 0).translada(432, -120).muda_cor(AMARELO),
                              cata_vento.rotaciona_no_ponto(radians(225)).escala_no_ponto(1.5, 1.5, 0).translada(-100, 150).muda_cor(AMARELO)]),
                     Desenho([cata_vento.escala_no_ponto(1.5, 1.5, 0).translada(-445, 185).muda_cor(VERDE)]),
                     Desenho([cruz.escala_no_ponto(0.8, 0.8, 0).translada(185, 55).muda_cor(VERDE)])]

        respostas = [Desenho([cruz.rotaciona_no_ponto(radians(45)).escala_no_ponto(0.8, 0.8, 0).translada(25, 310).muda_cor(VERDE),
                              cata_vento.rotaciona_no_ponto(radians(225)).escala_no_ponto(1.5, 1.5, 0).translada(-507, 580).muda_cor(VERDE)]),
                     Desenho([cruz.rotaciona_no_ponto(radians(45)).escala_no_ponto(0.8, 0.8, 0).translada(432, 325).muda_cor(VERDE),
                              cruz.escala_no_ponto(0.8, 0.8, 0).translada(385, 310).muda_cor(VERDE)]),
                     Desenho([cata_vento.escala_no_ponto(1.5, 1.5, 0).translada(-245, 450).muda_cor(VERDE),
                              cruz.escala_no_ponto(0.8, 0.8, 0).translada(185, 310).muda_cor(VERDE)])]

        resposta = 2

        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # Tela 4
        triforce_de_viking = triforce_de_viking.translada(45, 0)
        perguntas = [Desenho([triforce_de_viking.translada(35, 10)]),
                     Desenho([bandeira.translada(-210, -140).escala_no_ponto(0.8, 0.8).muda_cor(AZUL)]),
                     Desenho([triforce_de_viking.translada(395, 10).cisalha_no_ponto(0.6, 0).muda_cor(AZUL_PISCINA)]),
                     Desenho([triforce_de_viking.translada(35, 175)]),
                     Desenho([bandeira.translada(-210, 20).escala_no_ponto(0.5, 0.8).muda_cor(AZUL)]),
                     Desenho([triforce_de_viking.translada(420, 175).cisalha_no_ponto(0.35, 0).muda_cor(AZUL_PISCINA)]),
                     Desenho([triforce_de_viking.translada(35, 320)]),
                     Desenho([bandeira.translada(-215, 170).escala_no_ponto(1.1, 0.8).muda_cor(AZUL)])]

        respostas = [Desenho([triforce_de_viking.translada(100, 465).cisalha_no_ponto(-0.8, 0).muda_cor(AZUL_PISCINA)]),
                     Desenho([triforce_de_viking.translada(180, 465).cisalha_no_ponto(0.8, 0).muda_cor(AZUL_PISCINA)]),
                     Desenho([triforce_de_viking.translada(420, 465).cisalha_no_ponto(0.2, 0).muda_cor(AZUL_PISCINA)])]

        resposta = 2

        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # Objetos finais que rotacionam
        self.objetos_finais = [crazy_diamond.rotaciona_y(radians(10)).translada_3d(400, 450, 0)]

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
                objeto.desenha(rotaciona_y=True)

            self.superficie.blit(surface_msg1, (110, 150))
            self.superficie.blit(surface_msg2, (230, 200))
            self.superficie.blit(surface_msg3, (90, 350))

            time.sleep(0.3)


jogo = Jogo()
jogo.jogar()
