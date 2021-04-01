import pygame

from .game import GameState

class InterstitialState(GameState):
    def __init__(self, game, message, wait_time, next_state):
        super().__init__(game)

        self.font = pygame.font.SysFont('comicsans', 70)
        self.message = self.font.render(message, 1, (255, 255, 255))
        self.next_state = next_state
        self.wait_timer = wait_time
        
    def update(self, game_time):
        self.wait_timer -= gameTime
        if self.wait_timer < 0:
            self.game.change_state(self.next_state)
            
    def draw(self, window):
        window.blit(self.message, (self.width/2 - self.title.get_width()/2, 200))