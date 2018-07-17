import pygame
from Modulos.Janela import Janela

print('Inicio')
pygame.init()
janela = Janela()
info = pygame.display.Info()
janela.tamanho((info.current_w, info.current_h), fullscreen=True)
fps = 30
print(f'FPS: {fps}')
clock = pygame.time.Clock()
print('Game Loop')

while True:
    janela.executar()
    clock.tick(fps)
