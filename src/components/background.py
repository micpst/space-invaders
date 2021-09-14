import pygame as pg
from assets.images import BACKGROUND

class Background(pg.sprite.Sprite):

    def __init__(self, size=(1,1)):
        super().__init__()
        self.resize(size)

    def resize(self, size):
        w, h = size
        bg_w, bg_h = BACKGROUND.get_size()

        cropped_img = pg.Surface((w, h))
        for x in range(0, w, bg_w):
            for y in range(0, h, bg_h):
                cropped_img.blit(BACKGROUND, (x, y))
        
        self.image = pg.Surface((w, 2 * h))
        self.rect = self.image.get_rect(y=-h)

        self.image.blit(cropped_img, (0, 0))
        self.image.blit(cropped_img, (0, h))

    def update(self):
        # Scroll the background by 1px per frame:
        self.rect.y = (self.rect.y + 1) % (-self.rect.h / 2)