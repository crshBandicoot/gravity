import pygame

WIDTH = 800
HEIGHT = 800
FPS = 60
background = pygame.transform.smoothscale(
    pygame.image.load('img\space.jpg'), (800, 800))
star = pygame.transform.smoothscale(
    pygame.image.load('img\star.png'), (60, 60))
