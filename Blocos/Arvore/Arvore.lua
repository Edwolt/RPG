from Blocos.Bloco import Bloco
import pygame
from random import randint


class Bloco(Bloco):
    def __init__(self):
        self.num = randint(1, 2)
        self.colide = True

    def surface(self):
        return pygame.image.load(f'Blocos/Grama/{self.num}.png')
