import pygame
from Modulos.Janela import Janela
from Modulos.Loop import Loop

pygame.init()

janela = Janela()
info = pygame.display.Info()
janela.tamanho({x = 500, y = 500}, nil)

fps = 30

loop = Loop(janela, fps)
loop.executar()
