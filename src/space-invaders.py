import sys
import pygame as pg

from events import *
from scenes import *

MIN_SCREEN_WIDTH = MIN_SCREEN_HEIGHT = 600
MIN_SCREEN_SIZE = (MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT)

class SpaceInvaders:
  
    def __init__(self):
        pg.init()

        pg.display.set_mode(MIN_SCREEN_SIZE, pg.RESIZABLE)
        pg.display.set_caption('Space Invaders')

        self.fps = 60
        self.clock = pg.time.Clock()
        self.running = True
  
        self.init_scenes()
        self.change_scene('menu')

    def init_scenes(self):
        self.scenes = {
            'menu': MenuScene(),
            'settings': SettingsScene(),
        }
        self.scene = None

    def change_scene(self, key):
        if key in self.scenes:
            if self.scene is not None:
                self.scene.on_exit()

            self.scene = self.scenes[key]
            self.scene.on_enter()

    def process_event(self, ev):
        if ev.type is pg.QUIT or \
           ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE:
            self.running = False
        
        elif ev.type == pg.VIDEORESIZE:
            ev.w = max(ev.w, MIN_SCREEN_WIDTH)
            ev.h = max(ev.h, MIN_SCREEN_HEIGHT)

            # Resize without emitting event:
            pg.display.set_mode((ev.w, ev.h), pg.RESIZABLE)
            pg.event.get(pg.VIDEORESIZE)

        elif ev.type == CHANGE_SCENE:
            self.change_scene(ev.scene)

    def start(self):
        while self.running:
            for e in pg.event.get(): 
                self.process_event(e)
                self.scene.on_event(e)

            self.scene.update(self.clock.get_time())
            self.scene.draw(pg.display.get_surface())
            
            pg.display.flip()
            self.clock.tick(self.fps)

        self.scene.on_exit()
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    game = SpaceInvaders()
    game.start()