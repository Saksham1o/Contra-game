# sprites of the game

import pygame
from camera import *
from settings import *
from graphics import *
vec = pygame.math.Vector2


all_sprites = pygame.sprite.Group()

# Player States
RIGHT = 0
LEFT = 1
RIGHT_DOWN = 2
RIGHT_UP = 3
LEFT_UP = 4
LEFT_DOWN = 5