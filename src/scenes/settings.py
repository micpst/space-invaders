import pygame as pg
from .abc_scene import GameScene
from components import *
from config import SETTINGS
from events import CHANGE_SCENE
from styles import *

class SettingsScene(GameScene):

    def __init__(self):
        super().__init__()
        
        self.title = Text(
            text='SETTINGS', 
            fsize=XL, 
            fcolor=WHITE
        )
        self.name_label = Text(
            text='NAME',
            fsize=S,
            fcolor=WHITE
        )
        self.difficulty_label = Text(
            text='DIFFICULTY',
            fsize=S,
            fcolor=WHITE
        )
        self.ship_label = Text(
            text='PLAYER SHIP',
            fsize=S,
            fcolor=WHITE
        )

        self.label_column = pg.sprite.Group(
            self.name_label,
            self.difficulty_label,
            self.ship_label
        )

    def on_enter(self):
        super().on_enter()

        # Load current settings:
        SETTINGS.load()
        
        # Get the current screen size:
        screen_w, screen_h = pg.display.get_surface().get_size()

        # Update sprite positions:
        self.place_sprites(screen_w, screen_h)

    def on_event(self, ev):
        if ev.type == pg.VIDEORESIZE:
            # Update sprite positions:
            self.place_sprites(ev.w, ev.h)

        elif ev.type == pg.KEYDOWN and ev.key == pg.K_RETURN:
            # Save current settings:
            SETTINGS.save()

            # Go to the menu scene:
            pg.event.post(pg.event.Event(CHANGE_SCENE, scene='menu'))
       
    def update(self, dt_ms, key_state):
        # Update all scene sprites:
        self.all.update(dt_ms)

    def place_sprites(self, screen_w, screen_h):
        # Setup the title position:
        x = screen_w / 2
        y = screen_h / 4

        # Place the title sprite:
        self.title.rect.center = (x, y)
        
        # Set the position of the labels in the left column:
        x = screen_w / 8
        y += 110
        dy = 50

        for sprite in self.label_column:
            sprite.rect.midleft = (x, y)
            y += dy