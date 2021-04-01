import sys
import pygame

from states import *

class SpaceInvaders:
    def __init__(self, size):		
        pygame.init()
        pygame.display.set_caption('Space Invaders')

        self.mapping = {
            'menu': MainMenuState(self),
            # 'settings': None,
            # 'gameplay': None,
            # 'scoreboard': None,
            # 'pause': None,
        }
        self.state = self.mapping['menu']
        
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size)
        self.running = True

    def switch_state(self, key):
        if self.state is not None:
            self.state.on_exit()
            
        if key in self.mapping:
            self.state = self.mapping[key]
            self.state.on_enter()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            time = self.clock.get_time()
            self.state.update(time)
            self.state.draw(self.screen)
            
            pygame.display.update()
            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = SpaceInvaders((750, 750))
    game.run()