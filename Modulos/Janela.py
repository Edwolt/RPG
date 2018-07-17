import pygame
from Telas.Jogo import Jogo


class Janela:
    def __init__(self):
        self.display = None
        self.tela = Jogo()
        self.fullscreen = False
        self.tam = 100, 100

    def tamanho(self, tam, fullscreen=False):
        self.tam = tam
        print(f'Resolução: {self.tam}' + ' Fullscreen' if fullscreen else '')
        if fullscreen:
            self.fullscreen = True
            self.display = pygame.display.set_mode(self.tam, pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode(self.tam, pygame.RESIZABLE)
        self.tela.tamanho(self.tam)

    def executar(self):
        self.display.blit(self.tela.surface(), (0, 0))
        self.eventos()
        pygame.display.flip()

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print('Quit: Fechar')
                quit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    print('Quit: <ESC>')
                    quit(0)
                if event.key == pygame.K_F11:
                    self.fullscreen = not self.fullscreen
                    self.tamanho(self.tam, self.fullscreen)
            if event.type == pygame.VIDEORESIZE:  # FIXME Não está Redimensionando corretamente
                self.tam = event.size
                self.tamanho(self.tam, self.fullscreen)
                self.tela.tamanho(self.tam)
