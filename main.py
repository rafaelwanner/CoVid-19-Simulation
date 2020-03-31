import pygame
from utils import *


pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("CoVid-19 Simulation")
icon = pygame.image.load('bacteria.png')
pygame.display.set_icon(icon)

bacteria = pygame.image.load('bacteria.png')

def redrawWindow():
    screen.fill((255,255,255))
    sim1.draw(screen)
    sim2.draw(screen)


cor1 = (100, 250)
dim1 = (250, 100)
sim1 = Button((0,0,0), cor1, dim1, "Simulation without social distancing")

cor2 = (450, 250)
dim2 = (250, 100)
sim2 = Button((0,0,0), cor2, dim2, "Simulation with social distancing")

running = True
while running:

    redrawWindow()
    font1 = pygame.font.SysFont(None, 40)
    font2 = pygame.font.SysFont(None, 20)
    title = font1.render('Welcome to the CoVid-19 Simulation', True, (84, 126, 184))
    simulation_1 = font2.render('without social distancing', True, (84, 126, 184))
    simulation_2 = font2.render('with social distancing', True, (84, 126, 184))
    screen.blit(title, (150, 100))
    screen.blit(simulation_1, (145, 300))
    screen.blit(simulation_2, (505, 300))


    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if mouse_position[0] <= cor1[0] + dim1[0] and mouse_position[0] >= cor1[0]:
                if mouse_position[1] <= cor1[1] + dim1[1] and mouse_position[1] >= cor1[1]:
                    from simulation1 import *
            if mouse_position[0] <= cor2[0] + dim2[0] and mouse_position[0] >= cor2[0]:
                if mouse_position[1] <= cor2[1] + dim2[1] and mouse_position[1] >= cor2[1]:
                    from simulation2 import *
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
