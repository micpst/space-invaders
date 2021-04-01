import pygame

from .game import GameState
from controllers import MenuController

class MainMenuState(GameState):
    def __init__(self, game):
        self.game = game
        self.controller = MenuController(self.game)

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def update(self, game_time):
        self.controller.update(game_time)

    def draw(self, window):
        self.controller.draw(window)