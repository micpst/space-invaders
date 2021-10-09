import pygame as pg
from components import Background

class Scene:

    background = Background()
    all = pg.sprite.LayeredUpdates(background, layer=0)

    def on_enter(self):
        # Add all scene sprites:
        scene_sprites = self.__dict__.values()
        self.all.add(scene_sprites, layer=1)

        # Update sprite positions:
        screen_w, screen_h = pg.display.get_surface().get_size()
        self.resize(screen_w, screen_h)
    
    def on_exit(self):
        # Remove all scene sprites: 
        self.all.remove_sprites_of_layer(1)

    def on_event(self, ev):
        # Update sprite positions:
        if ev.type == pg.WINDOWSIZECHANGED:
            self.resize(ev.x, ev.y)

    def resize(self, screen_w, screen_h):
        pass

    def update(self, dt_ms, key_state):
        self.all.update(dt_ms)

    def draw(self, screen):
        self.all.draw(screen)