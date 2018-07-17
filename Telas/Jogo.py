import pygame


class Jogo:
    def __init__(self):
        self.tabela = [[None]]
        self.tam = None
        self.quad = 50, 50  # Dimensões do quadrado
        self.min = 15  # Número mínimo de quadrados (altura e largura)
        self.retorno = None

    def tamanho(self, largura, altura):
        self.tam = largura, altura
        quad = min(self.tam[0] // self.min, self.tam[1] // self.min)
        self.quad = quad, quad
        self.tabela = [
            [pygame.Surface(self.quad)] * (self.tam[1] // self.quad[1] + 1)
            for _ in range(self.tam[0] // self.quad[0] + 1)
        ]
        ret0 = self.quad[0] - self.tam[0] % self.quad[0]
        ret1 = self.quad[1] - self.tam[1] % self.quad[1]
        print(f"ret0 = {self.tam[0]} % {self.quad[0]} = {ret0}")
        print(f"ret1 = {self.tam[1]} % {self.quad[1]} = {ret1}")
        self.retorno = ret0 // 2, ret1 // 2
        print(f'retono = {self.retorno}')

    def surface(self):
        from random import randint
        for i in range(len(self.tabela)):
            for j in range(len(self.tabela[i])):
                cor = randint(0, 255), randint(0, 255), randint(0, 255)
                self.tabela[i][j] = pygame.Surface(self.quad)
                self.tabela[i][j].fill(cor)

        tela = pygame.Surface(self.tam)

        for i in range(len(self.tabela)):
            for j in range(len(self.tabela[i])):
                pygame.transform.scale(self.tabela[i][j], self.quad)
                tela.blit(self.tabela[i][j], (self.quad[0] * i - self.retorno[0], self.quad[1] * j - self.retorno[1]))

        return tela
