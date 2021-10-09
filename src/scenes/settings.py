import pygame as pg
from .scene import Scene
from components.ui import *
from config import SETTINGS
from events import CHANGE_SCENE
from styles import *

class SettingsScene(Scene):

    def __init__(self):
        super().__init__()
        
        # Scene title:
        self.title = Text('SETTINGS', XL)

        # Label column:
        self.name_label = Text('NAME', S)
        self.difficulty_label = Text('DIFFICULTY', S)
        self.ship_label = Text('PLAYER SHIP', S)

        # Input column:
        self.name_input = TextBox()
        self.difficulty_input = OptionBox(['EASY', 'MEDIUM', 'HARD'])
        self.ship_input = OptionBox(['SPY 105'])

        # Scene groups:
        self.label_column = pg.sprite.Group(
            self.name_label,
            self.difficulty_label,
            self.ship_label
        )
        self.input_column = SelectionList(
            sprites=[
                self.name_input,
                self.difficulty_input,
                self.ship_input
            ],
            fsize=S,
            highlight_fsize=S
        )

    def on_enter(self):
        super().on_enter()

        # Load current settings:
        SETTINGS.load()

        # Reset the cursor on the option sprites:
        self.input_column.reset_focus()

        # Set the defaults:
        self.name_input.change_text(SETTINGS.player_name)
        self.difficulty_input.change_option(SETTINGS.difficulty)
        self.ship_input.change_option(SETTINGS.player_ship)

    def on_event(self, ev):
        super().on_event(ev)

        if ev.type == pg.KEYDOWN and ev.key == pg.K_RETURN:
            # Save current settings:
            SETTINGS.player_name = self.name_input.text
            SETTINGS.difficulty = self.difficulty_input.text
            SETTINGS.player_ship = self.ship_input.text
            SETTINGS.save()

            # Go to the menu scene:
            pg.event.post(pg.event.Event(CHANGE_SCENE, scene='menu'))

        self.input_column.on_event(ev)
        selected_sprite = self.input_column.selected_sprite()
        selected_sprite.on_event(ev)

    def update(self, dt_ms, key_state):
        super().update(dt_ms, key_state)
        self.input_column.update(dt_ms)

    def resize(self, screen_w, screen_h):
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

        # Set the position of the inputs in the right column:
        x = screen_w - x
        y = (screen_h / 4) + 110
        max_w = screen_w / 3.5
        
        for sprite in self.input_column:
            sprite.rect.w = max_w
            sprite.rect.midright = (x, y)
            y += dy