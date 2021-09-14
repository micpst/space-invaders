import pygame as pg
from assets.fonts import ARCADE_IN

class Text(pg.sprite.Sprite):

    def __init__(self, text, fsize, fcolor):
        super().__init__()
        
        self.text = text
        self.font = ARCADE_IN[fsize]
        self.fcolor = fcolor

        # Initial render on the top left corner of the screen:
        self.image = self.font.render(self.text, 1, self.fcolor)
        self.rect = self.image.get_rect()

    def _rerender(self):
        # Render the text sprite in the same position:
        self.image = self.font.render(self.text, 1, self.fcolor)
        self.rect = self.image.get_rect(center=self.rect.center)

    def change_text(self, text):
        self.text = text
        self._rerender()

    def change_fsize(self, fsize):
        self.font = ARCADE_IN[fsize]
        self._rerender()

    def change_fcolor(self, fcolor):
        self.fcolor = fcolor
        self._rerender()