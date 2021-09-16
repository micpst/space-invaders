import pygame as pg
from .abc_scene import GameScene
from components import Background, Text
from events import CHANGE_SCENE
from styles import *

class SettingsScene(GameScene):

    def __init__(self):
        super().__init__()

        self.background = Background()
        self.title = Text(
            text='SETTINGS', 
            fsize=XL, 
            fcolor=WHITE
        )

        # Register all scene sprites:
        self.all.add(
            self.background, 
            self.title
        )

    def on_enter(self):
        # Get the current screen size:
        screen_w, screen_h = pg.display.get_surface().get_size()

        # Update sprite positions:
        self.place_sprites(screen_w, screen_h)

    def on_exit(self):
        pass

    def on_event(self, ev):
        if ev.type == pg.VIDEORESIZE:
            # Update sprite positions:
            self.place_sprites(ev.w, ev.h)

        elif ev.type == pg.KEYDOWN:
            # Save current settings and move to the menu scene:
            if ev.key is pg.K_RETURN:
                pg.event.post(pg.event.Event(CHANGE_SCENE, scene='menu'))
       
    def update(self, dt_ms):
        # Update all scene sprites:
        self.all.update()

    def place_sprites(self, screen_w, screen_h):
        # Resize the background:
        self.background.resize((screen_w, screen_h))
        
        # Setup the title position:
        x = screen_w / 2
        y = screen_h / 4

        # Place the title sprite:
        self.title.rect.center = (x, y)