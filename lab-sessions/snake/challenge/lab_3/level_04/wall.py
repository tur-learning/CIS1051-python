import fruit
import game
import main
import snake
import pygame

position = game.random_pos()

spawn = False

def init():
    spawn = True

def walls():
    walls_on_screen = []


def draw(game_window):
    pygame.draw.rect(game_window, game.red, pygame.Rect(
                     position[0], position[1], 10, 10))

def locate():
    return game.random_pos()

def add_wall():
    new_position = game.random_pos()



    #This is copied from the fruit. i need to make it add to a list of up to 5. 
    #TODO
    #create list of walls
    #make way to add random wall to list
    #cap list at 5 elements
    #make it so the snake dies when a wall is hit
    #smile and take a deep breath. its ok :)