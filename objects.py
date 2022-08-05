import pygame
from settings import *
from functions import *


class SoftDot:
    def __init__(self, screen, coordinates, radius, color, width):
        self.screen = screen
        self.coordinates = coordinates
        self.radius = radius
        self.color = color
        self.width = width
        self.speed = [0, 0]
        self.g = 0

    def move(self):
        if self.coordinates[0] > (WIDTH - self.radius):
            self.coordinates[0] = self.radius
        if self.coordinates[1] >= (HEIGHT - self.radius):
            self.speed[1] = -self.speed[1]*0.75
        if self.coordinates[1] > (HEIGHT - self.radius):
            self.coordinates[1] = HEIGHT - self.radius
        self.speed[1] += self.g
        self.coordinates = [self.coordinates[0] +
                            self.speed[0], self.coordinates[1]+self.speed[1]]

    def update(self):
        self.move()
        pygame.draw.circle(self.screen, self.color,
                           self.coordinates, self.radius, self.width)


class SpaceDot:
    def __init__(self, screen, coordinates, radius, color, width):
        self.screen = screen
        self.coordinates = coordinates
        self.radius = radius
        self.color = color
        self.width = width
        self.speed = [0, 0]
        self.mass = 600

    def move(self):
        self.coordinates = [self.coordinates[0] +
                            self.speed[0], self.coordinates[1]+self.speed[1]]

    def update(self):
        self.move()
        self.screen.blit(star, self.coordinates)


class SpaceCollection:
    def __init__(self):
        self.objects = []

    def add(self, elem):
        self.objects.append(elem)

    def update(self):
        for object in self.objects:
            speedx = 0
            speedy = 0
            if len(self.objects) > 1:
                for dot in self.objects:
                    if object != dot:
                        dist = distance(object.coordinates, dot.coordinates)
                        if dist > 30:
                            acceleration = dot.mass/(dist**2)
                            vect = ort_vector(
                                object.coordinates, dot.coordinates)
                            speedx += acceleration*vect[0]
                            speedy += acceleration*vect[1]
            object.speed[0] += speedx
            object.speed[1] += speedy
            object.update()


class Collection:
    def __init__(self):
        self.objects = []

    def add(self, elem):
        self.objects.append(elem)

    def update(self):
        for elem in self.objects:
            elem.update()
