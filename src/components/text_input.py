import pygame as pg
from .text import Text

class TextInput(Text):

    def __init__(self, text, fsize, fcolor, max_width=3):
        super().__init__(text, fsize, fcolor)

        self.max_width = max_width
        self.pressed_key = None
        self.blink_ms = 500
        self.delay_ms = 400

        self.cursor_visible = True
        self.cursor_width = 3
    
    def _rerender(self):
        # Render the text sprite in the same position:
        self.text_image = self.font.render(self.text, 1, self.fcolor)
        self.text_rect = self.text_image.get_rect()

        self.image = pg.Surface((self.max_width, self.text_rect.h), pg.SRCALPHA)
        self.rect = self.image.get_rect(midright=self.rect.midright)

        if self.text_rect.w > self.max_width:
            self.text_rect.right = self.max_width

        self.image.blit(self.text_image, self.text_rect)  

    def _rerender_cursor(self):
        cursor_x = min(self.text_rect.w, self.max_width - self.cursor_width)
        color = self.fcolor if self.cursor_visible else (0, 0, 0, 0)
        
        self.cursor_rect = pg.Rect((cursor_x, 0), (self.cursor_width, self.text_rect.h))
        self.image.fill(color, self.cursor_rect)

    def change_text(self, text):
        super().change_text(text)
        self.cursor_visible = True

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
        if self.blink_ms <= 0:
            self.blink_ms = 500
            self.cursor_visible ^= True
        else:
            self.blink_ms -= dt_ms
    
        self._rerender_cursor()

        if self.pressed_key:
            if self.delay_ms <= 0:
                if self.pressed_key.key == pg.K_BACKSPACE:
                    self.change_text(self.text[:-1])

                # Set the delay to 20 ms:
                self.delay_ms = 20
            else:
                # Count the remaining delay:
                self.delay_ms -= dt_ms