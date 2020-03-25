import pygame
from utils import *

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("CoVid-19 Simulation")
icon = pygame.image.load('bacteria.png')
pygame.display.set_icon(icon)

bacteria = pygame.image.load('bacteria.png')

def display():
    screen.blit(bacteria, (300, 300))

def redrawWindow():
    screen.fill((255,255,255))
    sim1.draw(screen)

running = True
sim1 = Button((0,0,0), 200, 300, 300, 150)

while running:

    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #display()
    pygame.display.update()
