import pygame
from Modulos.Janela import Janela

pygame.init()
janela = Janela()
info = pygame.display.Info()
janela.tamanho((500, 500))
fps = 30
clock = pygame.time.Clock()


def eventos():
    """Verifique os eventos"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit(0)
            if event.key == pygame.K_F11:
                janela.fullscreen()
        if event.type == pygame.VIDEORESIZE:  # FIXME Não está Redimensionando corretamente
            self.tam = event.size
            self.tamanho(self.tam, self.fullscreen)
            self.tela.tamanho(self.tam)


while True:
    janela.executar()
    eventos()
    clock.tick(fps)
