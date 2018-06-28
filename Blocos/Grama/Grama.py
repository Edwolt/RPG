import pygame
from random import randint


class Grama:
    def __init__(self):
        self.num = randint(1,2)

    def surface(self):
        return pygame.image.load(f'Blocos/Grama/{self.num}.png')
