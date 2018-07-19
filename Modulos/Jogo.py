import pygame
from Modulos.Mapa import Mapa
from Personagens.Principal.Principal import Principal


class Jogo:
    def __init__(self):
        self.dtab = 1, 1
        self.tab = [[None]]
        self.tam = None
        self.quad = 50, 50  # Dimensões do quadrado
        self.min = 10  # Número mínimo de quadrados (altura e largura)
        self.retorno = None
        self.mapa = Mapa('Teste', (15, 15))
        self.principal = Principal()
        self.cprincipal = 1, 1

    def tamanho(self, tam: tuple):
        """
        Redimensione a Janela
        :param tam: (largura, altura)
        """
        self.tam = tam

        quad = min(self.tam[0] // self.min, self.tam[1] // self.min)
        self.quad = quad, quad

        self.dtab = self.tam[0] // self.quad[0] + 1, self.tam[1] // self.quad[1] + 1
        self.cprincipal = self.dtab[0] // 2, self.dtab[1] // 2

        ret0 = self.quad[0] - self.tam[0] % self.quad[0]
        ret1 = self.quad[1] - self.tam[1] % self.quad[1]
        self.retorno = ret0 // 2, ret1 // 2

        self.tab = self.mapa.mapa(self.dtab)

    def movimento(self):  # TODO
        self.tab = self.mapa.mapa(self.dtab)
        pass

    def surface(self) -> pygame.Surface:
        """
        Gera uma Surface contendo a imagem a ser jogada na tela
        :return:Surface gerada com imagens renderizadas
        """

        tela = pygame.Surface(self.tam)

        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                sur = pygame.transform.scale(self.tab[i][j].surface(), self.quad)
                tela.blit(sur, (self.quad[0] * i - self.retorno[0], self.quad[1] * j - self.retorno[1]))

        sur = pygame.transform.scale(self.principal.surface(), self.quad)
        coord0 = self.quad[0] * self.cprincipal[0] - self.retorno[0]
        coord1 = self.quad[1] * self.cprincipal[1] - self.retorno[1]
        tela.blit(sur, (coord0, coord1))
        tela.blit(sur, (coord0, coord1))
        return tela
