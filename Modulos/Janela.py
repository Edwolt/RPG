import pygame
from Modulos.Jogo import Jogo


class Janela:
    def __init__(self):
        self.display = None
        self.tela = Jogo()
        self.__fullscreen = False
        self.tam = 100, 100

    def tamanho(self, tam, fullscreen=False):
        """
        Redimensione a tela
        :param tam: (largura, altura)
        :param fullscreen: Defina se será exibido em Full Screen
        """
        self.tam = tam
        print(f'Resolução: {self.tam}' + ' Fullscreen' if fullscreen else '')
        if fullscreen:
            self.__fullscreen = True
            self.display = pygame.display.set_mode(self.tam, pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode(self.tam, pygame.RESIZABLE)
        self.tela.tamanho(self.tam)

    def executar(self):
        """Atualize tela e verifiva eventos"""
        self.display.blit(self.tela.surface(), (0, 0))
        pygame.display.flip()

    def fullscreen(self):
        self.__fullscreen = not self.__fullscreen
        self.tamanho(self.tam, self.__fullscreen)

    def resize(self, size):  # FIXME Não está Redimensionando corretamente
        self.tam = size
        self.tamanho(self.tam, self.__fullscreen)
        self.tela.tamanho(self.tam)
