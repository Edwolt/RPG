import pygame
from Blocos.Grama.Grama import Grama


class Janela:
    def __init__(self):
        self.tela = pygame.display.set_mode((500, 500))
        self.tabela = [[Grama() for _ in range(10)] for _ in range(10)]

    def exibir(self):
        for i in range(10):
            for j in range(10):
                self.tela.blit(self.tabela[i][j].surface(), (50 * i, 50 * j))
        pygame.display.flip()
