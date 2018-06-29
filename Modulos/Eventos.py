import pygame

def eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()