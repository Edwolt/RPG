import pygame


class Jogo:
    def __init__(self):
        self.tab = [[None]]
        self.tam = None
        self.quad = 50, 50  # Dimensões do quadrado
        self.min = 15  # Número mínimo de quadrados (altura e largura)
        self.retorno = None

    def tamanho(self, tam):
        self.tam = tam
        quad = min(self.tam[0] // self.min, self.tam[1] // self.min)
        self.quad = quad, quad
        print(f'Quad_size:{quad}')
        self.tab = [
            [pygame.Surface(self.quad)] * (self.tam[1] // self.quad[1] + 1)
            for _ in range(self.tam[0] // self.quad[0] + 1)
        ]
        print(f'Tab: {len(self.tab)}x{len(self.tab[0])}')
        ret0 = self.quad[0] - self.tam[0] % self.quad[0]
        ret1 = self.quad[1] - self.tam[1] % self.quad[1]
        print(f"Retorno[0]: {self.tam[0]} % {self.quad[0]} = {ret0}")
        print(f"Retorno[1]: {self.tam[1]} % {self.quad[1]} = {ret1}")
        self.retorno = ret0 // 2, ret1 // 2
        print(f'Retorno: {self.retorno}')

    def surface(self):
        from random import randint
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                cor = randint(0, 255), randint(0, 255), randint(0, 255)
                self.tab[i][j] = pygame.Surface(self.quad)
                self.tab[i][j].fill(cor)

        tela = pygame.Surface(self.tam)

        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                pygame.transform.scale(self.tab[i][j], self.quad)
                tela.blit(self.tab[i][j], (self.quad[0] * i - self.retorno[0], self.quad[1] * j - self.retorno[1]))

        return tela
