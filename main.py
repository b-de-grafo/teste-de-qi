import pygame
from objeto import *
import inputbox
from curva import bezier
from util import *

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
INPUT_ROTACAO_P1 = 1
INPUT_ROTACAO_P2 = 2
INPUT_ROTACAO_ANGULO = 3
RODANDO_ROTACAO = 4
INPUT_CURVA_P1 = 5
INPUT_CURVA_P2 = 6
INPUT_CURVA_P3 = 7
INPUT_CURVA_P4 = 8
RODANDO_CURVA = 9
RODANDO = 10
FIM_DE_JOGO = 11

# valores default pra facilitar os testes
DEFAULT_P1 = "0 300 0"
DEFAULT_P2 = "300 300 0"
DEFAULT_ANGULO = "3600"
DEFAULT_P1_CURVA = "100 400 15"
DEFAULT_P2_CURVA = "300 400 5"
DEFAULT_P3_CURVA = "100 200 0"
DEFAULT_P4_CURVA = "500 500 -10"


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.tamanho_tela = [600, 600]
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        self.superficie = pygame.Surface(self.tamanho_tela)
        self.fonte = pygame.font.SysFont("Arial", 25)

        # Fluxo do jogo
        self.rodando = True
        self.estado_do_jogo = INPUT_ROTACAO_P1

        # Quatérnios: Eixo de rotação e ângulo
        self.eixo = [(200, 200, 0), (300, 300, 0)]
        self.angulo_rotacao = 360

        # Curva Bezier
        self.pontos_curva = [[100, 400, 15], [300, 400, 5], [100, 200, 0], [500, 500, -10]]
        self.objetos, self.objetos_curva = self.monta_objetos()

        # Shading
        self.fonte_luz = (300, 300, 0)


    def monta_objetos(self):
        objetos = []
        objetos_curva = []
        p = 100 # profundidade do diamante 3D
        crazy_diamond = Objeto([Face(self.superficie,
                                     [[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 0, 1], [125.0, 1437.5, 0, 1],
                                      [41.666666666666664, 1250.0, 1, 1], [-41.666666666666664, 1437.5, 1, 1]],
                                     cor=VERMELHO,
                                     preenchido=True),
                                Face(self.superficie,
                                     [[0.0, 1500.0, p, 1], [83.33333333333333, 1500.0, p, 1], [125.0, 1437.5, p, 1],
                                      [41.666666666666664, 1250.0, p, 1], [-41.666666666666664, 1437.5, p, 1]],
                                     cor=AZUL,
                                     preenchido=True)])
        crazy_diamond = crazy_diamond.mapeamento_sru_srd(600, 1000, 600, 1500)
        crazy_diamond = crazy_diamond.translada_3d(280, 120, 0)
        crazy_diamond.rotacao = 30
        crazy_diamond.eixo = [(0,0,0),(0,1,0)]

        crazy_diamond = crazy_diamond.rotaciona_quaternio()


        curva_teste = bezier([0, 1], 0.01, self.pontos_curva, self.superficie, AZUL_PISCINA)

        # curva_teste = curva_teste.mapeamento_sru_srd(600, 1000, 600, 1500)
        # Seta o passo (em graus) e o eixo da rotação
        crazy_diamond.set_rotacao(0.5, self.eixo)

        objetos.append(crazy_diamond)
        objetos_curva.append(curva_teste)

        return objetos, objetos_curva

    def jogar(self):
        while self.rodando:
            self.entrada()

            self.desenha_tela()

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

                if self.estado_do_jogo == FIM_DE_JOGO:  # Qualquer tecla foi pressionada
                    self.proximo_estado()
                    break

                if self.estado_do_jogo == RODANDO_CURVA or self.estado_do_jogo == RODANDO_ROTACAO:
                    if key[pygame.K_SPACE]:  # Tecla ESPAÇO
                        self.proximo_estado()
                        break

                if self.estado_do_jogo == TELA_INICIAL:  # Qualquer tecla foi pressionada
                    self.proximo_estado()
                    break

    def proximo_estado(self):
        if self.estado_do_jogo == FIM_DE_JOGO:
            self.estado_do_jogo = TELA_INICIAL
        else:
            self.estado_do_jogo += 1

    def desenha_tela(self):
        self.superficie.fill(PRETO)

        if self.estado_do_jogo == TELA_INICIAL:
            mensagem = "Insira os dados do eixo e do ângulo de rotação"
            surface_msg = self.fonte.render(mensagem, False, BRANCO)
            self.superficie.blit(surface_msg, (100, 250))

        elif self.estado_do_jogo == INPUT_ROTACAO_P1:
            p1_string = inputbox.ask(self.tela, "Início do eixo (x1 y1 z1)", DEFAULT_P1)
            self.eixo[0] = parse_ponto(p1_string)

            self.proximo_estado()  # não foi chamada automaticamente porque a ask() capturou o evento do botão return

        elif self.estado_do_jogo == INPUT_ROTACAO_P2:
            p2_string = inputbox.ask(self.tela, "Fim do eixo (x2 y2 z2)", DEFAULT_P2)
            self.eixo[1] = parse_ponto(p2_string)

            self.proximo_estado()

        elif self.estado_do_jogo == INPUT_ROTACAO_ANGULO:
            angulo_string = inputbox.ask(self.tela, "Ângulo de rotação", DEFAULT_ANGULO)
            self.angulo_rotacao = parse_num(angulo_string)

            self.proximo_estado()

        elif self.estado_do_jogo == RODANDO_ROTACAO:
            for objeto in self.objetos:
                objeto.set_fonte_luz(self.fonte_luz) # passa fonte de luz do Jogo pro Objeto

                # Incrementa o angulo de rotação do objeto e retorna um novo polígono, não altera o mesmo
                if objeto.rotacao < self.angulo_rotacao:
                    objeto.inc_rotacao()

                objeto_rotacionado = objeto.rotaciona_quaternio()
                objeto_rotacionado.desenha()

            # Desenha eixo
            desenha_eixo(self.superficie, self.eixo[0], self.eixo[1], BRANCO, self.tamanho_tela)
            pygame.draw.circle(self.superficie, AMARELO, self.fonte_luz[:2], 15) # Fonte de luz


        elif self.estado_do_jogo == INPUT_CURVA_P1:
            self.superficie.fill(PRETO)
            ponto_string = inputbox.ask(self.tela, "P1 da curva", DEFAULT_P1_CURVA)
            self.pontos_curva[0] = parse_ponto(ponto_string)

            self.proximo_estado()

        elif self.estado_do_jogo == INPUT_CURVA_P2:
            ponto_string = inputbox.ask(self.tela, "P2 da curva", DEFAULT_P2_CURVA)
            self.pontos_curva[1] = parse_ponto(ponto_string)

            self.proximo_estado()
        
        elif self.estado_do_jogo == INPUT_CURVA_P3:
            ponto_string = inputbox.ask(self.tela, "P3 da curva", DEFAULT_P3_CURVA)
            self.pontos_curva[2] = parse_ponto(ponto_string)

            self.proximo_estado()
        
        elif self.estado_do_jogo == INPUT_CURVA_P4:
            ponto_string = inputbox.ask(self.tela, "P4 da curva", DEFAULT_P4_CURVA)
            self.pontos_curva[3] = parse_ponto(ponto_string)

            self.proximo_estado()


        elif self.estado_do_jogo == RODANDO_CURVA:
            pygame.draw.circle(self.superficie, AMARELO, self.fonte_luz[:2], 20) # Fonte de luz

            for objeto in self.objetos:
                objeto.set_fonte_luz(self.fonte_luz)
                indice_ponto = self.objetos_curva[0].get_curva_ind()
                curva = self.objetos_curva[0].faces[0].vertices
                # print(curva)
                # print(objeto.faces[0].vertices)
                translacao = []

                for i in range(4):
                    translacao.append(curva[indice_ponto][i] - objeto.faces[0].vertices[3][i])
                    # print(translacao)
                
                objeto_transladado = objeto.translada_3d(translacao[0], translacao[1], translacao[2])
                objeto_transladado.desenha()

            for objeto_curva in self.objetos_curva:
                objeto_curva.desenha()


jogo = Jogo()
jogo.jogar()

