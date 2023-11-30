import main
import pygame
import time
import math
import game_logic
from pygame.math import Vector2


class Characters(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, image):
		super().__init__()
		self.width = width
		self.height = height
		self.image = image
		self.image = pygame.transform.scale(self.image, (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def draw(self, screen):
		screen.blit(self.image, self.rect.topleft)




class BadGuy(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, image):
		super().__init__()
		self.bad_guy_sprite = Characters(x, y, width, height, image)
		self.rect = self.bad_guy_sprite.rect
		self.bullets = []
		self.bullet_speed = 3.5
		self.fire_time = 0
		self.direction = 1  # Initial direction of movement, 1 for right, -1 for left
		self.speed = 1  # Movement speed
		self.can_shoot = True
		self.alive = True


		

	
	def update(self, walker,col):
		for man in walker.sprites():
			man.rect.x += self.direction * self.speed
			for column in col:
				if man.rect.colliderect(column):
					self.direction = self.direction * -1
                    # Flip the image horizontally
					self.bad_guy_sprite.image = pygame.transform.flip(self.bad_guy_sprite.image, True, False)

		

	def shoot(self, player_pos,bullet_speed, bullet_height, bullet_width):
		if self.can_shoot:
				#calculate direction
			direction = Vector2((player_pos.centerx) - (self.rect.centerx), (player_pos.centery) - (self.rect.centery))
			if direction.length() != 0:  # Ensure the length is not zero to avoid division by zero
				direction.normalize_ip()

				bullet_pos = Vector2(self.rect.centerx, self.rect.centery)

				bullet_velocity = [direction.x * bullet_speed, direction.y * bullet_speed]
				# Create a bullet instance and add it to the list of bullets, along with position and velocity
				bullet = Bullet(bullet_pos.x, bullet_pos.y, bullet_width, bullet_height, bullet_velocity, pygame.image.load('img/knife.png'))
				self.bullets.append(bullet)

				# Update fire time
				self.fire_time = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds


		
	def timer(self, gametime, player_pos, bullet_height, bullet_width):
		if gametime - self.fire_time >= 3:
			self.shoot(player_pos, self.bullet_speed, bullet_height, bullet_width)
			

	
	def draw(self,screen):
		for bullet in self.bullets:
			bullet.draw(screen)
		self.bad_guy_sprite.draw(screen)
	

	def bullet_detect_env(self, bullet_col): 
		for bullet in self.bullets:
			for tile in bullet_col:
				if bullet.rect.colliderect(tile[1]):  # Assuming tile is a pair (image, rect)
					self.bullets.remove(bullet)
	
	def disable_shooting(self):
		self.can_shoot = False

	def not_alive(self):
		self.alive = False

	def shoot_kill_character(self,player,gameover):
		for bullet in self.bullets:
			if bullet.rect.colliderect(player):
				gameover.show_game_over_screen()
				bullet.kill()

	def walk_kill_character(self,player,gameover):
		if self.alive:
			if self.rect.colliderect(player):
				gameover.show_game_over_screen()


	@property
	def image(self):
		return self.bad_guy_sprite.image
	





class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, bullet_width, bullet_height, velocity, image):
		super().__init__()
		self.image = pygame.Surface((bullet_width, bullet_height))
		self.image.fill((255, 0, 0))  # You can customize the color
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.velocity = velocity
		angle = math.atan2(velocity[1], velocity[0])
		self.image = image
		self.image = pygame.transform.rotate(self.image, 180-math.degrees(angle))
		self.image = pygame.transform.scale(self.image, (bullet_width, bullet_height))
		self.last_update_time = pygame.time.get_ticks()
	def update(self):
		elapsed_time = pygame.time.get_ticks() - self.last_update_time
		self.rect.centerx += self.velocity[0] * elapsed_time / 1000
		self.rect.centery += self.velocity[1] * elapsed_time / 1000
		

	#method to draw bullet
	def draw(self, screen):
		screen.blit(self.image, self.rect)
		






