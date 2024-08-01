# Contra with Dash


# Pygame Template

import os
import random
import sys
import pygame
from settings import *
from sprites import *
from camera import *
from graphics import *


# Game template class

class Game:
	def __init__(self):		
		# Initialize
		size = width, height = 600, 480
		if "-f" in sys.argv[1:]:
			self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
		else:
			self.screen = screen
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.soldierTimer = SOLDIER_SPAWN_TIMER
		self.reinit()

	def reinit(self):
		self.all_sprites = pygame.sprite.Group()
		self.grounds = pygame.sprite.Group()
		self.player_sprite = pygame.sprite.Group()
		self.bg_sprite = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.snipers = pygame.sprite.Group()
		self.soldiers = pygame.sprite.Group()
		self.enemy_bullets = pygame.sprite.Group()
		self.tanks = pygame.sprite.Group()
		self.powerups = pygame.sprite.Group()
		self.bosses = pygame.sprite.Group()
		self.death_anims = pygame.sprite.Group()
		self.health = PLAYER_HEALTH
		self.soldierTimer = SOLDIER_SPAWN_TIMER
		self.powerupTimer = POWERUP_TIME
		self.blinkRetract = BLINK_RETRACT
		self.time = 0
