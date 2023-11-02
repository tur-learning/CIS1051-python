import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tile mapping example')

# define game variables
tile_size = 100
n_tiles = screen_width//tile_size
print(n_tiles)

#load images
bg_img = pygame.image.load('img/sky.png')

def draw_grid():
	for n in range(0, n_tiles):
		pygame.draw.line(screen, (255, 255, 255), (0, n * tile_size), (screen_width, n * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (n * tile_size, 0), (n * tile_size, screen_height))

map = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 3, 3, 3, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 3, 3, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 3, 3, 1],
	[1, 0, 0, 0, 0, 3, 3, 2, 2, 1],
	[1, 0, 0, 3, 3, 2, 2, 2, 2, 1],
	[1, 0, 3, 2, 2, 2, 2, 2, 2, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Load images
brick_img = pygame.image.load('img/brick.png')
dirt_img = pygame.image.load('img/dirt.png')
grass_img = pygame.image.load('img/grass.png')

# Initialize empty tile list
tile_list = []

# Loop over each map element and 
# assing it the correct image
row_count = 0
for row in map:
    col_count = 0
    for tile in row:
        if tile == 1:
            img = pygame.transform.scale(brick_img, (tile_size, tile_size))
            img_rect = img.get_rect()
            img_rect.x = col_count * tile_size
            img_rect.y = row_count * tile_size
            tile = [img, img_rect]
            tile_list.append(tile)
        if tile == 2:
            img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
            img_rect = img.get_rect()
            img_rect.x = col_count * tile_size
            img_rect.y = row_count * tile_size
            tile = [img, img_rect]
            tile_list.append(tile)
        if tile == 3:
            img = pygame.transform.scale(grass_img, (tile_size, tile_size))
            img_rect = img.get_rect()
            img_rect.x = col_count * tile_size
            img_rect.y = row_count * tile_size
            tile = [img, img_rect]
            tile_list.append(tile)
        col_count += 1
    row_count += 1

run = True
while run:

	screen.blit(bg_img, (0, 0))

	for tile in tile_list:
		screen.blit(tile[0], tile[1])

	draw_grid()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()