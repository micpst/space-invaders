import pygame as pg
from .text import Text
from styles import *

class OptionBox(Text):

    def __init__(self, options=[''], selected=0, fsize=M, fcolor=WHITE):
        super().__init__('', fsize, fcolor)

        self.options = options
        self.selected = selected

        self.pressed_key = None
        self.delay_ms = 400

        self.change_text(self.options[self.selected])

    def _rerender(self):
        # Render the text sprite in the same position:
        self.text_image = self.font.render(self.text, 1, self.fcolor)
        self.text_rect = self.text_image.get_rect(centerx=(self.rect.w / 2))
        
        self.image = pg.Surface((self.rect.w, self.text_rect.h), pg.SRCALPHA)
        self.rect = self.image.get_rect(midright=self.rect.midright)

        pg.draw.polygon(self.image, self.fcolor, [(0, self.rect.h / 2), (15, 0), (15, self.rect.h)])
        pg.draw.polygon(self.image, self.fcolor, [(self.rect.w, self.rect.h / 2), (self.rect.w - 15, 0), (self.rect.w - 15, self.rect.h)])
        
        self.image.blit(self.text_image, self.text_rect)  

    def on_event(self, ev):
        if ev.type == pg.KEYDOWN and ev.key in (pg.K_LEFT, pg.K_RIGHT):
            # Move the selection up or down:
            direction = -1 if ev.key == pg.K_LEFT else 1
            self.move_selection(direction)

            self.pressed_key = ev.key
            self.delay_ms = 400
            
        elif ev.type == pg.KEYUP and ev.key in (pg.K_LEFT, pg.K_RIGHT):
            self.pressed_key = None
            self.delay_ms = 400

    def update(self, dt_ms, *args, **kwargs):   
        if self.pressed_key:
            if self.delay_ms <= 0:
                direction = -1 if self.pressed_key == pg.K_LEFT else 1
                self.move_selection(direction)

                # Set the delay to 20 ms:
                self.delay_ms = 20
            else:
                # Count the remaining delay:
                self.delay_ms -= dt_ms

    def move_selection(self, direction):
        # Change index value and update the group sprites:
        self.selected = (self.selected + direction) % len(self.options)   
        self.change_text(self.options[self.selected])