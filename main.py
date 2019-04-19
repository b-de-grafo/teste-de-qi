import pygame
from math import pi, radians
from face import *
from tela import *
from desenho import *

BRANCO = [255, 255, 255]
VERMELHO = [255, 0, 0]
VERDE = [0, 255, 0]
PRETO = [0, 0, 0]

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
        self.tela_atual = 0

        self.resposta_do_jogador = None
        self.tempo_inicial = pygame.time.get_ticks()
        self.tempo_de_resposta = 0

        self.corretas = 0

    def monta_telas(self):
        # Alguns polígonos pra começar
        # triforceDeViking = Face(self.superficie, [[45, 0], [60, 24], [75, 0], [120, 96], [90, 96], [105, 120], [15, 120], [30, 96], [0, 96]]).desenha()
        raio = Face(self.superficie, [[225, 0], [245, 0], [240, 30], [275, 35], [225, 125], [235, 50], [200, 50]], preenchido=True)
        diamante = Face(self.superficie, [[375, 0], [425, 0], [450, 25], [400, 100], [350, 25]])
        # cataVento = Face(self.superficie, [[550, 0], [575, 25], [575, 50], [600, 50], [575, 75], [550, 75], [550, 100], [525, 75], [525, 50], [500, 50], [525, 25], [550, 25]]).desenha()
        # cruz = Face(self.superficie, [[100, 150], [150, 150], [150, 200], [200, 200], [200, 250], [150, 250], [150, 300], [100, 300], [100, 250], [50, 250], [50, 200], [100, 200]]).desenha()
        seta = Face(self.superficie,
                    [[325, 150], [400, 225], [325, 300], [325, 250], [225, 250], [225, 200], [325, 200]], BRANCO)
        bandeiraEsquisitaDeFestaJunina = Face(self.superficie,
                                              [[500, 175], [600, 175], [550, 225], [600, 275], [500, 275], [425, 225]],
                                              BRANCO)
        dodecagono = Face(self.superficie, [[0, 466], [18, 399], [67, 350], [134, 332], [201, 350], [250, 399], [268, 466], [250, 533], [201, 582], [134, 600], [67, 582], [18, 533]])
        estrela = Face(self.superficie, [[350, 325], [365, 350], [400, 350], [375, 365], [385, 400], [350, 380], [315, 400], [325, 365], [300, 350], [335, 350]])
        estrelaDaviVsGolias = Face(self.superficie, [[450, 425], [465, 450], [500, 450], [475, 475], [500, 500], [465, 500], [450, 525], [435, 500], [400, 500], [425, 475], [400, 450], [435, 450]])

        # estrelaDaviVsGolias.cisalhamento_ponto(1, 0, 0).desenha()
        # estrelaDaviVsGolias.rotaciona_ponto(radians(90), 2).desenha()
        # estrelaDaviVsGolias.escala(1, 0.5).desenha()
        # estrelaDaviVsGolias.rotaciona(radians(15)).desenha()
        # estrelaDaviVsGolias.translada(50).desenha()
        # estrelaDaviVsGolias.translada(0, 50).desenha()
        # estrelaDaviVsGolias.translada(50, 50).desenha()

        # Area das Respostas:
        area_padrao = [Desenho([Face(self.superficie, [[0, 450], [600, 450]]),
                                Face(self.superficie, [[200, 450], [200, 600]]),
                                Face(self.superficie, [[400, 450], [400, 600]])])]

        # Tela 1 #Ideia: poligonos rotacionados de acordo com sua posicao na matriz vezes 90 graus se seta, 180 graus se bandeirola
        perguntas = [Desenho([seta.escala_no_ponto(0.7, 0.7).translada(-225, -100),
                              seta.escala_no_ponto(0.7, 0.7).translada(-40, -100).rotaciona_no_ponto(radians((0 + 1) * 90), 3),
                              seta.escala_no_ponto(0.7, 0.7).translada(150, -125).rotaciona_no_ponto(radians((0 + 2) * 90), 3),
                              ]),
                     Desenho([bandeiraEsquisitaDeFestaJunina.escala_no_ponto(0.7, 0.7).rotaciona_no_ponto(radians(180))
                                                                                   .translada(-525, 100)
                                                                                   .rotaciona_no_ponto(radians((1 + 0) * 180), 5),
                              bandeiraEsquisitaDeFestaJunina.escala_no_ponto(0.7, 0.7).rotaciona_no_ponto(radians(180))
                                                                                   .translada(-190, 98)
                                                                                   .rotaciona_no_ponto(radians((1 + 1) * 180), 5),
                              bandeiraEsquisitaDeFestaJunina.escala_no_ponto(0.7, 0.7).rotaciona_no_ponto(radians(180))
                                                                                   .translada(-130, 100)
                                                                                   .rotaciona_no_ponto(radians((1 + 2) * 180), 5),
                              ]),
                     Desenho(
                         [seta.escala_no_ponto(0.7, 0.7).translada(-250, 125).rotaciona_no_ponto(radians((2 + 0) * 90), 3),
                          seta.escala_no_ponto(0.7, 0.7).translada(-5, 135).rotaciona_no_ponto(radians((2 + 1) * 90), 3),
                          #seta.escala_ponto(0.7, 0.7).translada(0, 200).rotaciona_ponto(radians((2 + 2) * 90), 3)
                          ])]

        respostas = [Desenho([seta.escala_no_ponto(0.7, 0.7).translada(-220, 320).rotaciona_no_ponto(radians((2 + 2) * 90), 3)]),
                     Desenho([seta.escala_no_ponto(0.7, 0.7).translada(-40, 320).rotaciona_no_ponto(radians((2 + 3) * 90), 3)]),
                     Desenho([seta.escala_no_ponto(0.7, 0.7).translada(150, 290).rotaciona_no_ponto(radians((2 + 4) * 90), 3)]),
                     ]

        resposta = 1

        # tela = Tela(perguntas, respostas, resposta, area_padrao)
        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # Tela 2
        #Estrelas -> x [300 a 400] y [ 325 a 400]
        #Estrelas de Davi -> x [400 a 500] y [ 425 a 525 ]
        perguntas = [Desenho([estrelaDaviVsGolias.translada(-350, -400).escala_no_ponto(1.5, 1.5, 0),
                              estrela.escala_no_ponto(0.7, 0.7, 0).translada(-250, -260)]),
                     Desenho([estrelaDaviVsGolias.translada(-150, -400).escala_no_ponto(1.5, 1.5, 0),
                              raio.escala_no_ponto(0.5, 0.5, 0).translada(70, 75)]),
                     Desenho([estrelaDaviVsGolias.translada(50, -400).escala_no_ponto(1.5, 1.5, 0),
                              diamante.escala_no_ponto(0.5, 0.5, 0).translada(112, 75)]),
                     Desenho([dodecagono.translada(35, -195).escala_no_ponto(0.5, 0.5, 0),
                              diamante.escala_no_ponto(0.5, 0.5, 0).translada(-287, 245)]),
                     Desenho([dodecagono.translada(235, -195).escala_no_ponto(0.5, 0.5, 0),
                              raio.escala_no_ponto(0.5, 0.5, 0).translada(70, 245)])
                     ]

        respostas = [Desenho([dodecagono.translada(35, 60).escala_no_ponto(0.5, 0.5, 0),
                              diamante.escala_no_ponto(0.5, 0.5, 0).translada(-287, 500)]),
                     Desenho([estrelaDaviVsGolias.translada(-150, 25).escala_no_ponto(1.5, 1.5, 0),
                              raio.escala_no_ponto(0.5, 0.5, 0).translada(70, 500)]),
                     Desenho([dodecagono.translada(435, 60).escala_no_ponto(0.5, 0.5, 0),
                              estrela.escala_no_ponto(0.7, 0.7, 0).translada(150, 170)]),
                     ]

        resposta = 3

        tela = Tela(perguntas, respostas, resposta, area_padrao)
        self.telas.append(tela)

        # TODO: criar telas seguintes

    def jogar(self):
        print("")

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
                    if key[pygame.K_4]:  # Tecla 4
                        self.resposta_do_jogador = 4
                    if key[pygame.K_5]:  # Tecla 5
                        self.resposta_do_jogador = 5

                if self.estado_do_jogo == TELA_INICIAL:
                    self.estado_do_jogo = JOGANDO

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

            self.superficie.blit(surface_msg, (70, 250))
        elif self.estado_do_jogo == JOGANDO:
            self.telas[self.tela_atual].desenha()
        elif self.estado_do_jogo == FIM_DE_JOGO:
            mensagem = "Você acertou %d pergunta%s em %.1f segundos!" % (self.corretas,
                                                                                "" if self.corretas == 1 else "s",
                                                                                self.tempo_de_resposta)
            mensagem2 = "Seu QI é:"
            qi = "%.0f" % ((self.corretas * 10) * (10 / self.tempo_de_resposta))
            surface_msg = self.fonte.render(mensagem, False, BRANCO)
            surface_msg2 = self.fonte.render(mensagem2, False, BRANCO)
            surface_qi = self.fonte.render(qi, False, BRANCO)

            self.superficie.blit(surface_msg, (65, 150))
            self.superficie.blit(surface_msg2, (175, 200))
            self.superficie.blit(surface_qi, (290, 200))


jogo = Jogo()
jogo.jogar()
