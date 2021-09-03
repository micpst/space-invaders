import pygame
from assets.fonts import ARCADE_IN

class Text(pygame.sprite.Sprite):

    def __init__(self, text, font_size, font_color):
        super().__init__()
        self.text = text
        self.font = ARCADE_IN[font_size]
        self.font_color = font_color

        self.image = self.font.render(self.text, 1, self.font_color)
        self.rect = self.image.get_rect()

    def __render(self):
        self.image = self.font.render(self.text, 1, self.font_color)
        self.rect = self.image.get_rect(center=self.rect.center)

    def change_text(self, text):
        self.text = text
        self.__render()

    def change_font_size(self, size):
        self.font = ARCADE_IN[size]
        self.__render()

    def change_font_color(self, font_color):
        self.font_color = font_color
        self.__render()

    def place(self, *args, **kwargs):
        for key in kwargs:
            if key in dir(self.rect):
                setattr(self.rect, key, kwargs[key])

    def draw(self, screen):
        screen.blit(self.image, self.rect)