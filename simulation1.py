import pygame
import random
from particle import *
pygame.init()

screen = pygame.display.set_mode((800,600))


particles = []
for i in range(1,10):
    x = random.randint(0, 800)
    y = random.randint(0,600)
    particles.append(Particle((255,255,255), x, y))

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        particle.move()
        particle.draw(screen)


    pygame.display.update()
