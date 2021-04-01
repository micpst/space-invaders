import pygame
from assets import *

class MenuView:
    def __init__(self):
        self.font = pygame.font.SysFont('comicsans', 70)
        self.logo = pygame.transform.scale(LOGO, (450, 175))
        self.options = []

    def update(self, options, index):
        self.options = []
        for i, option in enumerate(options):
            color = (230, 230, 0) if i == index else (255, 255, 255)
            self.options.append(self.font.render(option, 1, color))

    def render(self, window):
        y = 100
        x = window.get_width() / 2 - self.logo.get_width() / 2
        window.blit(self.logo, (x, y))

        y += 200
        for option in self.options:
            x = window.get_width() / 2 - option.get_width() / 2
            window.blit(option, (x, y))
            y += 65