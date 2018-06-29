import pygame
from Modulos.Janela import Janela
import Modulos.Eventos as Eventos

pygame.init()
janela = Janela()
# janela.tamanho()

while True:
    janela.exibir()
    Eventos.eventos()
