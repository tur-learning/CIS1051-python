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
		self.speed = 2  # Movement speed


		self.rect.x += self.direction * self.speed

	
	def shoot(self, player_pos,bullet_speed, bullet_height, bullet_width):
		if game_logic.can_shoot:
				#calculate direction
			direction = Vector2((player_pos[0]) - (self.rect.x), (player_pos[1]) - (self.rect.y))
		
			if direction.length() != 0:  # Ensure the length is not zero to avoid division by zero
				direction.normalize_ip()

				bullet_pos = Vector2(self.rect.x + 20, self.rect.y)

				bullet_velocity = [direction.x * bullet_speed, direction.y * bullet_speed]
				# Create a bullet instance and add it to the list of bullets, along with position and velocity
				bullet = Bullet(bullet_pos.x, bullet_pos.y, bullet_width, bullet_height, bullet_velocity)
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
		bullets_to_remove = []
		for bullet in self.bullets[:]:  # Iterate over a copy of the list
			for tile in bullet_col:
				if bullet.rect.colliderect(tile[1]):  # Assuming tile is a pair (image, rect)
					bullets_to_remove.append(bullet)
		for bullet in bullets_to_remove:
			self.bullets.remove(bullet)
	@property
	def image(self):
		return self.bad_guy_sprite.image
	
	def update(self,badguy, columns):
        # Update the position based on the current direction and speed
		self.rect.x += self.direction * self.speed

        # Check for collision with columns
		for column in columns:
			for man in badguy.sprites:
				if man.colliderect(column):
					# Change the direction if there is a collision
					self.direction *= -1
					break



class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, bullet_width, bullet_height, velocity):
		super().__init__()
		self.image = pygame.Surface((bullet_width, bullet_height))
		self.image.fill((255, 0, 0))  # You can customize the color
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.velocity = velocity
	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	#method to draw bullet
	def draw(self, screen):
		pygame.draw.rect(screen, (255, 0, 0), self.rect)





all_sprites = pygame.sprite.Group()
walking_sprites = pygame.sprite.Group()
enemy1 = BadGuy(game_logic.enemy_pos[0], game_logic.enemy_pos[1], 40, 50, pygame.image.load('img/roman_soldier.png'))
enemy2 = BadGuy(500,450,40,50,pygame.image.load('img/roman_soldier.png'))
all_sprites.add(enemy1, enemy2)
walking_sprites.add(enemy2)