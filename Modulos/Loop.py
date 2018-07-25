import pygame

clock_l = pygame.time.Clock()
clock_g = pygame.time.Clock()
janela = None
fps = 0


def executar():
    """Dispara Threads"""
    while True:
        eventos()
        janela.executar()


def eventos():
    """Verifique os eventos"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit(0)
            if event.key == pygame.K_F11:  # FIXME não se deve ter métodos concorrenco
                janela.fullscreen()
        if event.type == pygame.VIDEORESIZE:  # FIXME não se deve ter métodos concorrenco
            janela.resize(event.size)
