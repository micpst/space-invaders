import os
import pygame

BACKGROUND        = pygame.image.load(os.path.join(os.path.dirname(__file__), "background.png"))
LOGO              = pygame.image.load(os.path.join(os.path.dirname(__file__), "logo.png"))
FULL_HEARTH       = pygame.image.load(os.path.join(os.path.dirname(__file__), "hearth_full.png"))
EMPTY_HEARTH      = pygame.image.load(os.path.join(os.path.dirname(__file__), "hearth_empty.png"))
GREEN_SPACE_SHIP  = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP   = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixel_ship_blue_small.png"))
RED_SPACE_SHIP    = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixel_ship_red_small.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixel_ship_yellow.png"))
YELLOW_LASER      = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixel_laser_yellow.png"))
GREEN_LASER       = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixel_laser_green.png"))
BLUE_LASER        = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixel_laser_blue.png"))
RED_LASER         = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixel_laser_red.png"))