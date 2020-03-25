import pygame
import math
import random

class Particle():

    def __init__(self, condition, x, y, size):
        self.condition = condition
        self.x = x
        self.y = y
        self.size = size
        self.immune = 500
        self.speed = 3
        self.angle = random.uniform(0, math.pi*2)


    def draw(self, screen):
        pygame.draw.circle(screen, self.condition, (int(self.x), int(self.y)), self.size)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y += math.cos(self.angle) * self.speed

    def contact(self):
        if self.x - self.size/2 < 0:
            self.angle = - self.angle
        elif self.x + self.size/2 > 800 :
            self.angle = - self.angle

        if self.y - self.size/2 < 0:
            self.angle = math.pi - self.angle
        elif self.y + self.size/2 > 600:
            self.angle = math.pi - self.angle
