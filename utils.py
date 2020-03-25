import pygame

class Button():

    def __init__(self, color, x, y, width, heigth):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth), 0)

    def isOver(self, position):
        if position[0] > self.x and position[0] < self.x + self.height:
            if position[1] > self.y and position[1] < self.y + self.width:
                return True

        return False
