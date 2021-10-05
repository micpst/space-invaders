import itertools
import pygame as pg
from assets.images import BACKGROUND

class Background(pg.sprite.Sprite):

    def __init__(self, size=(1,1), speed=1):
        super().__init__()

        self.speed = speed
        self.make_surface(size)

    def make_surface(self, size):
        w, h = size
        tile_w, tile_h = BACKGROUND.get_size()

        # Make a background image of tiles:
        bg_img = pg.Surface((w, h))
        for x, y in itertools.product(range(0, w, tile_w), 
                                      range(0, h, tile_h)):
            bg_img.blit(BACKGROUND, (x, y))

        # Create scrolling surface:
        self.image = pg.Surface((w, 2 * h))
        self.rect = self.image.get_rect(y=-h)

        # Cover the scrolling surface with background images:
        self.image.blit(bg_img, (0, 0))
        self.image.blit(bg_img, (0, h))

    def update(self, *args, **kwargs):
        # Scroll the background surface:
        self.rect.y = (self.rect.y + self.speed) % (-self.rect.h / 2)