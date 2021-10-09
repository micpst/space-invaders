import pygame as pg
from .scene import Scene
from components.ui import *
from events import CHANGE_SCENE
from styles import *

class MenuScene(Scene):

    def __init__(self):
        super().__init__()
        
        # Scene title:
        self.title = Text('SPACE INVADERS', XL)

        # Menu options:
        self.play = Text('PLAY')
        self.settings = Text('SETTINGS')
        self.quit = Text('QUIT')

        # Scene group:
        self.options = SelectionList([
            self.play, 
            self.settings, 
            self.quit
        ])

    def on_enter(self):
        super().on_enter()

        # Reset the cursor on the option sprites:
        self.options.reset_focus()

    def on_event(self, ev):
        super().on_event(ev)
        self.options.on_event(ev)

        if ev.type == pg.KEYDOWN and ev.key is pg.K_RETURN:
            # Emit an event based on the selected option:
            selected_sprite = self.options.selected_sprite()
            pg.event.post({
                self.play: pg.event.Event(CHANGE_SCENE, scene='game'),
                self.settings: pg.event.Event(CHANGE_SCENE, scene='settings'),
                self.quit: pg.event.Event(pg.QUIT)
            }[selected_sprite])   

    def update(self, dt_ms, key_state):
        super().update(dt_ms, key_state)
        self.options.update(dt_ms)

    def resize(self, screen_w, screen_h):
        # Setup the title position:
        x = screen_w / 2
        y = screen_h / 4

        # Place the title sprite:
        self.title.rect.center = (x, y)
        
        # Setup the options position:
        y += 110
        dy = 50

        # Place the options sprites:
        for sprite in self.options:
            sprite.rect.center = (x, y)
            y += dy