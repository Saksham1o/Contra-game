import os
import pygame

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
DARK_GREEN = (2,207,16)
BLUE = (0,0,255)
SEA_BLUE = (0,86,255)
LIGHT_YELLOW = (255,251,168)
YELLOW = (255,255,0)
DARK_YELLOW = (255,150,2)  


# Project Properties
TITLE = "Contra"
WIDTH = 600
HEIGHT = 480
windowSize = (WIDTH,HEIGHT)
FPS = 60


# Camera

LEFT_BOUND = 0 
RIGHT_BOUND = -6164

# Assets folder
gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder,"img")
soundFolder = os.path.join(gameFolder,"sounds")


# Player

PLAYER_HEALTH = 20
PLAYER_POSX = 100
PLAYER_ACC = 0.5
PLAYER_FRC = -0.12
PLAYER_WIDTH = 35
PLAYER_HEIGHT = 55
GRAVITY = 1
JUMP_HEIGHT = 15
BLINK_TIME = 10
BLINK_DISTANCE = 300
BLINK_SPEED = 20
BLINK_RETRACT = 500
ANIM_SPEED = 5  # Lower the faster

# Powerups
POWERUP_SPEED = 10
POWERUP_TIME = 300

# Bullet 

BULLET_SPEED = 10
BULLET_THRESHOLD = 50

# Sniper
SNIPER_RANGE = 500

LEVEL_1_SNIPERS = [(511,286),
					(695,292),
					(1443,162),
					(2702,100),
					(2767,345),
					(3150,218),
					(4146,251),
					(4652,153),
					(5210,243),
					(5710,344),
					(6469,284)
				]

# Soldier
SOLDIER_SPEEDX = 5
SOLDIER_SPAWN_TIMER = 120

LEVEL_1_SOLDIERS = [(500,10)]

# Tank
TANK_WIDTH = 100
TANK_HEIGHT = 60


LEVEL_1_TANKS = [
					(3620,119),
					(3492,244),
					(5015,297),
					(5610,231),
					(5882,302),
					(6336,364),
					(6327,178)
				]

#platforms
PLATFORM_THICKNESS = 1
pt = PLATFORM_THICKNESS
