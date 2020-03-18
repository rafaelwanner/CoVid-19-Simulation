import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("CoVid-19 Simulation")
icon = pygame.image.load('bacteria.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
