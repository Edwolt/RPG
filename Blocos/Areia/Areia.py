from Blocos.Bloco import Bloco
import pygame
from random import randint


class Areia(Bloco):
    def __init__(self):
        self.num = randint(1, 2)

    def surface(self):
        return pygame.image.load(f'Blocos/Grama/{self.num}.png')
