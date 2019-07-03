import pygame
from objeto import *
import inputbox
from curva import bezier

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
TELA_INPUT_P1 = 1
TELA_INPUT_P2 = 2
TELA_INPUT_ANGULO = 3
RODANDO = 4
FIM_DE_JOGO = 5

# valores default pra facilitar os testes
DEFAULT_P1 = "0 300 0"
DEFAULT_P2 = "300 300 0"
DEFAULT_ANGULO = "3600"


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.tamanho_tela = [600, 600]
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        self.superficie = pygame.Surface(self.tamanho_tela)
        self.fonte = pygame.font.SysFont("Arial", 25)

        self.rodando = True

        # Inicializa o eixo de rotação do programa e o ângulo
        self.eixo = [(200, 200, 0), (300, 300, 0)]
        self.angulo_rotacao = 360

        self.objetos,self.objetos_curva = self.monta_objetos()

        self.estado_do_jogo = TELA_INPUT_P1

    def monta_objetos(self):
        objetos = []
        objetos_curva = []
        p = 100
        crazy_diamond = Objeto([Face(self.superficie,
                                     [[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 0, 1], [125.0, 1437.5, 0, 1],
                                      [41.666666666666664, 1250.0, 1, 1], [-41.666666666666664, 1437.5, 1, 1]],
                                     cor=VERMELHO,
                                     preenchido=False),
                                Face(self.superficie,
                                     [[0.0, 1500.0, p, 1], [83.33333333333333, 1500.0, p, 1], [125.0, 1437.5, p, 1],
                                      [41.666666666666664, 1250.0, p, 1], [-41.666666666666664, 1437.5, p, 1]],
                                     cor=AZUL,
                                     preenchido=False)])
        crazy_diamond = crazy_diamond.mapeamento_sru_srd(600, 1000, 600, 1500)
        crazy_diamond = crazy_diamond.translada_3d(280, 120, 0)
        crazy_diamond.rotacao = 30
        crazy_diamond.eixo = [(0,0,0),(0,1,0)]
        crazy_diamond = crazy_diamond.rotaciona_quaternio()

        curva_teste = bezier([0, 1], 0.01, [[100, 400, 15], [300, 400, 5], [100, 200, 0], [500, 500, -10]], self.superficie, AZUL_PISCINA)

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

                if self.estado_do_jogo == RODANDO:
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
            # self.superficie.blit(surface_msg, (100, 250))

        elif self.estado_do_jogo == TELA_INPUT_P1:
            # input do primeiro ponto do eixo
            # mensagem = "Primeiro ponto do eixo:"
            # surface_msg = self.fonte.render(mensagem, False, BRANCO)
            # self.superficie.blit(surface_msg, (100, 250))
            
            p1_string = inputbox.ask(self.tela, "Ponto inicial (x1 y1 z1)", DEFAULT_P1)
            self.eixo[0] = parse_ponto(p1_string)

            self.proximo_estado()  # não foi chamada automaticamente porque a ask() capturou o evento do botão return

        elif self.estado_do_jogo == TELA_INPUT_P2:
            # input do segundo ponto do eixo
            # mensagem = "Segundo ponto do eixo:"
            # surface_msg = self.fonte.render(mensagem, False, BRANCO)
            # self.superficie.blit(surface_msg, (100, 250))

            p2_string = inputbox.ask(self.tela, "Ponto final (x2 y2 z2)", DEFAULT_P2)
            self.eixo[1] = parse_ponto(p2_string)

            self.proximo_estado()

        elif self.estado_do_jogo == TELA_INPUT_ANGULO:
            # input do ângulo de rotação
            # mensagem = "Ângulo de rotação:"
            # surface_msg = self.fonte.render(mensagem, False, BRANCO)
            # self.superficie.blit(surface_msg, (100, 250))

            angulo_string = inputbox.ask(self.tela, "Ângulo de rotação", DEFAULT_ANGULO)
            self.angulo_rotacao = parse_num(angulo_string)

            self.proximo_estado()

        elif self.estado_do_jogo == RODANDO:

            # Desenha polígono
            for objeto in self.objetos:
                # Incrementa o angulo de rotação do objeto e retorna um novo polígono, não altera o mesmo
                indice_ponto = self.objetos_curva[0].get_curva_ind()
                curva = self.objetos_curva[0].faces[0].vertices
                print(curva)
                print(objeto.faces[0].vertices)
                translacao = []
                for i in range(4):
                    translacao.append(curva[indice_ponto][i] - objeto.faces[0].vertices[3][i])
                    print(translacao)
                objeto_transladado = objeto.translada_3d(translacao[0], translacao[1], translacao[2])
                objeto_transladado.desenha()
                #if objeto.rotacao < self.angulo_rotacao:
                #    objeto.inc_rotacao()
                #objeto_rotacionado = objeto.rotaciona_quaternio()
                #objeto_rotacionado.desenha()
            for objeto_curva in self.objetos_curva:
                objeto_curva.desenha()
            # Desenha eixo
            #desenha_eixo(self.superficie, self.eixo[0], self.eixo[1], BRANCO, self.tamanho_tela)


jogo = Jogo()
jogo.jogar()

