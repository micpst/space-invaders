import os
import pygame
from styles import *

pygame.font.init()

ARCADE_IN = {
    S:  pygame.font.Font(os.path.join(os.path.dirname(__file__), '8-bit Arcade In.ttf'), S),
    M:  pygame.font.Font(os.path.join(os.path.dirname(__file__), '8-bit Arcade In.ttf'), M),
    L:  pygame.font.Font(os.path.join(os.path.dirname(__file__), '8-bit Arcade In.ttf'), L),
    XL: pygame.font.Font(os.path.join(os.path.dirname(__file__), '8-bit Arcade In.ttf'), XL)
}

ARCADE_OUT = {
    S:  pygame.font.Font(os.path.join(os.path.dirname(__file__), '8-bit Arcade Out.ttf'), S),
    M:  pygame.font.Font(os.path.join(os.path.dirname(__file__), '8-bit Arcade Out.ttf'), M),
    L:  pygame.font.Font(os.path.join(os.path.dirname(__file__), '8-bit Arcade Out.ttf'), L),
    XL: pygame.font.Font(os.path.join(os.path.dirname(__file__), '8-bit Arcade Out.ttf'), XL)
}