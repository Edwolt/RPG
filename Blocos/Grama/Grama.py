from Blocos.Bloco import Bloco
import pygame
from random import randint

NUM_FRAME = 3
VEL = 10


class Flor(Bloco):
    def __init__(self):
        self.frame = 0
        print('Hoje está muito florido')
        self.d = 1

    def surface(self) -> pygame.Surface:
        self.frame += self.d
        if self.frame == NUM_FRAME * VEL - 1 or self.frame == 0:
            self.d *= -1
            self.frame += VEL * self.d
        return pygame.image.load(f'Blocos/Grama/Flor{self.frame // VEL}.png')


class Grama(Bloco):
    def surface(self) -> pygame.Surface:
        return pygame.image.load(f'Blocos/Grama/Grama.png')


def Bloco():
    if randint(0, 24) == 0:
        return Flor()
    else:
        return Grama()
