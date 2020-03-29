import pygame

class Button():

    def __init__(self, color, coordinates, dimensions, message):
        self.color = color
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.width = dimensions[0]
        self.heigth = dimensions[1]
        self.message = message

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth), 0)
        

    def isOver(self, position):
        if position[0] > self.x and position[0] < self.x + self.height:
            if position[1] > self.y and position[1] < self.y + self.width:
                return True

        return False
