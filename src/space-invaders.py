import sys
import pygame

from events import *
from scenes import *

MIN_SCREEN_WIDTH = MIN_SCREEN_HEIGHT = 600
MIN_SCREEN_SIZE = (MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT)

class SpaceInvaders:
  
    def __init__(self):
        pygame.init()

        pygame.display.set_mode(MIN_SCREEN_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption('Space Invaders')

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.running = True
  
        self.init_scenes()
        self.change_scene('menu')

    def init_scenes(self):
        self.scenes = {
            'menu': MenuScene(),
        }
        self.scene = None

    def change_scene(self, key):
        if key in self.scenes:
            if self.scene is not None:
                self.scene.on_exit()

            self.scene = self.scenes[key]
            self.scene.on_enter()

    def process_event(self, ev):
        if ev.type is pygame.QUIT or \
           ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            self.running = False
        
        elif ev.type == pygame.VIDEORESIZE:
            ev.w = max(ev.w, MIN_SCREEN_WIDTH)
            ev.h = max(ev.h, MIN_SCREEN_HEIGHT)

            # Resize without emitting event:
            pygame.display.set_mode((ev.w, ev.h), pygame.RESIZABLE)
            pygame.event.get(pygame.VIDEORESIZE)

        elif ev.type is CHANGE_SCENE:
            self.change_scene(ev.scene)

    def start(self):
        while self.running:
            for e in pygame.event.get(): 
                self.process_event(e)
                self.scene.on_event(e)

            self.scene.update(self.clock.get_time())
            self.scene.draw(pygame.display.get_surface())
            
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = SpaceInvaders()
    game.start()