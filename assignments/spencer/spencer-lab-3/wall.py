import fruit
import game
import main
import snake
import pygame

position = game.random_pos()

spawn = False

def init():
    spawn = True

#list of wall coordinates that are on the screen
walls_on_screen = [position, [position[0] + 10, position[1]],
                 [position[0] + 20, position[1]],
                 [position[0], position[1] - 10],
                 [position[0], position[1] - 20]]




 #trying to make corner blocks from each item in the walls on screen list.
def corner_wall(blocks):
    cornerwall = ([blocks[0], blocks[1]],
                [blocks[0] + 10, blocks[1]],
                 [blocks[0] + 20, blocks[1]],
                 [blocks[0], blocks[1] - 10],
                 [blocks[0], blocks[1] - 20])
    return cornerwall




#trying to draw all the walls at once
def draw(game_window):
    for wallblock in walls_on_screen:
        pygame.draw.rect(game_window, game.red, pygame.Rect(
                     wallblock[0], wallblock[1], 10, 10))
        


#getting a random position for the walls
def locate():
    return game.random_pos()

#function used to add new wall coordinates to the list of walls. caps the wall list at 5 walls
def add_wall():
    #ai help edit not sure if this does anything but the code works so im not touching it :)
    global spawn
    #my code
    new_position = game.random_pos()
    cornerwall = corner_wall(new_position)
    #essentially i assigned the cornerwall variable to the return value of the corner_wall function to then append it to the walls on screen list block by block
    for block in cornerwall:
        walls_on_screen.append(block)

    spawn = True
    if len(walls_on_screen) > 25:
        for _ in range(5):
            walls_on_screen.pop(0)

