import random
import pygame
from objects import Player, Enemy

class GameEngine:
    def __init__(
        self, 
        resolution=(750,750), 
        player_velocity=8, 
        enemy_velocity=2, 
        laser_velocity=7, 
        wave_length=5, 
        player_color='yellow'
    ):
        self.window_width, self.window_height = resolution 
        self.player_velocity = player_velocity
        self.enemy_velocity = enemy_velocity 
        self.laser_velocity = laser_velocity
        self.wave_length = wave_length
          
        self.player = Player(300, 630, player_velocity, laser_velocity, player_color)
        self.enemies = []
        self.lasers= []
        
        self.level = 0
        self.lives = 3
        self.max_lives = 3
        self.score = 0
        self.lost = False 
        self.cooldown = 10   

    def is_off_screen(self, obj):
        return not(obj.y <= self.window_height and obj.y >= 0)

    def count_cooldown(self):
        objects = [self.player] + self.enemies if self.player else self.enemies
        for obj in objects:
            if obj.cooldown_counter == self.cooldown:
                obj.cooldown_counter = 0
            elif obj.cooldown_counter > 0:
                obj.cooldown_counter += 1

    def spawn_wave(self):
        for i in range(self.wave_length):
            x = random.randrange(100, self.window_width - 100)
            y = random.randrange(-1500, -100)
            color = random.choice(['red', 'green', 'blue'])
            enemy = Enemy(x, y, self.enemy_velocity, self.laser_velocity, color)
            self.enemies.append(enemy)

    def move_wave(self):
        for enemy in self.enemies:
            enemy.move_down()

            if self.window_height > enemy.y + enemy.height > 0 and random.randrange(0, 4*60) == 1:
                if enemy.cooldown_counter == 0:
                    laser = enemy.shoot()
                    self.lasers.append(laser)

            if self.player and enemy.collide(self.player):
                self.player.hp -= 15
                self.enemies.remove(enemy)

            elif enemy.y + enemy.height > self.window_height:
                if self.lives > 0:
                    self.lives -= 1
                self.enemies.remove(enemy)

    def move_lasers(self):
        player_lasers = [laser for laser in self.lasers if type(laser.src) == Player]
        enemy_lasers = [laser for laser in self.lasers if type(laser.src) == Enemy]

        for laser in player_lasers:
            laser.move_up()

            if self.is_off_screen(laser):
                self.lasers.remove(laser)
            else:
                for enemy in self.enemies:
                    if laser.collide(enemy):
                        self.score += 10
                        self.enemies.remove(enemy)

                        if laser in self.lasers:
                            self.lasers.remove(laser)
                           
        for laser in enemy_lasers:
            laser.move_down()

            if self.is_off_screen(laser):
                self.lasers.remove(laser)

            elif self.player and laser.collide(self.player):
                self.player.hp -= 10
                self.lasers.remove(laser)

    def navigate(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.player.x - self.player_velocity > 0:
            self.player.move_left()

        if keys[pygame.K_d] and self.player.x + self.player_velocity + self.player.width < self.window_width:
            self.player.move_right()   

        if keys[pygame.K_w] and self.player.y - self.player_velocity > 0:
            self.player.move_up()

        if keys[pygame.K_s] and self.player.y + self.player_velocity + self.player.height + 25 < self.window_height:
            self.player.move_down()

        if keys[pygame.K_SPACE]:
            if self.player.cooldown_counter == 0:
                laser = self.player.shoot()
                self.lasers.append(laser)

    def compute(self):
        if self.lives <= 0 or self.player and self.player.hp <= 0:
            self.player = None
            self.lost = True

        if len(self.enemies) == 0:
            self.level += 1
            self.wave_length += 5
            self.spawn_wave()

        self.move_wave()
        self.move_lasers()
        self.count_cooldown()