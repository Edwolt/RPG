import pygame
from Modulos.Mapa import Mapa


class Jogo:
    def __init__(self):
        self.dtab = 1, 1
        self.tam = None
        self.quad = 50, 50  # Dimensões do quadrado
        self.min = 15  # Número mínimo de quadrados (altura e largura)
        self.retorno = None
        self.mapa = Mapa('Teste', (15, 15))

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

    def movimento(self):  # TODO
        pass

    def surface(self) -> pygame.Surface:
        """
        Gera uma Surface contendo a imagem a ser jogada na tela
        :return:Surface gerada com imagens renderizadas
        """
        tab, personagens = self.mapa.get(self.dtab)
        tela = pygame.Surface(self.tam)

        for i in range(len(tab)):
            for j in range(len(tab[i])):
                sur = pygame.transform.scale(tab[i][j].surface(), self.quad)
                tela.blit(sur, (self.quad[0] * i - self.retorno[0], self.quad[1] * j - self.retorno[1]))

        for personagem in personagens:
            per, coord = personagem
            sur = pygame.transform.scale(per.surface(), self.quad)
            pos0 = self.quad[0] * coord[0] - self.retorno[0]
            pos1 = self.quad[1] * coord[1] - self.retorno[1]
            tela.blit(sur, (pos0, pos1))

        return tela
