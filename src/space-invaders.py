import sys
import pygame as pg

from events import *
from scenes import *

MIN_SCREEN_WIDTH = MIN_SCREEN_HEIGHT = 600
MIN_SCREEN_SIZE = (MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT)

class SpaceInvaders:
  
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(MIN_SCREEN_SIZE, pg.RESIZABLE)
        pg.display.set_caption('Space Invaders')

        self.fps = 60
        self.clock = pg.time.Clock()
        self.running = True
  
        self.init_scenes()
        self.change_scene('menu')

        # Change the scene background size:
        GameScene.background.make_surface(self.screen.get_size())

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
        
        elif ev.type == pg.KEYDOWN and ev.key == pg.K_f:
            # Toggle fullscreen mode:
            size = MIN_SCREEN_SIZE if self.screen.get_flags() & pg.FULLSCREEN else (0, 0)
            self.screen = pg.display.set_mode(size, self.screen.get_flags() ^ pg.FULLSCREEN)

        elif ev.type == pg.WINDOWSIZECHANGED:
            # Validate screen size:
            ev.x = max(ev.x, MIN_SCREEN_WIDTH)
            ev.y = max(ev.y, MIN_SCREEN_HEIGHT)
 
            # Resize without emitting events:
            self.screen = pg.display.set_mode((ev.x, ev.y), self.screen.get_flags())
            pg.event.get(pg.WINDOWSIZECHANGED)
            pg.event.get(pg.VIDEORESIZE)

            # Change the scene background size:
            GameScene.background.make_surface((ev.x, ev.y))

        elif ev.type == CHANGE_SCENE:
            self.change_scene(ev.scene)

    def start(self):
        while self.running:
            for e in pg.event.get(): 
                self.process_event(e)
                self.scene.on_event(e)

            key_state = pg.key.get_pressed()
            game_time = self.clock.get_time()

            self.scene.update(game_time, key_state)
            self.scene.draw(self.screen)
            
            pg.display.flip()
            self.clock.tick(self.fps)

        self.scene.on_exit()
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    game = SpaceInvaders()
    game.start()