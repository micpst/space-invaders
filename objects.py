import pygame
from assets import *

class Ship:
    def __init__(self, x, y, ship_velocity, laser_velocity, hp=100):
        self.x = x
        self.y = y 
        self.hp = hp
        self.max_hp = hp
        self.ship_img = None
        self.laser_img = None
        self.ship_velocity = ship_velocity
        self.laser_velocity = laser_velocity
        self.cooldown_counter= 0

    @property
    def height(self):
        return self.ship_img.get_height()

    @property
    def width(self):
        return self.ship_img.get_width()
        
    def move_up(self):
        self.y -= self.ship_velocity

    def move_down(self):
        self.y += self.ship_velocity

    def move_left(self):
        self.x -= self.ship_velocity

    def move_right(self):
        self.x += self.ship_velocity     

    def collide(self, obj):
        offset_x = obj.x - self.x
        offset_y = obj.y- self.y
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) != None

class Player(Ship):
    COLOR_MAP = {   
        'yellow': (YELLOW_SPACE_SHIP, YELLOW_LASER),
    }

    def __init__(self, x, y, ship_velocity, laser_velocity, color, hp=100):
        super().__init__(x, y, ship_velocity, laser_velocity, hp)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def shoot(self):
        laser = Laser(self, self.x, self.y-35)
        self.cooldown_counter = 1
        return laser

class Enemy(Ship):
    COLOR_MAP = {   
        'green': (GREEN_SPACE_SHIP, GREEN_LASER),
        'blue': (BLUE_SPACE_SHIP, BLUE_LASER),
        'red': (RED_SPACE_SHIP, RED_LASER)
    }

    def __init__(self, x, y, ship_velocity, laser_velocity, color, hp=100):
        super().__init__(x, y, ship_velocity, laser_velocity, hp)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def shoot(self):    
        laser = Laser(self, self.x-18, self.y)
        self.cooldown_counter = 1
        return laser

class Laser:
    def __init__(self, src, x, y):
       self.x = x
       self.y = y
       self.src = src
       self.img = self.src.laser_img
       self.velocity = self.src.laser_velocity
       self.mask = pygame.mask.from_surface(self.img)

    def move_up(self):
        self.y -= self.velocity

    def move_down(self):
        self.y += self.velocity
            
    def collide(self, obj):
        offset_x = obj.x - self.x
        offset_y = obj.y- self.y
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) != None