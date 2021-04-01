import pygame

from models import *
from views import *

class MenuController:
    def __init__(self, game):
        self.game = game
        self.model = MenuModel()
        self.view = MenuView()

    def update(self, game_time):	
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_DOWN] and self.model.input_tick == 0:
            self.model.input_tick = 250

            if keys[pygame.K_UP]:
                self.model.index -= 1
                if self.model.index < 0:
                    self.model.index = len(self.model.options) - 1

            elif keys[pygame.K_DOWN]:
                self.model.index += 1
                if self.model.index == len(self.model.options):
                    self.model.index = 0

        if keys[pygame.K_RETURN]:
            if self.model.index == 0:
                self.game.switch_state('gameplay')

            elif self.model.index == 1:
                self.game.switch_state('settings')

            elif self.model.index == 2:
                self.game.running = False

        if self.model.input_tick > 0:
            self.model.input_tick -= game_time
        else:
            self.model.input_tick = 0
                
    def draw(self, window):	
        self.view.render(window)