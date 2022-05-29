import pygame

# ****************************************************************************************************

class Screen:
    pygame.init()

    def __init__(self):
        self.CELL_SIZE = 40
        self.CELL_NUMBER = 20
        self.display = pygame.display.set_mode(((self.CELL_NUMBER * self.CELL_SIZE),
                                                (self.CELL_NUMBER * self.CELL_SIZE)))
