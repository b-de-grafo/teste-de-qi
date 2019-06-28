import pygame
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
RODANDO = 1
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

        # Seta o eixo de rotação do programa
        self.eixo = ((0, 200, 0), (500, 500, 0))
        self.objetos = self.monta_objetos()

        self.estado_do_jogo = TELA_INICIAL

    def monta_objetos(self):
        objetos = []
        eixo = (self.eixo[1][0]-self.eixo[0][0], self.eixo[1][1]-self.eixo[0][1], self.eixo[1][2]-self.eixo[0][2])

        p = 100
        crazy_diamond = Objeto([Face(self.superficie,
                                     [[0.0, 1500.0, 1, 1], [83.33333333333333, 1500.0, 1, 1], [125.0, 1437.5, 1, 1],
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
        # Seta o paço e o eixo da rotação
        crazy_diamond.set_rotacao(0.5, eixo)

        objetos.append(crazy_diamond)

        return objetos

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
                    if key[pygame.K_SPACE]:  # Tecla ESPACO
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
            mensagem = "Digite no terminal os pontos do eixo na ordem (x1, y1, z1), (x2, y2, z2)"
            surface_msg = self.fonte.render(mensagem, False, BRANCO)

            self.superficie.blit(surface_msg, (100, 250))
            # input()
        elif self.estado_do_jogo == RODANDO:
            # Desenha polígono
            for objeto in self.objetos:
                # Incrementa o angulo de rotação do objeto e retorna um novo polígono, não altera o mesmo
                objeto_rotacionado = objeto.inc_rotacao()
                # Tentei fazer essa transalação pra corrigir o problema dele rodar meio longe do eixo mas não deu certo
                # objeto_rotacionado = objeto_rotacionado.translada_3d(self.eixo[0][0], self.eixo[0][1], self.eixo[0][2]
                objeto_rotacionado.desenha()
            # Desenha eixo
            desenha_eixo(self.superficie, self.eixo[0], self.eixo[1], BRANCO, self.tamanho_tela)


jogo = Jogo()
jogo.jogar()
