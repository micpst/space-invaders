import pygame
from assets.images import BACKGROUND

class ScrollingBackground(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = BACKGROUND

    def resize(self, size):
        self.viewport_size = size
        w, h = self.viewport_size

        self.rects = []
        for x in range(0, w, self.image.get_width()):
            for y in range(-h, h, self.image.get_height()):
                self.rects.append(self.image.get_rect(x=x, y=y))

    def update(self, speed):
        for rect in self.rects:
            _, h = self.viewport_size
            rect.y = -h if rect.y > h else rect.y + speed

    def draw(self, screen):
        for rect in self.rects:
            screen.blit(self.image, rect)