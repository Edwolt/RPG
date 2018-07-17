from Blocos.Bloco import Bloco
import pygame
from random import randint


class Grama(Bloco):
    def __init__(self):
        self.num = randint(0, 1)

    def surface(self):
        return pygame.image.load(f'Blocos/Grama/{self.num}.png')
