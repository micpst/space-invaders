import pygame as pg
from .abc_scene import GameScene
from components import Background, SelectionList, Text
from events import CHANGE_SCENE
from styles import *

class MenuScene(GameScene):

    def __init__(self):
        super().__init__()

        self.background = Background()
        self.title = Text(
            text='SPACE INVADERS', 
            fsize=XL, 
            fcolor=WHITE
        )
        self.play = Text(
            text='PLAY', 
            fsize=M, 
            fcolor=WHITE
        )
        self.settings = Text(
            text='SETTINGS', 
            fsize=M, 
            fcolor=WHITE
        )
        self.quit = Text(
            text='QUIT', 
            fsize=M, 
            fcolor=WHITE
        )

        self.options = SelectionList(
            sprites=[
                self.play, 
                self.settings, 
                self.quit
            ],
            fsize=M, 
            fcolor=WHITE,
            highlight_fsize=L, 
            highlight_fcolor=YELLOW
        )

        # Register all scene sprites:
        self.all.add(
            self.background, 
            self.title, 
            self.play, 
            self.settings, 
            self.quit
        )

    def on_enter(self):
        # Get the current screen size:
        screen_w, screen_h = pg.display.get_surface().get_size()

        # Update sprite positions:
        self.place_sprites(screen_w, screen_h)
        
        # Reset the cursor on the option sprites:
        self.options.reset_focus()

    def on_exit(self):
        pass

    def on_event(self, ev):
        if ev.type == pg.VIDEORESIZE:
            # Update sprite positions:
            self.place_sprites(ev.w, ev.h)

        elif ev.type == pg.KEYDOWN and ev.key is pg.K_RETURN:
            # Emit an event based on the selected option:
            selected_sprite = self.options.selected_sprite()
            pg.event.post({
                self.play: pg.event.Event(CHANGE_SCENE, scene='gameplay'),
                self.settings: pg.event.Event(CHANGE_SCENE, scene='settings'),
                self.quit: pg.event.Event(pg.QUIT)
            }[selected_sprite])

        self.options.on_event(ev)

    def update(self, dt_ms, key_state):
        # Update all scene sprites:
        self.all.update(dt_ms)
        self.options.update(dt_ms)

    def place_sprites(self, screen_w, screen_h):
        # Resize the background:
        self.background.resize((screen_w, screen_h))
        
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