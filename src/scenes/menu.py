import pygame
from .abc_scene import GameScene
from components import ScrollingBackground, OptionsList, Text
from events import CHANGE_SCENE
from styles import *

class MenuScene(GameScene):

    def __init__(self):
        super().__init__()
        self.background = ScrollingBackground()
        self.title = Text('SPACE INVADERS', XL, WHITE)
        self.options = OptionsList(['Play', 'Settings', 'Quit'])

    def on_enter(self):
        # Get the current screen size:
        screen_size = pygame.display.get_surface().get_size()
        screen_width, screen_height = screen_size

        # Resize the background:
        self.background.resize(screen_size)

        # Update sprite positions:
        self.place_sprites(screen_width, screen_height)
        
        # Reset the cursor on the option sprites:
        self.options.reset_focus()

    def on_exit(self):
        pass

    def on_event(self, ev):
        if ev.type == pygame.VIDEORESIZE:
            # Resize the background:
            self.background.resize((ev.w, ev.h))
            
            # Update sprite positions:
            self.place_sprites(ev.w, ev.h)

        elif ev.type == pygame.KEYDOWN:
            # Move the selection up or down:
            if ev.key == pygame.K_UP:
                self.options.move_focus('up')

            elif ev.key == pygame.K_DOWN:
                self.options.move_focus('down')
            
            # Emit an event based on the selected option:
            elif ev.key is pygame.K_RETURN:    
                pygame.event.post({
                    0: pygame.event.Event(CHANGE_SCENE, scene='gameplay'),
                    1: pygame.event.Event(CHANGE_SCENE, scene='settings'),
                    2: pygame.event.Event(pygame.QUIT)
                }[self.options.index])

    def update(self, time_ms):
        # Scroll background by 1px per frame:
        self.background.update(speed=1)

    def place_sprites(self, screen_w, screen_h):
        x = screen_w / 2
        y = screen_h / 4

        self.title.place(center=(x, y))
        self.options.place(center=(x, y + 110), dy=50)