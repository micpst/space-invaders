import pygame as pg
from .text import Text

class TextInput(Text):

    def __init__(self, text, fsize, fcolor, max_width=3):
        super().__init__(text, fsize, fcolor)

        self.max_width = max_width
        self.pressed_key = None
        self.delay_ms = 400
    
    def _rerender(self):
        # Render the text sprite in the same position:
        self.text_image = self.font.render(self.text, 1, self.fcolor)
        self.text_rect = self.text_image.get_rect()

        self.image = pg.Surface((self.max_width, self.text_rect.h), pg.SRCALPHA)
        self.rect = self.image.get_rect(midright=self.rect.midright)

        if self.text_rect.w > self.max_width:
            self.text_rect.right = self.max_width

        self.image.blit(self.text_image, self.text_rect)      

    def on_event(self, ev):
        if ev.type == pg.TEXTINPUT:
            self.change_text(self.text + ev.text)

        elif ev.type == pg.KEYDOWN and ev.key == pg.K_BACKSPACE:
            self.change_text(self.text[:-1])
            self.pressed_key = ev
            self.delay_ms = 400
    
        elif ev.type == pg.KEYUP and self.pressed_key and self.pressed_key.key == ev.key:
            self.pressed_key = None
            self.delay_ms = 400

    def update(self, dt_ms, *args, **kwargs):   
        if self.pressed_key:
            if self.delay_ms <= 0:
                if self.pressed_key.key == pg.K_BACKSPACE:
                    self.change_text(self.text[:-1])

                # Set the delay to 20 ms:
                self.delay_ms = 20
            else:
                # Count the remaining delay:
                self.delay_ms -= dt_ms