import math
import pygame

# Initialization
pygame.init()

fps = pygame.time.Clock()

# Window size
window_x = 800
window_y = 600
  
# Initializing game window
pygame.display.set_caption("Endless Scrolling")
game_window = pygame.display.set_mode((window_x,
                                       window_y))
  
# Loading images to be displayed
background = pygame.image.load("snoopy.png").convert()
donald = pygame.image.load("donald_duck.png").convert_alpha()
  
# Scrolling variable
scroll = 0
  
# Amount of maximum contemporary repetitions of the background 
# over the game window
tiles = math.ceil(window_x / background.get_width()) + 1 
  
# Main loop
while True:
    # Setting the fps
    fps.tick(30)

    # Appending the image at the end of itself
    # keep in mind, this is done within the loop
    i = 0
    while(i < tiles):
       game_window.blit(background, (background.get_width()*i
                        + scroll, 0))
       i += 1

    # scroll update (the number represents the scroll velocity)
    scroll -= 6 # try to change this value

    # Reset the scroll variable after a complete cycle
    # (at the end of the background picture)
    if abs(scroll) > background.get_width():
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
  
    # Adding an image on top of the background 
    # (have a look at the blit method)
    game_window.blit(donald, (400, 300))

    pygame.display.update()
  
pygame.quit()
