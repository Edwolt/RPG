import pygame
import threading


class Loop:
    def __init__(self, janela, fps=0):
        self.clock_l = pygame.time.Clock()
        self.clock_g = pygame.time.Clock()
        self.janela = janela
        self.fps = fps

    def executar(self):
        """Dispara Threads"""
        while True:
            self.eventos()
            self.janela.executar()

    def eventos(self):
        """Verifique os eventos"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit(0)
                if event.key == pygame.K_F11:  # FIXME não se deve ter métodos concorrenco
                    self.janela.fullscreen()
            if event.type == pygame.VIDEORESIZE:  # FIXME não se deve ter métodos concorrenco
                self.janela.resize(event.size)
