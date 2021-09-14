import pygame as pg
from abc import ABCMeta, abstractmethod

class GameScene(metaclass=ABCMeta):

    def __init__(self):
        self.all = pg.sprite.Group()

    @abstractmethod
    def on_enter(self):
        pass
    
    @abstractmethod
    def on_exit(self):
        pass

    @abstractmethod
    def on_event(self, ev):
        pass

    @abstractmethod
    def update(self, dt_ms):
        pass

    def draw(self, screen):
        self.all.draw(screen)