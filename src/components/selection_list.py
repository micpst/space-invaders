import pygame as pg
from styles import *

class SelectionList(pg.sprite.Group):
    
    def __init__(
        self, 
        sprites, 
        fsize, 
        fcolor, 
        highlight_fsize, 
        highlight_fcolor
    ):
        super().__init__(*sprites)

        self.fsize = fsize 
        self.fcolor = fcolor 
        self.highlight_fsize = highlight_fsize 
        self.highlight_fcolor = highlight_fcolor

        self.pressed_key = None
        self.delay_ms = 400

        self.reset_focus()

    def on_event(self, ev):
        if ev.type == pg.KEYDOWN and ev.key in (pg.K_UP, pg.K_DOWN):
            # Move the selection up or down:
            direction = -1 if ev.key == pg.K_UP else 1
            self.move_focus(direction)
            
            # Start listening for key state after 750 ms:
            self.pressed_key = ev.key
            self.delay_ms = 750

        elif ev.type == pg.KEYUP and ev.key == self.pressed_key:
            # Stop listening for key state:
            self.pressed_key = None

    def update(self, dt_ms, *args, **kwargs):  
        if self.pressed_key:
            if self.delay_ms <= 0:
                # Move the selection up or down:
                direction = -1 if self.pressed_key == pg.K_UP else 1
                self.move_focus(direction)

                # Set the delay to 200 ms:
                self.delay_ms = 200
            else:
                # Count the remaining delay:
                self.delay_ms -= dt_ms

    def selected_sprite(self):
        return self.sprites()[self.index]

    def update_sprites(self):
        # Update the color and size of the group sprites:
        for i, sprite in enumerate(self.sprites()):
            if self.index == i:
                sprite.change_fcolor(self.highlight_fcolor)
                sprite.change_fsize(self.highlight_fsize)
            else:
                sprite.change_fcolor(self.fcolor)
                sprite.change_fsize(self.fsize)

    def reset_focus(self):
        # Reset index value and update the group sprites:
        self.index = 0
        self.update_sprites()

    def move_focus(self, direction):
        # Change index value and update the group sprites:
        self.index = (self.index + direction) % len(self.sprites())   
        self.update_sprites()