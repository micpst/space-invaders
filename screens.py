import os
import sys
import yaml
import pygame

from objects import Enemy, YELLOW_SPACE_SHIP
from engine import GameEngine

pygame.font.init()

class Screen:
    clock = pygame.time.Clock()
    FPS = 120
    
    resolution = (750, 750)
    width, height = resolution
    window = pygame.display.set_mode(resolution)
    
    background = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background-black.png')), resolution)
    title = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'logo.png')), (450, 175))
    
    font_70 = pygame.font.SysFont('comicsans', 70)
    font_60 = pygame.font.SysFont('comicsans', 60)
    font_50 = pygame.font.SysFont('comicsans', 50)
    font_40 = pygame.font.SysFont('comicsans', 40)

    config_file = open('_config.yaml', 'r')
    game_config = yaml.safe_load(config_file)

    y1 = 0
    y2 = -height

    def animate_background(self):
        self.window.blit(self.background, (0, self.y1))
        self.window.blit(self.background, (0, self.y2))

        self.y1 += 1
        self.y2 += 1

        if self.y1 > self.height:
            self.y1 = -self.height

        if self.y2 > self.height:
            self.y2 = -self.height

    def save(self):
        with open('_config.yaml', 'w') as f:
            yaml.dump(self.game_config, f)

class MainMenu(Screen):
    def __init__(self):
        super().__init__()
        self.selected = 0
        pygame.display.set_caption('Space Invaders')

    @property
    def options(self):
        color = lambda i: (230, 230, 0) if i == self.selected else (255, 255, 255)
        return [
            self.font_60.render('Play',     1, color(0)),
            self.font_60.render('Settings', 1, color(1)),
            self.font_60.render('Exit',     1, color(2)),
        ]

    def render(self):
        super().animate_background() 
        self.window.blit(self.title, (self.width/2 - self.title.get_width()/2, 125))

        y = 350
        for option in self.options:
            self.window.blit(option, (self.width/2 - option.get_width()/2, y))
            y += 65

    def navigate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.selected == 0:
                        self.selected = len(self.options) - 1
                    else:
                        self.selected -= 1

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if len(self.options) - 1 == self.selected:
                        self.selected = 0
                    else:
                        self.selected += 1

                elif event.key == pygame.K_RETURN and self.selected == 0:
                    game_screen = Game()
                    game_screen.run()

                    lost_screen = Scoreboard(game_screen.engine.score)
                    lost_screen.run()

                elif event.key == pygame.K_RETURN and self.selected == 1:
                    settings_screen = Settings()
                    settings_screen.run()

                elif event.key == pygame.K_RETURN and self.selected == 2:
                    pygame.quit()
                    sys.exit(0)

    def run(self):
        while True:
            self.render()
            self.navigate()
            
            pygame.display.update()
            self.clock.tick(self.FPS)       

class Settings(Screen):   
    def __init__(self):
        super().__init__()
        self.title = self.font_70.render('Settings', 1, (255, 255, 255))
        self.save = self.font_40.render('[ENTER] Save', 1, (255, 255, 255))
        self.exit = self.font_40.render('[ESC] Exit', 1, (255, 255, 255))

        self.settings = self.game_config['settings']
        self.models = { 'yellow': YELLOW_SPACE_SHIP }
        self.selected = 0
        self.running = True

    @property
    def options(self):
        color = lambda i: (230, 230, 0) if i == self.selected else (255, 255, 255)    
        return [    
            self.font_50.render(f"Player speed: {self.settings['player_velocity']}", 1, color(0)),
            self.font_50.render(f"Enemy speed: {self.settings['enemy_velocity']}",   1, color(1)),
            self.font_50.render(f"Wave length: {self.settings['wave_length']}",      1, color(2)),
            self.font_50.render(f"Player ship: {self.settings['player_color']}",     1, color(3)),
        ]

    @property
    def ship_model(self): 
        return self.models[self.settings['player_color']]

    def render(self):   
        super().animate_background()
        self.window.blit(self.title, (self.width/2 - self.title.get_width()/2, 200))

        y = 300
        for option in self.options:
            self.window.blit(option, (self.width/2 - option.get_width()/2, y))
            y += 60

        self.window.blit(self.ship_model, (self.width/2 - self.ship_model.get_width()/2, y + 20))

        self.window.blit(self.save, (40, self.height - self.save.get_height() - 40))
        self.window.blit(self.exit, (self.width - self.exit.get_width() - 40, self.height - self.exit.get_height() - 40))

    def navigate(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP or e.key == pygame.K_w:
                    if self.selected == 0:
                        self.selected = len(self.options) - 1
                    else:
                        self.selected -= 1

                elif e.key == pygame.K_DOWN or e.key == pygame.K_s:
                    if len(self.options) - 1 == self.selected:
                        self.selected = 0
                    else:
                        self.selected += 1

                elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                    if self.selected == 0: self.settings['player_velocity'] -= 1
                    if self.selected == 1: self.settings['enemy_velocity'] -= 1
                    if self.selected == 2: self.settings['wave_length'] -= 5

                elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                    if self.selected == 0: self.settings['player_velocity'] += 1
                    if self.selected == 1: self.settings['enemy_velocity'] += 1
                    if self.selected == 2: self.settings['wave_length'] += 5

                elif e.key == pygame.K_RETURN: 
                    self.game_config['settings'] = self.settings
                    super().save()
                    self.running = False

                elif e.key == pygame.K_ESCAPE:
                    self.running = False

    def run(self):
        while self.running:
            self.render()
            self.navigate()

            pygame.display.update()
            self.clock.tick(self.FPS)

class Game(Screen):
    def __init__(self):
        super().__init__()
        self.engine = GameEngine(self.resolution, **self.game_config['settings'])
        self.full_hearth = pygame.image.load(os.path.join('assets', 'hearth_full.png'))
        self.empty_hearth = pygame.image.load(os.path.join('assets', 'hearth_empty.png'))
        self.lost_overrun = 0
        self.running = True

    @property
    def lives(self):
        active_lives = [self.full_hearth] * self.engine.lives
        lost_lives = [self.empty_hearth] * (self.engine.max_lives - self.engine.lives)     
        return active_lives + lost_lives

    @property
    def level(self):
        return self.font_50.render(f'Level: {self.engine.level}', 1, (255, 255, 255))

    @property
    def score(self):
        return self.font_50.render(f'Score: {self.engine.score}', 1, (255, 255, 255))

    def render(self): 
        super().animate_background() 

        if self.engine.player:  
            self.window.blit(self.engine.player.ship_img, (self.engine.player.x, self.engine.player.y))
            
            pygame.draw.rect(self.window, (200, 0, 0), ((self.engine.player.x, self.engine.player.y + self.engine.player.height + 10, self.engine.player.width, 10)))
            pygame.draw.rect(self.window, (0, 200, 0), ((self.engine.player.x, self.engine.player.y + self.engine.player.height + 10, self.engine.player.width * (self.engine.player.hp / self.engine.player.max_hp), 10)))

        for enemy in self.engine.enemies:
            self.window.blit(enemy.ship_img, (enemy.x, enemy.y))

        for laser in self.engine.lasers:
            self.window.blit(laser.src.laser_img, (laser.x, laser.y))

        x = 10
        for life in self.lives:
            self.window.blit(life, (x, 10))
            x += life.get_width() + 5

        self.window.blit(self.level, (self.width - self.level.get_width() - 10, 10))
        self.window.blit(self.score, (self.width - self.score.get_width() - 10, 60))
   
    def run(self):
        while self.running:
            self.render()
            self.engine.compute()

            if self.engine.lost:
                if self.lost_overrun > self.FPS * 2:
                    self.running = False
                else:
                    self.lost_overrun += 1
            else:
                self.engine.navigate()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            pygame.display.update()
            self.clock.tick(self.FPS)

class Scoreboard(Screen):
    def __init__(self, score):
        super().__init__()    
        self.lost = self.font_60.render('GAME OVER', 1, (255, 255, 255))     
        self.score_1 = self.font_50.render(f'Your score: {score}', 1, (255, 255, 255))
        self.score_2 = self.font_50.render(f"Highest score: {self.game_config['game']['highest_score']}", 1, (255, 255, 255))
        self.info = self.font_40.render(f'Press [ENTER] to continue.', 1, (255, 255, 255))
        self.running = True

        if self.game_config['game']['highest_score'] < score:
            self.game_config['game']['highest_score'] = score
            super().save()

    def render(self): 
        super().animate_background()
        self.window.blit(self.title, (self.width/2 - self.title.get_width()/2, 125))
        self.window.blit(self.lost, (self.width/2 - self.lost.get_width()/2, 320))
        self.window.blit(self.score_1, (self.width/2 - self.score_1.get_width()/2, 400))
        self.window.blit(self.score_2, (self.width/2 - self.score_2.get_width()/2, 450))
        self.window.blit(self.info, (self.width/2 - self.info.get_width()/2, 550))                 

    def navigate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.running = False

    def run(self):
        while self.running:
            self.render()
            self.navigate()
            
            pygame.display.update()
            self.clock.tick(self.FPS)
