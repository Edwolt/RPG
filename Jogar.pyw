import pygame
from Modulos.Janela import Janela
from Modulos import Loop

pygame.init()

janela = Janela()
info = pygame.display.Info()
janela.tamanho((500, 500))

fps = 30

Loop.janela = janela
Loop.fps = fps
Loop.executar()
