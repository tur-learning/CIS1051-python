import math
import pygame
import random

# Initialization
pygame.init()

fps = pygame.time.Clock()

# Window size
window_x = 1000
window_y = 1000
  
# Initializing game window
pygame.display.set_caption("Endless Scrolling")
game_window = pygame.display.set_mode((window_x,
                                       window_y))
  
# Loading images to be displayed
zoom_1 = 20*0.6
zoom_2 = 20
background = pygame.image.load("your_new_image.png").convert()
background = pygame.transform.scale(background, (window_x*zoom_1, window_y*zoom_1))

bg_frame = background.get_rect()

ship = pygame.image.load("spaceship.png").convert_alpha()
ship = pygame.transform.scale(ship, (window_x/zoom_2, window_y/zoom_2))
  
# Scrolling variable
scroll = 0
  
# Amount of maximum contemporary repetitions of the background 
# over the game window
tiles = math.ceil(window_x / background.get_width()) + 1 

speed = 10
x1 = random.randint(0, window_x)#background.get_rect().centerx
y1 = random.randint(0, window_y)#background.get_rect().centery
  
# Main loop
while True:

    # Setting the fps
    fps.tick(30)

    movement = [0, 0]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        movement[0] =   speed
    elif keys[pygame.K_LEFT]:
        movement[0] = - speed
    if keys[pygame.K_UP]:
        movement[1] = - speed
    elif keys[pygame.K_DOWN]:
        movement[1] =   speed

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

    game_window.blit(background, (0,0), quad_1)
    game_window.blit(background, (w1,0), quad_2)
    game_window.blit(background, (w1,h1), quad_3)
    game_window.blit(background, (0,h1), quad_4)

    # scroll update (the number represents the scroll velocity)

    # Reset the scroll variable after a complete cycle
    # (at the end of the background picture)
    if abs(scroll) > background.get_width():
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
  
    # Adding an image on top of the background 
    # (have a look at the blit method)
    game_window.blit(ship, ((window_x-ship.get_width())/2, (window_y-ship.get_height())/2))

    pygame.display.update()
  
pygame.quit()
