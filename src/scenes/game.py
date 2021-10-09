import pygame as pg
from .scene import Scene

class GameScene(Scene):

    def __init__(self):
        super().__init__()

    def on_enter(self):
        super().on_enter()

    def on_event(self, ev):
        super().on_event(ev)

    def update(self, dt_ms, key_state):
        super().update(dt_ms, key_state)

    def resize(self, screen_w, screen_h):
        pass