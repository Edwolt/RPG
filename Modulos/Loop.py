import pygame
import threading


class Loop:
    def __init__(self, janela, fps=0):
        self.clock_l = pygame.time.Clock()
        self.clock_g = pygame.time.Clock()
        self.janela = janela
        self.fps = fps
        self.Logica = None
        self.Grafico = None

    def executar(self):
        self.Logica = threading.Thread(target=self.logica, args=tuple())
        self.Grafico = threading.Thread(target=self.grafico, args=tuple())
        self.Grafico.daemon = True
        self.Logica.start()
        self.Grafico.start()

    def eventos(self):
        """Verifique os eventos"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit(0)
                if event.key == pygame.K_F11:  # FIXME não se deve ter métodos concorrenco
                    self.janela.fullscreen()
            if event.type == pygame.VIDEORESIZE:  # FIXME não se deve ter métodos concorrenco
                self.janela.resize(event.size)

    def logica(self):
        while True:
            self.eventos()
            self.clock_l.tick(self.fps)
            # print(f'Lógica_FPS: {self.clock_l.get_fps()}')

    def grafico(self):
        while True:
            self.janela.executar()
            # print(f'Gráfico_FPS: {self.clock_g.get_fps()}')
