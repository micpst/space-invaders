import pygame
from .text import Text
from styles import *

class OptionsList(pygame.sprite.Group):
    
    def __init__(self, options=[]):
        super().__init__()
        self._index = 0
        self.create_sprites(options)

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self.sprites()[self.index].change_font_size(M)
        self.sprites()[self.index].change_font_color(WHITE)
        self.sprites()[index].change_font_size(L)
        self.sprites()[index].change_font_color(YELLOW)
        self._index = index

    def create_sprites(self, options):
        for i, option in enumerate(options):
            size, color = { 0: (M, WHITE), 1: (L, YELLOW) }[self.index == i]
            self.add(Text(option, size, color))

    def reset_focus(self):
        self.index = 0

    def move_focus(self, direction):
        offset = { 'up': -1, 'down': 1 }[direction]
        self.index = (self.index + offset) % len(self.sprites())   

    def change_text(self, text):
        self.sprites()[self.index].change_text(text)

    def place(self, center, dy):
        x, y = center
        for sprite in self.sprites():
            sprite.place(center=(x, y))
            y += dy