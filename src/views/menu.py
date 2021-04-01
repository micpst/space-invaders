import pygame

class MenuView:
    def __init__(self):
        self.font = pygame.font.SysFont('comicsans', 70)

    def render(self, window):
        self.font.render('Play', 1, (255, 255, 255))