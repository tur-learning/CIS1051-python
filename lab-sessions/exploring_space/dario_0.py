import math
import pygame

# Initialization
pygame.init()

fps = pygame.time.Clock()

# Window size
window_x = 600
window_y = 600
  
# Initializing game window
pygame.display.set_caption("Endless Scrolling")
game_window = pygame.display.set_mode((window_x,
                                       window_y))
  
# Loading images to be displayed
zoom = 10
background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (window_x*zoom, window_y*zoom))

ship = pygame.image.load("spaceship.png").convert_alpha()
ship = pygame.transform.scale(ship, (window_x/zoom, window_y/zoom))
  
# Scrolling variable
scroll = 0
  
# Amount of maximum contemporary repetitions of the background 
# over the game window
tiles = math.ceil(window_x / background.get_width()) + 1 

movement = [0, 0, 0, 0]
speed = 15
  
# Main loop
while True:
    # Setting the fps
    fps.tick(30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        movement[0] += speed
    if keys[pygame.K_LEFT]:
        movement[1] += speed
    if keys[pygame.K_UP]:
        movement[2] += speed
    if keys[pygame.K_DOWN]:
        movement[3] += speed

    # Appending the image at the end of itself
    # keep in mind, this is done within the loop
    #i = 0
    #while(i < tiles):
       #game_window.blit(background, (background.get_width()*i
       #                 + scroll, 0))

    cropped_region = ((background.get_width()-window_x)/2 + movement[0] - movement[1],
                      (background.get_height()-window_y)/2 + movement[3] - movement[2],
                      window_x,
                      window_y)
    
    game_window.blit(background, (0, 0), cropped_region)

    ## La variabile offset mi dice di quanto sta sconfinando la finestra in uscita       
    #offset = (movement[0] - movement[1] + window_x) - background.get_width()
    ## Crop della prima zona di dimensioni fisse
    #cropped_region_1 = (movement[0] - movement[1], 0, window_x, window_y)
    ## Crop della seconda zona di dimensioni variabili (vertice fisso in zero e lunghezza data da offset)
    #cropped_region_2 = (0, 0, offset, window_y)
    ## Blit della prima zona standard
    #game_window.blit(background, (0, 0), cropped_region_1)
    ## Blit della seconda zona sovrapposta alla prima, a partire da x = window_x - offset
    #game_window.blit(background, (window_x - offset, 0), cropped_region_2)

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
