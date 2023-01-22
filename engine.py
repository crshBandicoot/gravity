import pygame
from settings import *
from objects import *

pygame.init()
font = pygame.font.SysFont('Arial', 20, bold=True)
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space')
clock = pygame.time.Clock()
stars = SpaceCollection()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            new_dot = SpaceDot(screen, list(pygame.mouse.get_pos()), 25, 1)
            stars.add(new_dot)
        if pygame.mouse.get_pressed()[2]:
            new_dot = SpaceDot(screen, list(pygame.mouse.get_pos()), 25, 10 ** 3)
            stars.add(new_dot)

    screen.blit(background, (0, 0))
    stars.update()
    position = font.render(str(pygame.mouse.get_pos()),
                           True, pygame.Color('Blue'))
    screen.blit(position, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
