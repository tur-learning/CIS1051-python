import math
import pygame
import random
import planet
import enemy
import map

def show_periodic_background(x1, y1, bkg):
    x1 = (bg_frame.width  + x1 + movement[0]) % bg_frame.width
    y1 = (bg_frame.height + y1 + movement[1]) % bg_frame.height
  
    v1 = (x1, y1)
    v2 = ( 0, y1)
    v3 = ( 0,  0)
    v4 = (x1,  0)

    window_frame = pygame.Rect(v1, (window_x, window_y))

    w2 = max(0, window_frame.right - bg_frame.right)
    w1 = window_frame.width - w2
    w3 = w2 ; w4 = w1

    h4 = max(0, window_frame.bottom - bg_frame.bottom)
    h1 = window_frame.height - h4
    h2 = h1 ; h3 = h4
        
    quad_1 = pygame.Rect(v1, (w1, h1))
    quad_2 = pygame.Rect(v2, (w2, h2))
    quad_3 = pygame.Rect(v3, (w3, h3))
    quad_4 = pygame.Rect(v4, (w4, h4))

    game_window.blit(bkg, (0,0), quad_1)
    game_window.blit(bkg, (w1,0), quad_2)
    game_window.blit(bkg, (w1,h1), quad_3)
    game_window.blit(bkg, (0,h1), quad_4)

    return x1, y1

# Initialization
pygame.init()

fps = pygame.time.Clock()

# Window size
window_x = 1000
window_y = 1000
  
# Initializing game window
pygame.display.set_caption("Exploring Space")
game_window = pygame.display.set_mode((window_x,
                                       window_y))

# Hide cursor here
pygame.mouse.set_visible(False)

# Loading images to be displayed
zoom_1 = 10*0.6
zoom_2 = 20
bkg_map = map.Map(0., 0., window_x, window_y, zoom_1, "background.png")

ship = pygame.image.load("spaceship.png").convert_alpha()
ship = pygame.transform.scale(ship, (window_x/zoom_2, window_y/zoom_2))

target_image = pygame.image.load("target.png").convert_alpha()
target_image = pygame.transform.scale(target_image, (window_x/zoom_2, window_y/zoom_2))
target_rect = target_image.get_rect()

shot_image = pygame.image.load("shot.png").convert_alpha()
shot_image = pygame.transform.scale(shot_image, (window_x/zoom_2, window_y/zoom_2))
shot_rect = shot_image.get_rect()
shot_rect.center = game_window.get_rect().center
shot_moving = False

speed = 10
x1 = random.randint(0, window_x)
y1 = random.randint(0, window_y)

x2 = random.randint(0, window_x)
y2 = random.randint(0, window_y)

# Create a planet
earth = planet.Planet(x2, y2, 500, 0, 0, "earth.png")
moon = planet.Planet(x2 + 800, y2, 100, x2, y2, "moon.png")

# Create an enemy
alien = enemy.Enemy(x2 + 400., y2, 600, x2, y2, "enemy.png")

end_pos = (-1, -1)

# Create a black surface background to blit surfaces on
background = bkg_map.scaled_surface.copy()
background.fill('black')
bg_frame = background.get_rect()

# Main loop
while True:

    # Setting the fps
    fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and not shot_moving:
            # Start moving the shot to the mouse position on click
            shot_moving = True
            start_pos = shot_rect.center
            end_pos = pygame.mouse.get_pos()
            direction = pygame.math.Vector2(end_pos) - pygame.math.Vector2(start_pos)
            shot_speed = 1

    movement = [0, 0]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        movement[0] =   speed
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        movement[0] = - speed
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        movement[1] = - speed
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        movement[1] =   speed

    x1, y1 = show_periodic_background(x1, y1, background)

    # Draw the map on top of the black background
    bkg_map.draw(background)

    # Draw the planet on top of the map
    earth.draw(background)

    # Draw the moon on top of the map
    moon.move_around_circle(1)
    moon.draw(background)

    # Draw the alien on top of the map
    alien.move_around_circle(2)
    alien.draw(background)

    # Draw the ship on the game window center
    game_window.blit(ship, ((window_x-ship.get_width())/2, (window_y-ship.get_height())/2))

    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Center the target sprite at the mouse position
    target_rect.center = mouse_pos
    
    # Draw the target sprite on the game_window
    game_window.blit(target_image, target_rect)

    if shot_moving:
        # Move the shot toward the clicked position over time
        delta_time = 30.
        distance = direction.normalize() * shot_speed * delta_time
        shot_rect.move_ip(distance)
        game_window.blit(shot_image, shot_rect)

    # Check if the shot has reached the clicked position
    if shot_rect.collidepoint(end_pos):
        shot_moving = False
        shot_rect.center = game_window.get_rect().center

    pygame.display.update()
  
pygame.quit()