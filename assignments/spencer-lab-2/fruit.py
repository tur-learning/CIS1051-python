import pygame
import game

# # Setup initial fruit position
# #TODO
posi = game.random_pos()

#do not spawn the fruit
spawn = False

#spawns the fruit
def init():
    spawn = True


#     #TODO

#draw the fruit on the window
def draw(game_window):
    pygame.draw.rect(game_window, game.white, (posi[0], posi[1], 10, 10))

#returning the random position function to reassign the position of the fruit to another one.
def locate():
    return(game.random_pos())
# TODO