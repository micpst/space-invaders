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

        self.reset_focus()

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