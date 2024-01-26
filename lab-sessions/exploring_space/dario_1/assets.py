import pygame
import game

zoom_1 = 20*0.6
zoom_2 = 20

ship_speed = 1
shot_speed = 0.2

# Loading images to be displayed
background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, (game.window_x*zoom_1, game.window_y*zoom_1))
bg_frame = background.get_rect()

ship = pygame.image.load("assets/spaceship.png").convert_alpha()
ship = pygame.transform.scale(ship, (game.window_x/zoom_2, game.window_y/zoom_2))

target = pygame.image.load("assets/target.png").convert_alpha()
target = pygame.transform.scale(target, (game.window_x/zoom_2, game.window_y/zoom_2))
target_rect = target.get_rect()

shot = pygame.image.load("assets/shot.png").convert_alpha()
shot = pygame.transform.scale(shot, (game.window_x/zoom_2, game.window_y/zoom_2))
shot_rect = shot.get_rect()
