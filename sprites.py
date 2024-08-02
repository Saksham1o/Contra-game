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

class Player(pygame.sprite.Sprite):
	def __init__(self,game):

		
		pygame.sprite.Sprite.__init__(self)

		# Copy of Game
		self.game = game

		self.image = pygame.transform.scale(PLAYER_RIGHT_0,(PLAYER_WIDTH,PLAYER_HEIGHT))
		self.image.set_colorkey(YELLOW)
		self.rect = self.image.get_rect()
		self.rect.center = (PLAYER_POSX,0)
		self.health = PLAYER_HEALTH

		# Movement
		self.state = RIGHT
		self.up = False
		self.down = False
		self.pos = vec(30,30)
		self.vel = vec(0,0)
		self.acc = vec(0,GRAVITY)
		self.canMove = True
		self.jumping = True
		self.facing = 1

		# Jumping
		self.canJump = False
		self.collisions = True

		# Blinking
		self.blinkTime = BLINK_TIME
		self.canBlink = 1
		self.blinking = False
		self.blinkRetract = BLINK_RETRACT


		self.dead = False
		# Animation
		# Frames hold each frame
		# index determines the current frame to be played
		self.animCounter = ANIM_SPEED

		self.jumpFrames = [PLAYER_JUMP_0,PLAYER_JUMP_1,PLAYER_JUMP_2,PLAYER_JUMP_3]
		self.jumpIndex = 0

		self.rightFrames = [PLAYER_RIGHT_0,PLAYER_RIGHT_1,PLAYER_RIGHT_2,PLAYER_RIGHT_3,PLAYER_RIGHT_4,PLAYER_RIGHT_5]
		self.rightIndex = 0

		self.rightUpFrames = [PLAYER_RIGHT_UP_0,PLAYER_RIGHT_UP_1,PLAYER_RIGHT_UP_2]
		self.rightUpIndex = 0

		self.rightDownFrames =  [PLAYER_RIGHT_DOWN_0,PLAYER_RIGHT_DOWN_1,PLAYER_RIGHT_DOWN_2]
		self.rightDownIndex = 0

		self.deadFrames = [PLAYER_DEAD_0,PLAYER_DEAD_1,PLAYER_DEAD_2,PLAYER_DEAD_3,PLAYER_DEAD_4]
		self.deadIndex = 0
