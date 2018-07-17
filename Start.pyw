import pygame
from Modulos.Janela import Janela

pygame.init()
janela = Janela()
info = pygame.display.Info()
janela.tamanho((info.current_w, info.current_h), fullscreen=True)
fps = 30
clock = pygame.time.Clock()

while True:
    janela.executar()
    clock.tick(fps)
