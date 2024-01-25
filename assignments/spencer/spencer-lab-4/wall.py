import fruit
import game
import main
import snake
import pygame
import random

position = game.random_pos()

spawn = False

def init():
    spawn = True


#list of wall coordinates that are on the screen
walls_on_screen = [] 



#making random variables either -1 or 1 inside my function to act as random rotation for the walls
 #make corner blocks from each item in the walls on screen list.
def corner_wall(blocks):
    a = random.choice([-1, 1])
    b = random.choice([-1, 1])
    cornerwall = ([blocks[0], blocks[1]],
                [blocks[0] + a*10, blocks[1]],
                 [blocks[0] + a*20, blocks[1]],
                 [blocks[0], blocks[1] - b*10],
                 [blocks[0], blocks[1] - b*20])
    return cornerwall




#trying to draw all the walls at once
def draw(game_window):
    for wallblock in walls_on_screen:
        pygame.draw.rect(game_window, game.red, pygame.Rect(
                     wallblock[0], wallblock[1], 10, 10))
        
#random position of walls but offsetting them so they do not spawn off the screen
def random_pos():
    pos = [random.randrange(1, ((game.window_x-40)//10)) * 10,
           random.randrange(1, ((game.window_y-40)//10)) * 10]
    return pos

#same function with different parameters to make the spawning work somehow.
def random_pos2():
    pos = [random.randrange(1, ((game.window_x-35)//10)) * 10,
           random.randrange(1, ((game.window_y-35)//10)) * 10]
    return pos

#getting a random position for the walls
def locate():
    return random_pos()

#function used to add new wall coordinates to the list of walls. caps the wall list at 5 walls
def add_wall():
    #ai help edit not sure if this does anything but the code works so im not touching it :)
    global spawn
    #my code
    new_position = random_pos()
    cornerwall = corner_wall(new_position)
    
    #essentially i assigned the cornerwall variable to the return value of the corner_wall function to 
    # then append it to the walls on screen list block by block.
    for block in cornerwall:
        walls_on_screen.append(block)

#Limiting the number of walls to 5
    spawn = True
    if len(walls_on_screen) > 25:
        for _ in range(5):
            walls_on_screen.pop(0)

