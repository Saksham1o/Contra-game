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
		
    def new(self):
		self.reinit()
		self.run()

	def run(self):
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
	def deathAnim(self,sprite):
		d = Death(sprite.rect.left,sprite.rect.top)
		self.death_anims.add(d)
		self.all_sprites.add(d)
	def update(self):
		self.time += 1
		if not self.bosses:
			self.playing = False
		self.soldierTimer -= 1
		self.powerupTimer -= 1
		self.soldierTimer %= SOLDIER_SPAWN_TIMER
		if self.soldierTimer == 0:
			self.soldierTimer = SOLDIER_SPAWN_TIMER
			s = Soldier(random.randint(int(p.pos.x+600),int(p.pos.x+800)),random.randint(int(p.pos.y),int(p.pos.y+300)))
			self.soldiers.add(s)
			self.all_sprites.add(s)

		if self.powerupTimer == 0:
			self.powerupTimer = POWERUP_TIME
			po = Powerup(random.randint(int(p.pos.x+300),int(p.pos.x+600)),random.randint(0,3))
			self.powerups.add(po)
			self.all_sprites.add(po)
		self.health = p.health
		self.blinkRetract = p.blinkRetract
		self.all_sprites.update()
		h.update_HUD(self)
		camera.update(p)
		# Check if player fell off screen
		if p.rect.top > HEIGHT or p.rect.x < 0:
			p.die()
			self.deathAnim(p)		
			self.playing = False
		# Check if any enemy dies
		h1 = pygame.sprite.groupcollide(g.bullets,g.snipers,True,True)
		if h1:
			for k in h1:
				self.deathAnim(k)
		h1 = pygame.sprite.groupcollide(g.bullets,g.soldiers,True,True)
		if h1:
			for k in h1:
				self.deathAnim(k)
		h1 = pygame.sprite.groupcollide(g.bullets,g.tanks,True,True)
		if h1:
			for k in h1:
				self.deathAnim(k)

		# Check player colliding with any bullet
		hits = pygame.sprite.spritecollide(p,g.enemy_bullets,True)
		if hits:
			p.health -= 1
			hit_sound.play()
			if p.health == 0:
				p.die()
				self.deathAnim(p)
				self.playing = False
				
        # or enemy
		h1 = pygame.sprite.spritecollide(p,g.snipers,False)
		if h1:
			p.die()
			self.deathAnim(p)
			self.playing = False
		h1 =  pygame.sprite.spritecollide(p,g.soldiers,False)
		if h1:
			p.die()
			self.deathAnim(p)
			self.playing = False
		h1 = pygame.sprite.spritecollide(p,g.tanks,False)
		if h1:
			p.die()
			self.deathAnim(p)
			self.playing = False
