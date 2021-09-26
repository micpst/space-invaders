import pygame as pg
from abc import ABCMeta, abstractmethod
from components import Background

class GameScene(metaclass=ABCMeta):

    background = Background()
    all = pg.sprite.LayeredUpdates(background, layer=0)

    def on_enter(self):
        # Add all scene sprites:
        scene_sprites = self.__dict__.values()
        self.all.add(scene_sprites, layer=1)
    
    def on_exit(self):
        # Remove all scene sprites: 
        self.all.remove_sprites_of_layer(1)

    @abstractmethod
    def on_event(self, ev):
        pass

    @abstractmethod
    def update(self, dt_ms, key_state):
        pass

    def draw(self, screen):
        self.all.draw(screen)