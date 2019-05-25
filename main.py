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
        # TODOS OS DESENHOS DEVEM RESPEITAR Euler: Vertices – Arestas + Faces = 2

        # Desenhos 2D
        # triforce_de_viking = Face(self.superficie,
                                #   [[0, 0], [15, 24], [30, 0], [75, 96], [45, 96], [60, 120], [-30, 120], [-15, 96], [-45, 96]])
        triforce_de_viking = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [25.0, 1440.0, 1, 1], [50.0, 1500.0, 1, 1], [125.0, 1260.0, 1, 1], [75.0, 1260.0, 1, 1], [100.0, 1200.0, 1, 1], [-50.0, 1200.0, 1, 1], [-25.0, 1260.0, 1, 1], [-75.0, 1260.0, 1, 1]]), Face(self.superficie, [[0.0, 1500.0, 1, 1], [25.0, 1440.0, 1, 1], [50.0, 1500.0, 1, 1], [125.0, 1260.0, 1, 1], [75.0, 1260.0, 1, 1], [100.0, 1200.0, 1, 1], [-50.0, 1200.0, 1, 1], [-25.0, 1260.0, 1, 1], [-75.0, 1260.0, 1, 1]])])

        #raio = Face(self.superficie,
        #            [[0, 0], [20, 0], [15, 30], [50, 35], [0, 125], [10, 50], [-25, 50]])
        raio = Objeto([Face(self.superficie,[[0.0, 1500.0, 1, 1], [33.333333333333336, 1500.0, 1, 1], [25.0, 1425.0, 1, 1], [83.33333333333333, 1412.5, 1, 1], [0.0, 1187.5, 1, 1], [16.666666666666668, 1375.0, 1, 1], [-41.666666666666664, 1375.0, 1, 1]]),
                       Face(self.superficie,[[0.0, 1500.0, 1, 1], [33.333333333333336, 1500.0, 1, 1], [25.0, 1425.0, 1, 1], [83.33333333333333, 1412.5, 1, 1], [0.0, 1187.5, 1, 1], [16.666666666666668, 1375.0, 1, 1], [-41.666666666666664, 1375.0, 1, 1]])])
        #diamante = Face(self.superficie,
        #                [[0, 0], [50, 0], [75, 25], [25, 100], [-25, 25]])
        diamante = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 1, 1], [125.0, 1437.5, 1, 1], [41.666666666666664, 1250.0, 1, 1], [-41.666666666666664, 1437.5, 1, 1]]),
                           Face(self.superficie, [[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 1, 1], [125.0, 1437.5, 1, 1], [41.666666666666664, 1250.0, 1, 1], [-41.666666666666664, 1437.5, 1, 1]])])
        # cata_vento = Face(self.superficie,
        #                  [[0, 0], [25, 25], [25, 50], [50, 50], [25, 75], [0, 75], [0, 100], [-25, 75], [-25, 50], [-50, 50], [-25, 25], [0, 25]])
        cata_vento = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [41.666666666666664, 1437.5, 1, 1], [41.666666666666664, 1375.0, 1, 1], [83.33333333333333, 1375.0, 1, 1], [41.666666666666664, 1312.5, 1, 1], [0.0, 1312.5, 1, 1], [0.0, 1250.0, 1, 1], [-41.666666666666664, 1312.5, 1, 1], [-41.666666666666664, 1375.0, 1, 1], [-83.33333333333333, 1375.0, 1, 1], [-41.666666666666664, 1437.5, 1, 1], [0.0, 1437.5, 1, 1]]),
                             Face(self.superficie, [[0.0, 1500.0, 1, 1], [41.666666666666664, 1437.5, 1, 1], [41.666666666666664, 1375.0, 1, 1], [83.33333333333333, 1375.0, 1, 1], [41.666666666666664, 1312.5, 1, 1], [0.0, 1312.5, 1, 1], [0.0, 1250.0, 1, 1], [-41.666666666666664, 1312.5, 1, 1], [-41.666666666666664, 1375.0, 1, 1], [-83.33333333333333, 1375.0, 1, 1], [-41.666666666666664, 1437.5, 1, 1], [0.0, 1437.5, 1, 1]])])
        # cruz = Face(self.superficie,
        #            [[0, 0], [50, 0], [50, 50], [100, 50], [100, 100], [50, 100], [50, 150], [0, 150], [0, 100], [-50, 100], [-50, 50], [0, 50]])
        cruz = Objeto([Face(self.superficie,[[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 1, 1], [83.33333333333333, 1375.0, 1, 1], [166.66666666666666, 1375.0, 1, 1], [166.66666666666666, 1250.0, 1, 1], [83.33333333333333, 1250.0, 1, 1], [83.33333333333333, 1125.0, 1, 1], [0.0, 1125.0, 1, 1], [0.0, 1250.0, 1, 1], [-83.33333333333333, 1250.0, 1, 1], [-83.33333333333333, 1375.0, 1, 1], [0.0, 1375.0, 1, 1]], preenchido=True),
                       Face(self.superficie,[[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 1, 1], [83.33333333333333, 1375.0, 1, 1], [166.66666666666666, 1375.0, 1, 1], [166.66666666666666, 1250.0, 1, 1], [83.33333333333333, 1250.0, 1, 1], [83.33333333333333, 1125.0, 1, 1], [0.0, 1125.0, 1, 1], [0.0, 1250.0, 1, 1], [-83.33333333333333, 1250.0, 1, 1], [-83.33333333333333, 1375.0, 1, 1], [0.0, 1375.0, 1, 1]])])
        # seta = Objeto([Face(self.superficie, [[0, 0, 1, 1], [75, 75, 1, 1], [0, 150, 1, 1], [0, 100, 1, 1], [-100, 100, 1, 1], [-100, 50, 1, 1], [0, 50, 1, 1]]),
        #               Face(self.superficie, [[0, 0, 1, 1], [75, 75, 1, 1], [0, 150, 1, 1], [0, 100, 1, 1], [-100, 100, 1, 1], [-100, 50, 1, 1], [0, 50, 1, 1]])])
        seta = Objeto([Face(self.superficie,  [[0.0, 1500.0, 1, 1], [125.0, 1312.5, 1, 1], [0.0, 1125.0, 1, 1], [0.0, 1250.0, 1, 1], [-166.66666666666666, 1250.0, 1, 1], [-166.66666666666666, 1375.0, 1, 1], [0.0, 1375.0, 1, 1]]),
                       Face(self.superficie,  [[0.0, 1500.0, 1, 1], [125.0, 1312.5, 1, 1], [0.0, 1125.0, 1, 1], [0.0, 1250.0, 1, 1], [-166.66666666666666, 1250.0, 1, 1], [-166.66666666666666, 1375.0, 1, 1], [0.0, 1375.0, 1, 1]])])
        # bandeira = bandeira = Face(self.superficie,
        #                         [[0, 0], [100, 0], [50, 50], [100, 100], [0, 100], [-75, 50]])
        bandeira = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [166.66666666666666, 1500.0, 1, 1], [83.33333333333333, 1375.0, 1, 1], [166.66666666666666, 1250.0, 1, 1], [0.0, 1250.0, 1, 1], [-125.0, 1375.0, 1, 1]]),
                           Face(self.superficie, [[0.0, 1500.0, 1, 1], [166.66666666666666, 1500.0, 1, 1], [83.33333333333333, 1375.0, 1, 1], [166.66666666666666, 1250.0, 1, 1], [0.0, 1250.0, 1, 1], [-125.0, 1375.0, 1, 1]])])
        # dodecagono = Face(self.superficie,
                        #   [[0, 0], [18, -67], [67, -116], [134, -134], [201, -116], [250, -67], [268, 0], [250, 67], [201, 116], [134, 134], [67, 116], [18, 67]])
        dodecagono = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [30.0, 1667.5, 1, 1], [111.66666666666667, 1790.0, 1, 1], [223.33333333333334, 1835.0, 1, 1], [335.0, 1790.0, 1, 1], [416.6666666666667, 1667.5, 1, 1], [446.6666666666667, 1500.0, 1, 1], [416.6666666666667, 1332.5, 1, 1], [335.0, 1210.0, 1, 1], [223.33333333333334, 1165.0, 1, 1], [111.66666666666667, 1210.0, 1, 1], [30.0, 1332.5, 1, 1]]), Face(self.superficie, [[0.0, 1500.0, 1, 1], [30.0, 1667.5, 1, 1], [111.66666666666667, 1790.0, 1, 1], [223.33333333333334, 1835.0, 1, 1], [335.0, 1790.0, 1, 1], [416.6666666666667, 1667.5, 1, 1], [446.6666666666667, 1500.0, 1, 1], [416.6666666666667, 1332.5, 1, 1], [335.0, 1210.0, 1, 1], [223.33333333333334, 1165.0, 1, 1], [111.66666666666667, 1210.0, 1, 1], [30.0, 1332.5, 1, 1]])])

        # estrela = Face(self.superficie,
                        # [[0, 0], [15, 25], [50, 25], [25, 40], [35, 75], [0, 55], [-35, 75], [-25, 40], [-50, 25], [-15, 25]])
        estrela = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [25.0, 1437.5, 1, 1], [83.33333333333333, 1437.5, 1, 1], [41.666666666666664, 1400.0, 1, 1], [58.333333333333336, 1312.5, 1, 1], [0.0, 1362.5, 1, 1], [-58.333333333333336, 1312.5, 1, 1], [-41.666666666666664, 1400.0, 1, 1], [-83.33333333333333, 1437.5, 1, 1], [-25.0, 1437.5, 1, 1]]), Face(self.superficie, [[0.0, 1500.0, 1, 1], [25.0, 1437.5, 1, 1], [83.33333333333333, 1437.5, 1, 1], [41.666666666666664, 1400.0, 1, 1], [58.333333333333336, 1312.5, 1, 1], [0.0, 1362.5, 1, 1], [-58.333333333333336, 1312.5, 1, 1], [-41.666666666666664, 1400.0, 1, 1], [-83.33333333333333, 1437.5, 1, 1], [-25.0, 1437.5, 1, 1]])])

        # estrela_de_davi = Face(self.superficie,
                            #    [[0, 0], [15, 25], [50, 25], [25, 50], [50, 75], [15, 75], [0, 100], [-15, 75], [-50, 75], [-25, 50], [-50, 25], [-15, 25]])
        estrela_de_davi = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [25.0, 1437.5, 1, 1], [83.33333333333333, 1437.5, 1, 1], [41.666666666666664, 1375.0, 1, 1], [83.33333333333333, 1312.5, 1, 1], [25.0, 1312.5, 1, 1], [0.0, 1250.0, 1, 1], [-25.0, 1312.5, 1, 1], [-83.33333333333333, 1312.5, 1, 1], [-41.666666666666664, 1375.0, 1, 1], [-83.33333333333333, 1437.5, 1, 1], [-25.0, 1437.5, 1, 1]]), Face(self.superficie, [[0.0, 1500.0, 1, 1], [25.0, 1437.5, 1, 1], [83.33333333333333, 1437.5, 1, 1], [41.666666666666664, 1375.0, 1, 1], [83.33333333333333, 1312.5, 1, 1], [25.0, 1312.5, 1, 1], [0.0, 1250.0, 1, 1], [-25.0, 1312.5, 1, 1], [-83.33333333333333, 1312.5, 1, 1], [-41.666666666666664, 1375.0, 1, 1], [-83.33333333333333, 1437.5, 1, 1], [-25.0, 1437.5, 1, 1]])])

        # Desenhos 3D
        p = 100
        crazy_diamond = Objeto([Face(self.superficie, [[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 1, 1], [125.0, 1437.5, 1, 1], [41.666666666666664, 1250.0, 1, 1], [-41.666666666666664, 1437.5, 1, 1]], cor=VERMELHO, preenchido=True),
                                Face(self.superficie, [[0.0, 1500.0, p, 1], [83.33333333333333, 1500.0, p, 1], [125.0, 1437.5, p, 1], [41.666666666666664, 1250.0, p, 1], [-41.666666666666664, 1437.5, p, 1]], cor=AZUL, preenchido=True)])
        crazy_diamond = crazy_diamond.mapeamento_sru_srd(600, 1000, 600, 1500)

        # Area das Respostas:
        area_padrao = [Desenho([Face(self.superficie, [[0, 450], [600, 450]]),
                                Face(self.superficie, [[200, 450], [200, 600]]),
                                Face(self.superficie, [[400, 450], [400, 600]])])]

        # Tela 00
        # Desenhar a figura 3D do seu grupo como wire-frame em projecao isometrica na tela inicial de abertura do seu teste de QI
        # Projecao isometrica: teta_y = 45 graus e teta_x = 35,26
        perguntas = [crazy_diamond.translada_3d(150, 80, 0).rotaciona_y(radians(10)).rotaciona_x(radians(10)).escala_3d(2, 2, 2),
                     crazy_diamond.translada_3d(100, 100, 0).rotaciona_y_ponto(radians(45)).rotaciona_x_ponto(radians(35.26)),
                     crazy_diamond.translada_3d(400, 450, 0).rotaciona_y_ponto(radians(45)).rotaciona_x_ponto(radians(35.26)).escala_3d_ponto(1.5, 1.5, 1.5)]


        tela = Tela(perguntas, [], 1, [])
        self.telas.append(tela)

        # Tela 01
        perguntas = [crazy_diamond.translada_3d(50, 50, 0),
                     crazy_diamond.translada_3d(225, 50, 0).rotaciona_y_ponto(radians(30)),
                     crazy_diamond.translada_3d(320, 50, 0).rotaciona_y_ponto(radians(-30)),
                     crazy_diamond.translada_3d(500, 50, 0).rotaciona_y_ponto(radians(210))]

        tela = Tela(perguntas, [], 1, [])
        self.telas.append(tela)

        # IMPORTANTE: ROTACAO 2D = ROTACAO Z
        # Tela 1
        # Ideia: poligonos rotacionados de acordo com sua posicao na matriz
        # multiplicado por 90 graus se for seta e 180 graus se for bandeira
        seta = seta.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(325, 150, 0)
        bandeira = bandeira.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(500, 175, 0)
        perguntas = [Desenho([seta.escala_3d_ponto(0.7, 0.7, 0.7).translada_3d(-225, -100, 0).muda_cor(VERMELHO),
                              seta.escala_3d_ponto(0.7, 0.7, 0.7).translada_3d(-40, -100, 0).rotaciona_z_ponto(radians((0 + 1) * 90), ind_ponto=3).muda_cor(VERMELHO),
                              seta.escala_3d_ponto(0.7, 0.7, 0.7).translada_3d(150, -125, 0).rotaciona_z_ponto(radians((0 + 2) * 90), ind_ponto=3).muda_cor(VERMELHO)]),
                     Desenho([bandeira.escala_3d_ponto(0.7, 0.7, 0.7).rotaciona_z_ponto(radians(180), ind_ponto=0).translada_3d(-525, 100, 0).rotaciona_z_ponto(radians((1 + 0) * 180), ind_ponto=5).muda_cor(VERDE),
                              bandeira.escala_3d_ponto(0.7, 0.7, 0.7).rotaciona_z_ponto(radians(180), ind_ponto=0).translada_3d(-190, 98, 0).rotaciona_z_ponto(radians((1 + 1) * 180), ind_ponto=5).muda_cor(VERDE),
                              bandeira.escala_3d_ponto(0.7, 0.7, 0.7).rotaciona_z_ponto(radians(180), ind_ponto=0).translada_3d(-130, 100, 0).rotaciona_z_ponto(radians((1 + 2) * 180), ind_ponto=5).muda_cor(VERDE)]),
                     Desenho([seta.escala_3d_ponto(0.7, 0.7, 0.7).translada_3d(-250, 125, 0).rotaciona_z_ponto(radians((2 + 0) * 90), ind_ponto=3).muda_cor(AZUL),
                              seta.escala_3d_ponto(0.7, 0.7, 0.7).translada_3d(-5, 135, 0).rotaciona_z_ponto(radians((2 + 1) * 90), ind_ponto=3).muda_cor(AZUL)])]

        respostas = [Desenho([seta.escala_3d_ponto(0.7, 0.7, 0.7).translada_3d(-220, 320, 0).rotaciona_z_ponto(radians((2 + 2) * 90), ind_ponto=3).muda_cor(AZUL)]),
                     Desenho([seta.escala_3d_ponto(0.7, 0.7, 0.7).translada_3d(-40, 320, 0).rotaciona_z_ponto(radians((2 + 3) * 90), ind_ponto=3).muda_cor(AZUL)]),
                     Desenho([seta.escala_3d_ponto(0.7, 0.7, 0.7).translada_3d(150, 290, 0).rotaciona_z_ponto(radians((2 + 4) * 90), ind_ponto=3).muda_cor(AZUL)])]

        resposta = 1

        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # Tela 2
        raio = raio.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(225, 0, 0)
        diamante = diamante.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(375, 0, 0)
        dodecagono = dodecagono.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(0, 466, 0)
        estrela_de_davi = estrela_de_davi.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(450, 425, 0)
        estrela = estrela.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(350, 325, 0)

        perguntas = [Desenho([estrela_de_davi.translada_3d(-350, -400, 0).escala_3d_ponto(1.5, 1.5, 0).muda_cor(VERDE),
                              estrela.escala_3d_ponto(0.7, 0.7, 0).translada_3d(-250, -260, 0).muda_cor(AMARELO)]),
                     Desenho([estrela_de_davi.translada_3d(-150, -400, 0).escala_3d_ponto(1.5, 1.5, 0).muda_cor(VERDE),
                              raio.escala_3d_ponto(0.5, 0.5, 0.5).translada_3d(70, 75, 0).muda_cor(VERMELHO)]),
                     Desenho([estrela_de_davi.translada_3d(50, -400, 0).escala_3d_ponto(1.5, 1.5, 0).muda_cor(VERDE),
                              diamante.escala_3d_ponto(0.5, 0.5, 0.5).translada_3d(112, 75, 0).muda_cor(AZUL)]),
                     Desenho([dodecagono.translada_3d(35, -195, 0).escala_3d_ponto(0.5, 0.5, 0.5).muda_cor(AZUL_PISCINA),
                              diamante.escala_3d_ponto(0.5, 0.5, 0.5).translada_3d(-287, 245, 0).muda_cor(AZUL)]),
                     Desenho([dodecagono.translada_3d(235, -195, 0).escala_3d_ponto(0.5, 0.5, 0.5).muda_cor(AZUL_PISCINA),
                              raio.escala_3d_ponto(0.5, 0.5, 0.5).translada_3d(70, 245, 0).muda_cor(VERMELHO)])]

        respostas = [Desenho([dodecagono.translada_3d(35, 60, 0).escala_3d_ponto(0.5, 0.5, 0.5).muda_cor(AZUL_PISCINA),
                              diamante.escala_3d_ponto(0.5, 0.5, 0.5).translada_3d(-287, 500, 0).muda_cor(AZUL)]),
                     Desenho([estrela_de_davi.translada_3d(-150, 25, 0).escala_3d_ponto(1.5, 1.5, 0).muda_cor(VERDE),
                              raio.escala_3d_ponto(0.5, 0.5, 0.5).translada_3d(70, 500, 0).muda_cor(VERMELHO)]),
                     Desenho([dodecagono.translada_3d(435, 60, 0).escala_3d_ponto(0.5, 0.5, 0.5).muda_cor(AZUL_PISCINA),
                              estrela.escala_3d_ponto(0.7, 0.7, 0).translada_3d(150, 170, 0).muda_cor(AMARELO)])]

        resposta = 3

        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # Tela 3
        cata_vento = cata_vento.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(550, 0, 0)
        cruz = cruz.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(100, 150, 0)
        perguntas = [Desenho([cata_vento.rotaciona_z_ponto(radians(45)).escala_3d_ponto(1.5, 1.5, 1.5).translada_3d(-382, 35, 0).muda_cor(AMARELO)]),
                     Desenho([cruz.rotaciona_z_ponto(radians(45)).escala_3d_ponto(0.8, 0.8, 0.8).translada_3d(232, -120, 0).muda_cor(AMARELO)]),
                     Desenho([cruz.rotaciona_z_ponto(radians(45)).escala_3d_ponto(0.8, 0.8, 0.8).translada_3d(432, -120, 0).muda_cor(AMARELO),
                              cata_vento.rotaciona_z_ponto(radians(225)).escala_3d_ponto(1.5, 1.5, 1.5).translada_3d(-100, 150, 0).muda_cor(AMARELO)]),
                     Desenho([cata_vento.escala_3d_ponto(1.5, 1.5, 1.5).translada_3d(-445, 185, 0).muda_cor(VERDE)]),
                     Desenho([cruz.escala_3d_ponto(0.8, 0.8, 0.8).translada_3d(185, 55, 0).muda_cor(VERDE)])]

        respostas = [Desenho([cruz.rotaciona_z_ponto(radians(45)).escala_3d_ponto(0.8, 0.8, 0.8).translada_3d(25, 310, 0).muda_cor(VERDE),
                              cata_vento.rotaciona_z_ponto(radians(225)).escala_3d_ponto(1.5, 1.5, 1.5).translada_3d(-507, 580, 0).muda_cor(VERDE)]),
                     Desenho([cruz.rotaciona_z_ponto(radians(45)).escala_3d_ponto(0.8, 0.8, 0.8).translada_3d(432, 325, 0).muda_cor(VERDE),
                              cruz.escala_3d_ponto(0.8, 0.8, 0.8).translada_3d(385, 310, 0).muda_cor(VERDE)]),
                     Desenho([cata_vento.escala_3d_ponto(1.5, 1.5, 1.5).translada_3d(-245, 450, 0).muda_cor(VERDE),
                              cruz.escala_3d_ponto(0.8, 0.8, 0.8).translada_3d(185, 310, 0).muda_cor(VERDE)])]

        resposta = 2

        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # Tela 4
        triforce_de_viking = triforce_de_viking.mapeamento_sru_srd(600, 1000, 600, 1500).translada_3d(45, 0, 0)

        perguntas = [Desenho([triforce_de_viking.translada_3d(35, 10, 0)]),
                     Desenho([bandeira.translada_3d(-210, -140, 0).escala_3d_ponto(0.8, 0.8, 0.8).muda_cor(AZUL)]),
                     Desenho([triforce_de_viking.translada_3d(395, 10, 0).cisalha_3d_ponto(0.6, 0).muda_cor(AZUL_PISCINA)]),
                     Desenho([triforce_de_viking.translada_3d(35, 175, 0)]),
                     Desenho([bandeira.translada_3d(-210, 20, 0).escala_3d_ponto(0.5, 0.8, 0.5).muda_cor(AZUL)]),
                     Desenho([triforce_de_viking.translada_3d(420, 175, 0).cisalha_3d_ponto(0.35, 0).muda_cor(AZUL_PISCINA)]),
                     Desenho([triforce_de_viking.translada_3d(35, 320, 0)]),
                     Desenho([bandeira.translada_3d(-215, 170, 0).escala_3d_ponto(1.1, 0.8, 1.1).muda_cor(AZUL)])]

        respostas = [Desenho([triforce_de_viking.translada_3d(100, 465, 0).cisalha_3d_ponto(-0.8, 0).muda_cor(AZUL_PISCINA)]),
                     Desenho([triforce_de_viking.translada_3d(180, 465, 0).cisalha_3d_ponto(0.8, 0).muda_cor(AZUL_PISCINA)]),
                     Desenho([triforce_de_viking.translada_3d(420, 465, 0).cisalha_3d_ponto(0.2, 0).muda_cor(AZUL_PISCINA)])]

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
