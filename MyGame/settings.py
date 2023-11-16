# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

import random
from random import randint
# game settings 
WIDTH = 1440
HEIGHT = 960
FPS = 25


# player settings
PLAYER_JUMP = 27
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)


def set_pos(self,x_pos, y_pos):
    self.rect.x = x_pos
    self.rect.y = y_pos

GROUND = (0, HEIGHT - 40, WIDTH, 40, "normal")


# Platform info
PLATFORM_LIST = [
    (0, HEIGHT - 40, WIDTH, 40, "normal"),
    (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, "normal"),
    (125, HEIGHT - 350, 100, 20, "moving"),
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"), 
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"),  
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"), 
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"),  
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"),  
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"),  
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"),  
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"),  
    (randint(50, WIDTH - 150), randint(50, HEIGHT - 50), 100, 20, "normal"),  
    (WIDTH / 2 - 50, HEIGHT - 100, 100, 20, "moving"),  
    (WIDTH / 2 - 50, randint(50, HEIGHT - 150), 100, 20, "moving"),  
]


