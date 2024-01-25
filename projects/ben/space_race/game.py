import pygame


'''
    Simple module for the game window
    setup and caption set up.
'''
# Window size
window_x = 1500
window_y = 776

# Initializing game window
pygame.display.set_caption("The Space Race")
game_window = pygame.display.set_mode((window_x,
                                    window_y))
