import pygame
import random
from particle import *
pygame.init()

size = 5
height = 800
width = 600
healthy = (255,255,255)
infected = (255, 0, 111)
recovered = (128, 255, 0)

screen = pygame.display.set_mode((height, width))

particles = [Particle(infected, random.randint(0, height), random.randint(0, width), size)]
for i in range(1, 50):
    x = random.randint(0, height)
    y = random.randint(0, width)
    particles.append(Particle(healthy, x, y, size))

def infection(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    d = math.hypot(dx, dy)

    if d < p1.size + p2. size:
        if p1.condition == infected:
            if p2.immune != 0:
                p2.condition = infected
        if p2.condition == infected:
            if p1.immune != 0:
                p1.condition = infected

        tangent = math.atan2(dy, dx)
        p1.angle = 2*tangent - p1.angle
        p2.angle = 2*tangent - p2.angle

        angle = 0.5 * math.pi + tangent
        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)
        p2.x -= math.sin(angle)
        p2.y += math.cos(angle)


running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i, particle in enumerate(particles):
        particle.contact()
        particle.move()
        if particle.condition == infected:
            particle.immune -= 1
            if particle.immune == 0:
                particle.condition = recovered
        for particle1 in particles[i+1:]:
            infection(particle, particle1)
        particle.draw(screen)


    pygame.display.update()
