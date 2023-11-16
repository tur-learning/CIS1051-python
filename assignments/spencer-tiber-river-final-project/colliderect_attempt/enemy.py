import main
import pygame
import time
import math
import game_logic



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
		self.bullet_speed = 2
		self.fire_time = 0

	#def update(self, sprites, col):
	#	game_logic.delta_x = 2
		
	#	for tile in col:
	#		if sprites.rect.colliderect(col):
	#			game_logic.delta_x = -1*(game_logic.delta_x)
	#	for man in sprites:
	#		man.x = man.x + game_logic.delta_x

	
	def shoot(self, player_pos,bullet_speed, bullet_height, bullet_width):
		#calculate direction
		direction = [player_pos[0] - self.rect.x, player_pos[1] - self.rect.y]

        # Normalize direction vector
		length = math.sqrt(direction[0]**2 + direction[1]**2)
		if length != 0:
			direction = [direction[0] / length, direction[1] / length]

        # Set the bullet's velocity based on normalized speed that isnt working
		bullet_velocity = [direction[0] * bullet_speed, direction[1] * bullet_speed]

        # Create a bullet instance and add it to list of bullets, along with position and velocity
		bullet = Bullet(self.rect.x, self.rect.y, bullet_width, bullet_height, bullet_velocity)
		self.bullets.append(bullet)

		# Update firetime
		self.fire_time = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds

		
	def timer(self, gametime, player_pos, bullet_speed, bullet_height, bullet_width):
		if gametime - self.fire_time >= 3:
			self.shoot(player_pos, bullet_speed, bullet_height, bullet_width)

	
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
	


class Bullet(pygame.sprite.Sprite):
	#need to figure out the width and stuff
	def __init__(self, x, y, bullet_width, bullet_height, velocity):
		self.rect = pygame.Rect(x, y, bullet_width, bullet_height)
		self.velocity = velocity


	# Update the position based on the velocity
	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	#method to draw bullet
	def draw(self, screen):
		pygame.draw.rect(screen, (255, 0, 0), self.rect)





all_sprites = pygame.sprite.Group()
walking_sprites = pygame.sprite.Group()
enemy1 = BadGuy(game_logic.enemy_pos[0], game_logic.enemy_pos[1], 40, 50, pygame.image.load('img/roman_soldier.png'))
enemy2 = BadGuy(500,465,40,50,pygame.image.load('img/roman_soldier.png'))
all_sprites.add(enemy1, enemy2)
walking_sprites.add(enemy2)