import pygame
import math
import random

class Particle():

    def __init__(self, condition, x, y,  ):
        self.condition = condition
        self.x = x
        self.y = y
        self.speed = 2
        self.angle = random.uniform(0, math.pi*2)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.x), int(self.y)), 5)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y += math.cos(self.angle) * self.speed
