import pygame as pg
from .abc_scene import Scene

class GameScene(Scene):

    def __init__(self):
        super().__init__()

    def on_enter(self):
        super().on_enter()

        # Update sprite positions:
        screen_w, screen_h = pg.display.get_surface().get_size()
        self.place_sprites(screen_w, screen_h)

    def on_event(self, ev):
        if ev.type == pg.WINDOWSIZECHANGED:
            # Update sprite positions:
            self.place_sprites(ev.x, ev.y)

    def update(self, dt_ms, key_state):
        # Update all scene sprites:
        self.all.update(dt_ms)

    def place_sprites(self, screen_w, screen_h):
        pass