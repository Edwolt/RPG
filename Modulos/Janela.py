import pygame
from Telas.Jogo import Jogo


class Janela:
    def __init__(self):
        self.display = None
        self.tela = Jogo()

    def tamanho(self, largura, altura, fullscreen=False):
        if fullscreen:
            self.display = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode((largura, altura))
        print(self.display.__class__)
        self.tela.tamanho(largura, altura)

    def executar(self):
        self.display.blit(self.tela.surface(), (0, 0))
        self.eventos()
        pygame.display.flip()

    def eventos(self):
        """Analisará eventos"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit(0)
