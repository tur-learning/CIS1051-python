import math
import pygame
import pygame_menu
import random
import time
import game
import GameObject
from GameObject import Planet
from GameObject import Enemy
from GameObject import Spaceship
from GameObject import Crosshair
from GameObject import Shot
import shelve

# Load the extended background image and its dimensions
extended_background = pygame.image.load("background1v2.png").convert_alpha()
new_width, new_height = extended_background.get_size()
background = pygame.transform.scale(extended_background, (new_width, new_height))
map = ["background1v2.png"]

moving_objects_surface = pygame.Surface((new_width, new_height), pygame.SRCALPHA)

planet_image_path = "planet.png"
earth = Planet(200, 200, 200, planet_image_path)

testPlanet = GameObject.Planet(700, 700, 100, planet_image_path)

enemy_image_path = "enemy.png"
alien = Enemy(600, 600, 50, enemy_image_path)

def update_background(image_path):
    global background, new_width, new_height, bg_frame
    background = pygame.image.load(image_path).convert_alpha()
    background = pygame.transform.scale(background, (new_width, new_height))
    bg_frame = background.get_rect()
    new_width = background.get_width()
    new_height = background.get_height()

def set_map(_, value):
    map[0] = value
    update_background(value)

# Loading images to be displayed
zoom_1 = 1
zoom_2 = 0.1
zoom_3 = 0.04
zoom_4 = 0.02
tip_offset = 75

#ADDED CODE
background = pygame.image.load(map[0]).convert_alpha()
update_background(map[0])
background = pygame.transform.scale(background, (new_width, new_height))
bg_frame = background.get_rect()
new_width = background.get_width()
new_height = background.get_height()

spaceship = Spaceship(630, 330, 50, "spaceship.png")

crosshair_width = int(game.window_x * zoom_3)
crosshair_height = int(game.window_y * zoom_3)
crosshair = Crosshair(0, 0, crosshair_width, crosshair_height, "crosshair.png")

shot_width = int(game.window_x * zoom_4)
shot_height = int(game.window_y * zoom_4)
shot = Shot(750, 750, shot_width, shot_height, "shot.png")

movement = [0, 0]
speed = 15

# ADDED CODE
def show_periodic_background(x1, y1, background_with_objects):
    x1 = (new_width  + x1 + movement[0]) % new_width
    y1 = (new_height + y1 + movement[1]) % new_height

    v1 = (x1, y1)
    v2 = ( 0, y1)
    v3 = ( 0,  0)
    v4 = (x1,  0)

    window_frame = pygame.Rect(v1, (game.window_x, game.window_y))

    w2 = max(0, window_frame.right - new_width)
    w1 = window_frame.width - w2
    w3 = w2 ; w4 = w1

    h4 = max(0, window_frame.bottom - new_height)
    h1 = window_frame.height - h4
    h2 = h1 ; h3 = h4
        
    quad_1 = pygame.Rect(v1, (w1, h1))
    quad_2 = pygame.Rect(v2, (w2, h2))
    quad_3 = pygame.Rect(v3, (w3, h3))
    quad_4 = pygame.Rect(v4, (w4, h4))

    game.game_window.blit(background_with_objects, (0,0), quad_1)
    game.game_window.blit(background_with_objects, (w1,0), quad_2)
    game.game_window.blit(background_with_objects, (w1,h1), quad_3)
    game.game_window.blit(background_with_objects, (0,h1), quad_4)

    return x1, y1


# Initialization
pygame.init()

def start():

    enemy_group = pygame.sprite.Group()
    enemy_group.add(alien)
    shot_speed = 50
    
    x1 = game.window_x / 2
    y1 = game.window_y / 2

    fps = pygame.time.Clock()

    # Scrolling variable
    scroll = 0

    # Amount of maximum contemporary repetitions of the background
    # over the game window
    tiles = math.ceil(game.window_x / background.get_width()) + 1

    # Initialize the shot position and shot_active flag
    shot_pos = [0, 0]
    shot_active = False

    spaceship_pos = [630, 330]  # Adjust this to match the spaceship's initial position
    background_with_objects = background.copy()

    enemy_group = pygame.sprite.Group()

    # Main loop
    while True:
        # Setting the fps
        fps.tick(30)
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            movement[0] = speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            movement[0] = -speed
        else:
            movement[0] = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            movement[1] = -speed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            movement[1] = speed
        else:
            movement[1] = 0

        if keys[pygame.K_p]:
            spaceship.save("spaceship_data", "spaceship_data")

        crosshair.x_coordinate, crosshair.y_coordinate = pygame.mouse.get_pos()

        x1, y1 = show_periodic_background(x1, y1, background_with_objects)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if not shot_active and (event.type == pygame.MOUSEBUTTONDOWN):
                shot_active = True
                tip_x = spaceship_pos[0] + spaceship.get_width() / 2 + math.cos(angle_rad) * tip_offset
                tip_y = spaceship_pos[1] + spaceship.get_height() / 2 + math.sin(angle_rad) * tip_offset
                shot.x_coordinate, shot.y_coordinate = tip_x, tip_y
                crosshair_pos = pygame.mouse.get_pos()
                shot.set_direction((tip_x, tip_y), crosshair_pos)

        # Get the angle between the spaceship and the mouse position
        mouse_pos = pygame.mouse.get_pos()
        angle_rad = math.atan2(mouse_pos[1] - (spaceship_pos[1] + spaceship.get_height() / 2),
                               mouse_pos[0] - (spaceship_pos[0] + spaceship.get_width() / 2))
        angle_deg = math.degrees(angle_rad) - 90

        spaceship.rotate(*pygame.mouse.get_pos())
        spaceship.draw(game.game_window)

        if shot_active:
            shot.move(shot_speed)
            shot_pos = [shot.x_coordinate, shot.y_coordinate]
            game.game_window.blit(shot.image, shot_pos)

        '''if alien.alive:  # Only draw the alien if it's alive
            alien.move(30)  # Update the alien's position
            earth.draw(moving_objects_surface)  # Draw the earth on the moving_objects_surface
            #alien.draw(moving_objects_surface)  # Draw the alien on the moving_objects_surface
        else:
            moving_objects_surface.fill((0, 0, 0, 0))  # Clear the moving_objects_surface if the alien is not alive
            earth.draw(moving_objects_surface)  # Draw the earth on the moving_objects_surface'''

        for enemy in enemy_group:
            enemy.move(30)
            enemy.draw(moving_objects_surface)

        background_with_objects = background.copy()
        background_with_objects.blit(moving_objects_surface, (0, 0))


        moving_objects_surface.fill((0, 0, 0, 0))  # Clear the moving_objects_surface
        alien.move(30)  # Update the alien's position
        earth.draw(moving_objects_surface)  # Draw the earth on the moving_objects_surface
        alien.collide(shot, x1, y1)
        alien.handle_collision(shot)
        if shot_active:
            alien.handle_collision(shot)
        if not alien.alive:
            continue
        else:
            alien.draw(moving_objects_surface)  # Draw the alien on the moving_objects_surface

        background_with_objects = background.copy()
        background_with_objects.blit(moving_objects_surface, (0, 0))
        
        #if (shot_pos[0] < 0 or shot_pos[0] > game.window_x or shot_pos[1] < 0 or shot_pos[1] > game.window_y):
        if shot.is_out_of_bounds(game.window_x, game.window_y):
            shot_active = False

        #if shot_active and pygame.Rect(shot_pos, shot.get_size()).collidepoint(crosshair_pos):
        if shot_active and pygame.Rect((shot.x_coordinate, shot.y_coordinate), (shot_width, shot_height)).collidepoint(crosshair_pos):
            shot_active = False

        crosshair.draw(game.game_window)

        pygame.display.update()

    pygame.quit()


def mainmenu():
	# Create a menu object
	menu = pygame_menu.Menu('SPACE RACE', game.window_x, game.window_y, theme=pygame_menu.themes.THEME_DARK.copy())
	
	# Adding features to the menu
	menu.add.button('Play', start)
	menu.add.selector('Map: ', [('1', "background1v2.png"), ('2', "background2v2.png"), ('3', "background3v2.png"), ('4', "background4v2.png"), ('5', "background5v2.png")], onchange=set_map)
	menu.add.text_input('Name: ')
	menu.add.button('Quit', pygame_menu.events.EXIT)
	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
				
		if menu.is_enabled():
			menu.update(events)
			menu.draw(game.game_window)
		
		pygame.display.update()

mainmenu()