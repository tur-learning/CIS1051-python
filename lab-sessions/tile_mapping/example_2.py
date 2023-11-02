import pygame
from pygame.locals import *
from GameObjects import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tile mapping example')

# define game variables
tile_size = 100
n_tiles = screen_width//tile_size

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

worldmap = WorldMap(map, tile_size)

run = True
while run:

	screen.blit(bg_img, (0, 0))
	worldmap.draw(screen)

	draw_grid()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
