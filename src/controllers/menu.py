import pygame

from models import *
from views import *

class MenuController:
    def __init__(self, game):
        self.game = game
        self.model = MenuModel()
        self.view = MenuView()

    def update(self, game_time):
        self.model.update(game_time)
        self.view.update(self.model.options, self.model.index)

        if self.model.timeout == 0:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.model.tick()
                self.model.move('up')

            elif keys[pygame.K_DOWN]:
                self.model.tick()
                self.model.move('down')

            elif keys[pygame.K_RETURN]:
                if self.model.index == 0:
                    self.game.switch_state('gameplay')

                elif self.model.index == 1:
                    self.game.switch_state('settings')

                elif self.model.index == 2:
                    self.game.running = False

    def draw(self, window):	
        self.view.render(window)